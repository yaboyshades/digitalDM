"""
Dungeon Master (Game Coordinator)
Manages multi-agent interactions and game flow.
"""
import random
import sys
import os

# FORCE ADD D_Master_1 TO sys.path
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))  # Get `game/` directory
PROJECT_ROOT = os.path.abspath(os.path.join(ROOT_DIR, '..'))  # Go up to `D_Master_1`
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)  # Add to Python's module search path

print("🔍 sys.path:", sys.path)  # Debugging output

from agents.intent_parsing_agent import IntentParsingAgent
from agents.scene_tracking_agent import SceneTrackingAgent
from agents.character_database_agent import CharacterDatabaseAgent
from agents.reinforcement_learning_agent import ReinforcementLearningAgent

class DungeonMaster:
    def __init__(self):
        self.intent_agent = IntentParsingAgent("IntentAgent")
        self.scene_agent = SceneTrackingAgent("SceneAgent")
        self.character_agent = CharacterDatabaseAgent("CharacterDB")
        self.reinforcement_agent = ReinforcementLearningAgent("RLAgent")

    def process_player_action(self, action):
        """Processes player actions via relevant agents."""
        print("\n🔍 Player Action:", action)

        # Parse Intent
        intent_data = self.intent_agent.process_input(action)
        print("🧠 Parsed Intent:", intent_data)

        # Scene Awareness
        scene_description = self.scene_agent.get_scene_state()
        print("🌎 Scene State:", scene_description)

        # Retrieve Character Info
        character_info = self.character_agent.get_character(intent_data["target"]) if intent_data["target"] else {}
        print("🎭 Character Info:", character_info)

        # Update Learning Model
        self.reinforcement_agent.update_q_value(intent_data["intent"], "engage", random.uniform(0.5, 1))
        print("📈 Reinforcement Learning Updated!")

        return f"Action '{action}' processed with intent '{intent_data['intent']}'."
