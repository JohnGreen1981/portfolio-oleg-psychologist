from __future__ import annotations

import math
import re
from collections import Counter

from .models import MemoryRecord, UserProfile

TOKEN_RE = re.compile(r"[a-zа-яё0-9]+", re.IGNORECASE)


def tokenize(text: str) -> Counter[str]:
    return Counter(token.lower() for token in TOKEN_RE.findall(text))


def cosine_score(left: Counter[str], right: Counter[str]) -> float:
    if not left or not right:
        return 0.0
    common = set(left) & set(right)
    dot = sum(left[token] * right[token] for token in common)
    left_norm = math.sqrt(sum(value * value for value in left.values()))
    right_norm = math.sqrt(sum(value * value for value in right.values()))
    return dot / (left_norm * right_norm)


class MemoryStore:
    """In-memory stand-in for a pgvector-backed memory store."""

    def __init__(self) -> None:
        self._records: list[MemoryRecord] = []
        self._profile = UserProfile()

    @property
    def profile(self) -> UserProfile:
        return self._profile

    @property
    def records(self) -> tuple[MemoryRecord, ...]:
        return tuple(self._records)

    def save(self, record: MemoryRecord) -> None:
        self._records.append(record)
        self._profile = self._profile.with_facts(*record.key_facts)

    def search(self, query: str, limit: int = 3) -> list[MemoryRecord]:
        query_vector = tokenize(query)
        scored = [
            (cosine_score(query_vector, tokenize(record.content + " " + record.summary)), record)
            for record in self._records
        ]
        return [record for score, record in sorted(scored, key=lambda item: item[0], reverse=True)[:limit] if score > 0]
