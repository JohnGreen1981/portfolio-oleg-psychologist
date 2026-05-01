# Oleg Psychologist Demo

## Назначение

Очищенный портфельный demo repo для проекта персонального AI-психолога с долгосрочной памятью.

Это не копия production-проекта. Оригинальная предметная область чувствительная, поэтому публичная версия показывает архитектуру на синтетических данных: сессионный буфер, сохранение резюме, поиск по памяти, профиль пользователя и safety boundaries.

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

## Портфельная рамка

Проект представлен как AI-assisted architecture case study для чувствительного Telegram-бота. Фокус: memory design, privacy boundaries, UX логика сессий, safety handling и то, как такой продукт можно описать проверяющему без публикации личных данных.

Не описывать demo как медицинский продукт, терапию или замену специалиста.

## Privacy / Safety

В публичный репозиторий не входят реальные сессии, психологический профиль, owner IDs, Telegram tokens, Supabase details, домены, VPS-пути, production prompts и deployment settings.

Все примеры должны быть синтетическими и нейтральными.

## Правила

- Не коммитить `.env`, tokens, Supabase keys, user IDs, real session text, profile facts, therapy notes, domains, IP, VPS paths.
- Если добавляются примеры памяти, они должны быть fake/demo.
- При изменении Python-кода запускать `python3 -m py_compile $(find src -name '*.py')`.
- Перед GitHub push запускать tests и secret scan.
- `CLAUDE.md` должен оставаться ссылкой на `AGENTS.md`.
