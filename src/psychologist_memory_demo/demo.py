from __future__ import annotations

from .memory import MemoryStore
from .prompt import build_prompt_context
from .session import SessionBuffer


def main() -> None:
    memory = MemoryStore()
    session = SessionBuffer(memory)

    first = "Факт: я лучше думаю после прогулки. Хочу спокойнее реагировать на рабочие сообщения."
    warning = session.add_user_message(first)
    if warning:
        print(warning)
    session.add_assistant_message("Попробуй перед ответом сделать паузу и назвать одну конкретную эмоцию.")
    record = session.save_and_reset()

    query = "Рабочие сообщения снова вызывают тревогу."
    memories = memory.search(query)
    print("Saved summary:", record.summary)
    print()
    print(build_prompt_context(memory.profile, memories, query))


if __name__ == "__main__":
    main()
