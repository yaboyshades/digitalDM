
"""
Base Agent Class
Defines the structure for all agents, including memory and basic communication.
"""

class BaseAgent:
    def __init__(self, agent_id, specialization):
        self.agent_id = agent_id
        self.specialization = specialization
        self.memory = {}  # Adaptive knowledge storage

    def process_input(self, input_data):
        """Abstract method to be overridden by subclasses."""
        raise NotImplementedError("Agents must implement process_input method.")

    def update_memory(self, key, data, importance=1.0):
        """Stores adaptive knowledge with weighted forgetting."""
        if key not in self.memory:
            self.memory[key] = (data, importance)
        else:
            prev_data, prev_importance = self.memory[key]
            self.memory[key] = (data, (prev_importance + importance) / 2)

    def forget_low_importance(self, threshold=0.2):
        """Removes low-importance data from memory."""
        self.memory = {k: v for k, v in self.memory.items() if v[1] > threshold}
