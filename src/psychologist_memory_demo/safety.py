from __future__ import annotations

CRISIS_TERMS = {
    "суицид",
    "самоубийство",
    "убить себя",
    "не хочу жить",
    "навредить себе",
}

MEDICAL_TERMS = {
    "диагноз",
    "таблетки",
    "лекарства",
    "дозировка",
    "психиатр",
}

LEGAL_TERMS = {"суд", "иск", "заявление", "адвокат", "договор"}


def classify_boundary(text: str) -> str:
    lowered = text.lower()
    if any(term in lowered for term in CRISIS_TERMS):
        return "crisis"
    if any(term in lowered for term in MEDICAL_TERMS):
        return "medical"
    if any(term in lowered for term in LEGAL_TERMS):
        return "legal"
    return "normal"


def boundary_reply(boundary: str) -> str | None:
    replies = {
        "crisis": (
            "Я не могу заменить экстренную помощь. Если есть риск причинить вред себе "
            "или другому человеку, нужно немедленно обратиться в местную службу экстренной "
            "помощи или к близкому человеку рядом."
        ),
        "medical": (
            "Я могу помочь структурировать мысли, но не назначаю лечение и не меняю "
            "дозировки. Медицинские вопросы нужно обсуждать с врачом."
        ),
        "legal": (
            "Я не даю юридических заключений. Могу помочь сформулировать вопросы, "
            "которые стоит обсудить со специалистом."
        ),
    }
    return replies.get(boundary)
