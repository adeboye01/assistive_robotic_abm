#importing necessary modules
from mesa import Model
from agent import ResidentAgent
from agent import RobotAgent
from agent import NurseAgent
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import mesa
#defining the model
class CareHomeModel(Model):
    """A model with some number of agents."""

    def __init__(self, n_residents, n_robots, n_nurses, width, height):
        self.num_residents = n_residents
        self.num_robots = n_robots
        self.num_nurses = n_nurses
        self.headings = {(1, 0), (0, 1), (-1, 0), (0, -1)}
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)
        self.running = True
        # Create agents
        u = []
       
        for t in range(self.num_residents):
            heading = (1, 0)
            #apend element in vector 
            k = ResidentAgent(t,self)
            self.schedule.add(k)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            u.append(x) 
            
            self.grid.place_agent(k, (x,75))
            
        
        
        for r,s in enumerate(range(self.num_residents+1, self.num_robots+self.num_residents+1)):
        
            heading = (1, 0)
            l = RobotAgent(s,self)
            self.schedule.add(l)
            # Add the agent to a random grid cell 
            v = (u[r])
            self.grid.place_agent(l, (v,65))
            
            
        for a in range(self.num_residents+1, self.num_nurses+self.num_robots+self.num_residents+1):
        
            heading = (1, 0)
            l = NurseAgent(a,self)
            #self.schedule.add(l)            
            self.grid.place_agent(l, (35,5))
            
            
            
    #Adding all the agents to schedule         
    def step(self):
        self.schedule.step()
