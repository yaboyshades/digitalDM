"""
Character Database Agent
Stores and retrieves character data dynamically.
"""

from agents.base_agent import BaseAgent


class CharacterDatabaseAgent(BaseAgent):
    def __init__(self, agent_id):
        super().__init__(agent_id, "Character Database")
        self.character_db = {
            "Goblin King": {"name": "Goblin King", "traits": ["aggressive", "cunning"], "position": (10, 5)},
            "Merchant": {"name": "Merchant", "traits": ["friendly", "greedy"], "position": (2, 3)}
        }

    def get_character(self, name):
        """Retrieves character data."""
        return self.character_db.get(name, {"name": name, "traits": [], "position": (0, 0)})

    def update_character(self, name, new_data):
        """Updates character attributes."""
        self.character_db[name] = new_data
