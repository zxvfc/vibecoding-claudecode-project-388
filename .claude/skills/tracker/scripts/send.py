#!/usr/bin/env python3
"""Send a text message to a Telegram chat via the Bot API.

Usage:
    python send.py "текст сообщения"

Credentials (TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID) are read from the
environment, falling back to a .env file next to this script.
"""
import json
import os
import sys
import urllib.error
import urllib.request

API_URL = "https://api.telegram.org/bot{token}/sendMessage"
ENV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")


def load_env_file(path):
    values = {}
    if not os.path.isfile(path):
        return values
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            values[key] = value
    return values


def get_credentials():
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        env_values = load_env_file(ENV_PATH)
        token = token or env_values.get("TELEGRAM_BOT_TOKEN")
        chat_id = chat_id or env_values.get("TELEGRAM_CHAT_ID")
    return token, chat_id


def send_message(token, chat_id, text):
    url = API_URL.format(token=token)
    payload = json.dumps({"chat_id": chat_id, "text": text}).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=15) as response:
        return json.loads(response.read().decode("utf-8"))


def main():
    if len(sys.argv) != 2:
        print('Использование: python send.py "текст сообщения"', file=sys.stderr)
        return 1

    text = sys.argv[1]
    token, chat_id = get_credentials()
    if not token or not chat_id:
        print(
            "Не заданы TELEGRAM_BOT_TOKEN и/или TELEGRAM_CHAT_ID "
            "(переменные окружения или .env рядом со скриптом).",
            file=sys.stderr,
        )
        return 1

    try:
        result = send_message(token, chat_id, text)
    except urllib.error.HTTPError as e:
        print(f"Telegram API вернул ошибку {e.code}: {e.read().decode('utf-8', 'replace')}", file=sys.stderr)
        return 1
    except urllib.error.URLError as e:
        print(f"Не удалось подключиться к Telegram: {e.reason}", file=sys.stderr)
        return 1

    if not result.get("ok"):
        print(f"Telegram API вернул ошибку: {result}", file=sys.stderr)
        return 1

    print("Сообщение отправлено.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
