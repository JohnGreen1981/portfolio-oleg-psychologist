from __future__ import annotations

from datetime import datetime, timedelta, timezone

from .memory import MemoryStore
from .models import MemoryRecord, Message
from .safety import boundary_reply, classify_boundary

SAVE_TRIGGERS = (
    "запомни",
    "зафиксируй",
    "сохрани",
    "итоги",
    "закончим сеанс",
    "закрыть сеанс",
)


class SessionBuffer:
    def __init__(self, memory: MemoryStore, idle_timeout: timedelta = timedelta(minutes=30)) -> None:
        self.memory = memory
        self.idle_timeout = idle_timeout
        self.messages: list[Message] = []
        self.last_message_at: datetime | None = None

    def add_user_message(self, text: str, now: datetime | None = None) -> str | None:
        current_time = now or datetime.now(timezone.utc)
        boundary = classify_boundary(text)
        self.messages.append(Message(role="user", text=text, created_at=current_time))
        self.last_message_at = current_time
        return boundary_reply(boundary)

    def add_assistant_message(self, text: str, now: datetime | None = None) -> None:
        current_time = now or datetime.now(timezone.utc)
        self.messages.append(Message(role="assistant", text=text, created_at=current_time))
        self.last_message_at = current_time

    def should_save(self, latest_user_text: str, now: datetime | None = None) -> bool:
        lowered = latest_user_text.lower()
        if any(trigger in lowered for trigger in SAVE_TRIGGERS):
            return True
        if self.last_message_at is None:
            return False
        current_time = now or datetime.now(timezone.utc)
        return current_time - self.last_message_at >= self.idle_timeout

    def save_and_reset(self) -> MemoryRecord:
        if not self.messages:
            raise ValueError("Cannot save an empty session.")

        user_messages = [message.text for message in self.messages if message.role == "user"]
        assistant_messages = [message.text for message in self.messages if message.role == "assistant"]
        content = "\n".join(f"{message.role}: {message.text}" for message in self.messages)
        summary = summarize(user_messages)
        record = MemoryRecord(
            content=content,
            summary=summary,
            mood=detect_mood(user_messages),
            goals=extract_goals(user_messages),
            next_steps=extract_next_steps(assistant_messages),
            key_facts=extract_key_facts(user_messages),
        )
        self.memory.save(record)
        self.messages.clear()
        self.last_message_at = None
        return record


def summarize(messages: list[str]) -> str:
    joined = " ".join(messages).strip()
    if not joined:
        return "Пустая сессия."
    return joined[:180] + ("..." if len(joined) > 180 else "")


def detect_mood(messages: list[str]) -> str:
    text = " ".join(messages).lower()
    if any(word in text for word in ("тревожно", "страшно", "переживаю", "устал")):
        return "напряжение"
    if any(word in text for word in ("спокойно", "легче", "получилось")):
        return "стабилизация"
    return "нейтрально"


def extract_goals(messages: list[str]) -> tuple[str, ...]:
    goals = []
    for text in messages:
        lowered = text.lower()
        if "хочу" in lowered or "цель" in lowered:
            goals.append(text.strip())
    return tuple(goals[:3])


def extract_next_steps(messages: list[str]) -> tuple[str, ...]:
    steps = []
    for text in messages:
        if "попробуй" in text.lower() or "следующий шаг" in text.lower():
            steps.append(text.strip())
    return tuple(steps[:3])


def extract_key_facts(messages: list[str]) -> tuple[str, ...]:
    facts = []
    for text in messages:
        lowered = text.lower()
        if lowered.startswith("факт:"):
            raw_fact = text.split(":", 1)[1].strip()
            facts.append(raw_fact.split(".", 1)[0].strip())
    return tuple(facts[:5])
