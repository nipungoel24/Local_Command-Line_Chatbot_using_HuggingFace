# chat_memory.py

from collections import deque

class ChatMemory:
    def __init__(self, max_turns=5):
        self.max_turns = max_turns
        self.history = deque(maxlen=max_turns)

    def add_turn(self, user_input, bot_reply):
        turn = f"[INST] {user_input} [/INST] {bot_reply}"
        self.history.append(turn)

    def get_context(self):
        return "\n".join(self.history)
