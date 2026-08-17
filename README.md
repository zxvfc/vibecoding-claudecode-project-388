# jib.co.th price tracker

Отслеживает цены на компьютерное железо и периферию на
[jib.co.th](https://www.jib.co.th/) — тайском интернет-магазине. Список
конкретных товаров зашит в скилл `tracker` (см.
`.claude/skills/tracker/SKILL.md`) и меняется по мере добавления новых
позиций; сейчас это видеокарты, геймпады/рули и процессоры/материнские
платы. Отслеживание нужно, чтобы узнавать об изменении цены или
рассрочки раньше, чем пришлось бы проверять страницы вручную, и иметь
историю цен по каждому товару, а не только последнее значение.

«Цена» в этой нише — не одно число: `extract-price` (см.
`.claude/skills/extract-price/SKILL.md`) различает обычную цену
(`regular_price`) и цену по скидке/акции (`sale_price`, которой может не
быть), плюс отдельно фиксирует, доступна ли рассрочка (`has_credit`) —
на jib.co.th это отдельное условие покупки, а не часть цены. Валюта
везде — тайский бат (THB). Правила о том, какое изменение этих полей
достаточно значимо для уведомления, а какое — шум, описаны в
`KNOWLEDGE.md`.

### Hexlet tests and linter status:
[![Actions Status](https://github.com/zxvfc/vibecoding-claudecode-project-388/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/zxvfc/vibecoding-claudecode-project-388/actions)