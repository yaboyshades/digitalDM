"""
Intent Parsing Agent
Parses player actions into structured intent, subject, and target.
"""

from agents.base_agent import BaseAgent  # ✅ Correct import path


class IntentParsingAgent(BaseAgent):
    def __init__(self, agent_id: str) -> None:
        """Initializes an IntentParsingAgent.

        Args:
            agent_id (str): The unique identifier for the agent.
        """
        super().__init__(agent_id, "Intent Parsing")

    def process_input(self, player_action):
        """Extracts intent from player actions."""
        keywords = {
            "combat": ["attack", "fight", "strike"],
            "exploration": ["search", "explore", "look"],
            "social": ["talk", "persuade", "negotiate"]
        }
        for intent, words in keywords.items():
            if any(word in player_action.lower() for word in words):
                target = "enemy" if intent == "combat" else "environment" if intent == "exploration" else "NPC"
                return {"intent": intent, "target": target, "context": player_action}
        return {"intent": "unknown", "target": None, "context": player_action}
