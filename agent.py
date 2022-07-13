import mesa
from mesa import Agent

class ResidentAgent(mesa.Agent):
    """An agent living the care home."""

    def __init__(self, unique_id, model, level_of_movement):
        super().__init__(unique_id, model)
        self.level_of_movement = level_of_movement   
    
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
class NurseAgent(mesa.Agent):
    """An agent living the care home."""

    def __init__(self, unique_id, model, level_of_movement):
        super().__init__(unique_id, model)
        self.level_of_movement = level_of_movement   
    
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
class RobotAgent(mesa.Agent):
    """An agent living the care home."""

    def __init__(self, unique_id, model, level_of_movement):
        super().__init__(unique_id, model)
        self.level_of_movement = level_of_movement   
    
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)