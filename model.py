from mesa import Model
from agent import ResidentAgent
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
        u = []
       
        for t in range(self.num_residents):
            heading = (1, 0)
            #apend element in vector 
            k = ResidentAgent(t,self)
            self.schedule.add(k)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            u.append(x) 
            
            self.grid.place_agent(k, (x,60))
            
        
        
        for r,s in enumerate(range(self.num_residents+1, self.num_robots+self.num_residents+1)):
        #for r,s in enumerate(self.num_robots):
            heading = (1, 0)
            l = RobotAgent(s,self)
            self.schedule.add(l)
            # Add the agent to a random grid cell
            #v = (u[r])
            v = (u[r])
           # for a,b in enumerate (v):
            #v = self.random.randrange(u[r])
            self.grid.place_agent(l, (v,55))
            #move_agent(self, l, (x,y))
            
            
            # Add the agent to a random grid cell
            # Robot needs to be placed next/close to the resident (res_id):
                   # find out the location of my resident in the grid (x,y) of the resident, whose id == res_id
                   # substract 1 to the y value of the resident and that will be y of the robot
                   # x of robot = x of resident and y of robot = y of resident - 1
            #x = self.random.randrange(self.grid.width)
            #y = self.random.randrange(self.grid.height)
        #def _place_agent(self, ResidentAgent, pos):
            """Place the agent at the correct location."""
         #   x, y = pos
        #if ResidentAgent not in self.grid[x][y]:
         #   self.grid[x][y].append(RobotAgent)
            #self.empties.discard(pos)
            #Todo: check that the agent does not occupy the cell that is occupied by another agent
          #  self.grid.place_agent(f, (x,y))
            
             
    def step(self):
        self.schedule.step()
