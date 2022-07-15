from mesa import Model
from agent import ResidentAgent
from agent import NurseAgent
from agent import RobotAgent
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import mesa

class CareHomeModel(Model):
    """A model with some number of agents."""

    def __init__(self, n_residents, n_robots, width, height):
        self.num_residents = n_residents
        self.num_robots = n_robots
        self.headings = {(1, 0), (0, 1), (-1, 0), (0, -1)}
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)
        self.running = True
        # Create agents
        for i in range(self.num_residents):
            a = ResidentAgent(i, self)
            #b = NurseAgent(i, self)
            #c = RobotAgent(i, self)
            self.schedule.add(a)
            #self.schedule.add(b)
            #self.schedule.add(c)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))
        for i in range(self.num_residents+1,self.num_robots+self.num_residents):
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            pos = (x, y)
            heading = (1, 0)
            b = RobotAgent(i, pos,heading,self)
            #b = NurseAgent(i, self)
            #c = RobotAgent(i, self)
            self.schedule.add(b)
            #self.schedule.add(b)
            #self.schedule.add(c)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(b, (x, y))
    def step(self):
        self.schedule.step()
