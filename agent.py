import mesa
from mesa import Agent

class ResidentAgent(mesa.Agent):
    """Resident agent."""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.residence = 1
        
    def step(self) -> None:                                                                                                             
        self.move()   
        if self.residence > 0:
            self.walk()
        
    def walk(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            other = self.random.choice(cellmates)
            other.residence += 1
            self.residence -= 1
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

class NurseAgent(mesa.Agent):
    """Resident agent."""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        #self.residence = 1
        
    def step(self) -> None:                                                                                                             
        self.move()   
        # if self.robot > 0:
        #     self.walk()
        
    def walk(self):
        #cellmates = self.model.grid.get_cell_list_contents([self.pos])
        # if len(cellmates) > 1:
        #     other = self.random.choice(cellmates)
        #     other.robot += 1
        #     self.robot -= 1
        print("walk robot")   
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)    
class RobotAgent(mesa.Agent):
    """Robot agent."""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.residence = 1
        
    def step(self) -> None:                                                                                                             
        self.move()   
        # if self.robot > 0:
        #     self.walk()
        
    def walk(self):
        #cellmates = self.model.grid.get_cell_list_contents([self.pos])
        # if len(cellmates) > 1:
        #     other = self.random.choice(cellmates)
        #     other.robot += 1
        #     self.robot -= 1
        print("walk robot")
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)   