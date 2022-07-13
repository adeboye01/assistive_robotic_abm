from mesa import Model
from agent import ResidentAgent
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import mesa

class CarehomeModel(Model):
    """A model with some number of agents."""

    def __init__(self, number_of_agents, width, height):
        self.num_agents = number_of_agents
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)
        self.running = True
        

    def step(self):
        self.schedule.step()
# Create agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            self.schedule.add(a)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

    def step(self):
        self.schedule.step()
        

    
    
