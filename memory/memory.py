"""
Memory & Context Engineering for Voice Agent
Company: SpaceMarvel.ai
"""
import json
from typing import Dict, Any, List

class ConversationMemory:
    def __init__(self):
        self.sessions: Dict[str, List[Dict[str, Any]]] = {}

    def start_session(self, session_id: str):
        if session_id not in self.sessions:
            self.sessions[session_id] = []

    def add_message(self, session_id: str, role: str, message: str, metadata: Dict[str, Any] = None):
        self.start_session(session_id)
        entry = {
            "role": role,
            "message": message,
            "metadata": metadata or {}
        }
        self.sessions[session_id].append(entry)

    def get_history(self, session_id: str) -> List[Dict[str, Any]]:
        return self.sessions.get(session_id, [])

    def save_to_file(self, filepath: str):
        with open(filepath, "w") as f:
            json.dump(self.sessions, f)

    def load_from_file(self, filepath: str):
        try:
            with open(filepath, "r") as f:
                self.sessions = json.load(f)
        except FileNotFoundError:
            self.sessions = {}

# Example usage:
# memory = ConversationMemory()
# memory.add_message("customer_123", "agent", "Hello, how can I help you?")
# print(memory.get_history("customer_123"))
