# Skills

Заготовка для будущих скиллов Claude Code.

Каждый скилл — отдельная папка внутри `.claude/skills/` со своим файлом
`SKILL.md`:

```
.claude/skills/
  my-skill/
    SKILL.md
    scripts/      # опционально
    references/   # опционально
```

`SKILL.md` начинается с YAML frontmatter:

```yaml
---
name: my-skill
description: Краткое описание того, когда и зачем использовать этот скилл.
---

Инструкции для Claude...
```

Подробнее: https://docs.claude.com/en/docs/claude-code/skills
