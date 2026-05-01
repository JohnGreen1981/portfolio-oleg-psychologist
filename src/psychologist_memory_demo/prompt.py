from __future__ import annotations

from .models import MemoryRecord, UserProfile


def build_prompt_context(profile: UserProfile, memories: list[MemoryRecord], current_text: str) -> str:
    profile_block = "\n".join(f"- {fact}" for fact in profile.facts) or "- Подтвержденных фактов пока нет."
    memory_block = "\n".join(f"- {record.summary}" for record in memories) or "- Релевантной памяти пока нет."

    return f"""Роль: поддерживающий AI-assistant с ограничениями безопасности.

Safety:
- Не ставь диагнозы.
- Не назначай лечение.
- При кризисных формулировках направляй к экстренной помощи.
- Не выдавай терапию за медицинскую услугу.

Профиль пользователя:
{profile_block}

Релевантная память:
{memory_block}

Текущий запрос:
{current_text}

Формат ответа:
- короткий поддерживающий ответ;
- один уточняющий вопрос;
- один безопасный следующий шаг.
"""
