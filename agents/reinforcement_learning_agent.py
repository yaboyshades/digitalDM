"""
Reinforcement Learning Agent
Implements Q-learning to adapt agent behavior.
"""

import random
from agents.base_agent import BaseAgent


class ReinforcementLearningAgent(BaseAgent):
    def __init__(self, agent_id):
        super().__init__(agent_id, "Reinforcement Learning")
        self.q_table = {}

    def choose_action(self, state, actions):
        """Selects an action using Q-learning."""
        if state in self.q_table:
            return max(self.q_table[state], key=self.q_table[state].get)
        return random.choice(actions)

    def update_q_value(self, state, action, reward):
        """Updates Q-values based on rewards."""
        if state not in self.q_table:
            self.q_table[state] = {}
        self.q_table[state][action] = reward
