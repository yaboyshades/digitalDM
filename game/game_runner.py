"""
Game Runner
Simulates gameplay interactions.
"""

import sys
import os

# FORCE ADD D_Master_1 TO sys.path
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))  # Get `game/` directory
PROJECT_ROOT = os.path.abspath(os.path.join(ROOT_DIR, '..'))  # Go up to `D_Master_1`
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)  # Add to Python's module search path

print("🔍 sys.path:", sys.path)  # Debugging output

from game.dungeon_master import DungeonMaster
import random
import time

def simulate_game():
    """Runs multiple game interactions."""
    system = DungeonMaster()
    player_actions = [
        "fight the Goblin King",
        "explore the dungeon ruins",
        "talk to the Merchant"
    ]

    for _ in range(3):
        action = random.choice(player_actions)
        system.process_player_action(action)
        time.sleep(1)

if __name__ == "__main__":
    simulate_game()
