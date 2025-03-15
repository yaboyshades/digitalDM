"""
Scene Tracking Agent
Manages spatial awareness and character distances using a graph.
"""

import networkx as nx
from agents.base_agent import BaseAgent


class SceneTrackingAgent(BaseAgent):
    def __init__(self, agent_id):
        super().__init__(agent_id, "Scene Tracking")
        self.scene_graph = nx.DiGraph()

    def update_scene(self, characters):
        """Updates positions and relationships in the scene."""
        self.scene_graph.clear()
        for char in characters:
            self.scene_graph.add_node(char["name"], position=char["position"])

    def get_scene_state(self):
        """Returns the current state of the scene."""
        return {node: self.scene_graph.nodes[node]["position"] for node in self.scene_graph.nodes}
