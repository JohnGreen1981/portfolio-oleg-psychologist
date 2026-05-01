# Oleg Psychologist Demo

## Назначение

Demo-репозиторий для проекта персонального AI-психолога с долгосрочной памятью.

Это не копия production-проекта. Оригинальная предметная область чувствительная, поэтому демо-версия показывает архитектуру на синтетических данных: сессионный буфер, сохранение резюме, поиск по памяти, профиль пользователя и safety boundaries.

## Стек

- Python 3.12+
- stdlib-only demo implementation
- pytest для проверок
- Markdown docs

## Структура

```text
src/psychologist_memory_demo/
  models.py          dataclasses для сообщений, памяти и профиля
  safety.py          простая классификация crisis/medical/legal boundaries
  memory.py          in-memory vector-like search по синтетическим записям
  session.py         буфер сессии, триггеры сохранения, summary generation
  prompt.py          сборка безопасного prompt context
  demo.py            CLI demo без внешних API
tests/
docs/architecture.md
```

## Роль проекта

Проект показывает архитектурный подход к чувствительному AI-ассистенту: memory design, privacy boundaries, UX логику сессий и safety handling без публикации личных данных.

Не описывать demo как медицинский продукт, терапию или замену специалиста.

## Privacy / Safety

В репозитории не хранить реальные сессии, психологический профиль, owner IDs, Telegram tokens, Supabase details, домены, VPS-пути, production prompts и deployment settings.

Все примеры должны быть синтетическими и нейтральными.

## Правила

- Не коммитить `.env`, tokens, Supabase keys, user IDs, real session text, profile facts, therapy notes, domains, IP, VPS paths.
- Если добавляются примеры памяти, они должны быть fake/demo.
- При изменении Python-кода запускать `python3 -m py_compile $(find src -name '*.py')`.
- Запускать tests и проверку на секреты перед публикацией изменений.
- `AGENTS.md` и `CLAUDE.md` должны оставаться синхронизированными по смыслу.
