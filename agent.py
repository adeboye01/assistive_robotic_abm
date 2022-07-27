#importing necessary modules
import mesa
from mesa import Agent
#Defining the Resident agent
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
        possible_steps = [(self.pos[0],self.pos[1]),(self.pos[0],self.pos[1]-1)]
        
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
#Defining Robot Agent
class RobotAgent(mesa.Agent):
    """Robot agent."""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.robot = 1
        
        
    def step(self) -> None:                                                                                                             
        self.move()   
        if self.robot > 0:
            self.walk()
    
    def walk(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            other = [(self.pos[0],self.pos[1]-1)]
            other.robot += 1
            self.robot -= 1
    def move(self):
        possible_steps = [(self.pos[0],self.pos[1]), (self.pos[0],self.pos[1]-1)]
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
#Defining Nurse Agent
class NurseAgent(mesa.Agent):
   """Nurse agent."""

   def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.nurse = 1      