# Архитектура demo

Production-проект был чувствительным персональным ботом, поэтому публичная версия показывает не реальные данные, а архитектурный скелет.

## Workflow

1. Пользователь пишет текстовое или голосовое сообщение.
2. Сообщение проходит safety boundary check.
3. Текущий session buffer собирает пары user/assistant.
4. При ручном триггере или idle timeout сессия превращается в memory record.
5. Memory store сохраняет summary, mood, goals, next steps и key facts.
6. Следующий запрос получает релевантные записи из памяти.
7. Prompt builder собирает профиль, найденную память и текущий запрос.

## Что намеренно не включено

- реальные сессии;
- психологический профиль;
- production prompt;
- Telegram owner IDs;
- Supabase URL/key;
- webhook host, домены, IP, VPS-пути;
- логи и deployment settings.

## Что демонстрирует код

- разделение runtime session и долгосрочной памяти;
- явные триггеры сохранения;
- поиск по прошлым сессиям;
- обновление профиля только из явных facts;
- safety response для crisis/medical/legal boundaries;
- воспроизводимые тесты без внешних API.
