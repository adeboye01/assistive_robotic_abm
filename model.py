from mesa import Model
from agent import ResidentAgent
from agent import NurseAgent
from agent import RobotAgent
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import mesa

class CareHomeModel(Model):
    """A model with some number of agents."""

    def __init__(self, n_residents, n_nurses, n_robots, width, height):
        self.num_residents = n_residents
        self.num_nurses = n_nurses
        self.num_robots = n_robots
        self.headings = {(1, 0), (0, 1), (-1, 0), (0, -1)}
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)
        self.running = True
        # Create agents
        for t in range(self.num_robots):
            #pos = (x, y)
            heading = (1, 0)
            k = RobotAgent(t,self)
            self.schedule.add(k)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(k, (20, 60))
        
        for r in range(self.num_robots+1, self.num_nurses+self.num_robots+1):
            pos = (x, y)
            heading = (1, 0)
            f = NurseAgent(r,self)
            self.schedule.add(f)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(f, (60, 60))
        for i in range(self.num_robots+1,self.num_nurses+self.num_residents+self.num_robots+1):
            a = ResidentAgent(i, self)
            #self.schedule.add(a)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (38,20))      
    def step(self):
        self.schedule.step()