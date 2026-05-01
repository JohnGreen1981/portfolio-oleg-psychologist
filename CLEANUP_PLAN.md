# План очистки

- [x] Выбрать безопасный формат: demo-code + case study, не production dump.
- [x] Не копировать исходные docs с owner IDs, доменами, VPS/IP, Supabase details и production settings.
- [x] Создать нейтральную demo-реализацию memory workflow на синтетических данных.
- [x] Добавить безопасный `.env.example` только с placeholder-значениями.
- [x] Добавить публичные `AGENTS.md` / `CLAUDE.md`.
- [x] Добавить explicit disclaimer: не медицинская услуга, не терапия, не замена специалиста.
- [x] Добавить tests без реальных psychological/profile/session data.
- [x] Запустить tests/syntax check.
- [x] Запустить secret/privacy scan перед первым GitHub push.
