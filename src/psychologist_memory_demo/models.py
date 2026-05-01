from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass(frozen=True)
class Message:
    role: str
    text: str
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass(frozen=True)
class MemoryRecord:
    content: str
    summary: str
    mood: str
    goals: tuple[str, ...] = ()
    next_steps: tuple[str, ...] = ()
    key_facts: tuple[str, ...] = ()
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass(frozen=True)
class UserProfile:
    facts: tuple[str, ...] = ()

    def with_facts(self, *new_facts: str) -> "UserProfile":
        cleaned = [fact.strip() for fact in new_facts if fact.strip()]
        merged = list(self.facts)
        for fact in cleaned:
            if fact not in merged:
                merged.append(fact)
        return UserProfile(tuple(merged[-12:]))
