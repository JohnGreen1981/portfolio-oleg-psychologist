# Безопасность

Не коммитить:

- therapy-like session content;
- psychological profile data;
- user identifiers / Telegram IDs;
- Supabase URL/key;
- bot tokens;
- production prompts;
- real domains, IP, VPS paths;
- logs, deployment settings, screenshots with personal data.

Перед публикацией проверить:

- `.env.example` содержит только placeholder-значения;
- в README и docs нет owner IDs, production domains, IP, Supabase details и личных фактов;
- tests используют только synthetic data;
- secret scan не находит токены и ключи;
- privacy scan не находит личные идентификаторы и production infrastructure details.
