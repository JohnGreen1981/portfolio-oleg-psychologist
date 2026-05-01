from datetime import datetime, timedelta, timezone

from psychologist_memory_demo.memory import MemoryStore
from psychologist_memory_demo.prompt import build_prompt_context
from psychologist_memory_demo.session import SessionBuffer


def test_session_save_updates_memory_and_profile() -> None:
    memory = MemoryStore()
    session = SessionBuffer(memory)

    session.add_user_message("Факт: я лучше думаю после прогулки. Хочу спокойнее отвечать на сообщения.")
    session.add_assistant_message("Попробуй перед ответом сделать паузу.")
    record = session.save_and_reset()

    assert record in memory.records
    assert "я лучше думаю после прогулки" in memory.profile.facts
    assert session.messages == []


def test_memory_search_returns_relevant_record() -> None:
    memory = MemoryStore()
    session = SessionBuffer(memory)
    session.add_user_message("Хочу спокойнее реагировать на рабочие сообщения.")
    session.add_assistant_message("Следующий шаг: сделать паузу перед ответом.")
    session.save_and_reset()

    result = memory.search("рабочие сообщения")

    assert len(result) == 1
    assert "рабочие сообщения" in result[0].content


def test_boundary_reply_for_medical_request() -> None:
    memory = MemoryStore()
    session = SessionBuffer(memory)

    reply = session.add_user_message("Подскажи дозировка лекарства подойдет?")

    assert reply is not None
    assert "врачом" in reply


def test_idle_timeout_triggers_save() -> None:
    memory = MemoryStore()
    now = datetime(2026, 5, 1, tzinfo=timezone.utc)
    session = SessionBuffer(memory, idle_timeout=timedelta(minutes=30))

    session.add_user_message("Сегодня тревожно.", now=now)

    assert session.should_save("Продолжим?", now=now + timedelta(minutes=31))


def test_prompt_context_includes_profile_and_memory() -> None:
    memory = MemoryStore()
    session = SessionBuffer(memory)
    session.add_user_message("Факт: мне помогает короткая прогулка.")
    session.add_assistant_message("Попробуй выйти на 10 минут.")
    session.save_and_reset()

    context = build_prompt_context(memory.profile, memory.search("прогулка"), "Снова напряжение.")

    assert "мне помогает короткая прогулка" in context
    assert "Релевантная память" in context
