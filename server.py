import mesa
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
from traitlets import Integer
from model import CareHomeModel
from agent import ResidentAgent
from agent import RobotAgent
from agent import NurseAgent
from mesa.visualization.modules import CanvasGrid

NUMBER_OF_CELLS = 64

SIZE_OF_CANVAS_IN_PIXELS_X = 400
SIZE_OF_CANVAS_IN_PIXELS_Y = 600

simulation_params = {
    'n_residents' : UserSettableParameter(
        'slider',
        'number of residents',
        2, #default
        2, #min
        10, #max
        1, #step
        description="choose how many games to include in the simulation",
    ),
    'n_robots' : UserSettableParameter(
        'slider',
        'Number of Robots',
        2, #default
        2, #min
        10, #max
        1, #step
        description="choose how many games to include in the simulation",
    ),
    'n_nurses' : UserSettableParameter(
        'slider',
        'Number of Nurses',
        2, #default
        3, #min
        10, #max
        1, #step
        description="choose how many games to include in the simulation",
    ),
    'width': NUMBER_OF_CELLS,
    'height': NUMBER_OF_CELLS,
}

def agent_portrayal(agent):
    print(f"Uid: {agent.unique_id}")
    portrayal = {
            "Filled": "true",
            "Layer": 1,
            "Color": "red",
            "heading_x": -1,
            "heading_y": 0,
        }
    if isinstance(agent, ResidentAgent):
        print("Is resident!!!")
        portrayal['Color'] = 'red'
        portrayal['Layer'] = 0
        portrayal['Shape'] = 'circle'
        portrayal['r'] = 6
        
    elif isinstance(agent, RobotAgent):
        print("Is robot!!! {agent.heading}")
        portrayal['Color'] = 'blue'
        portrayal['Layer'] = 1
        portrayal['Shape'] = 'rect'
        portrayal['w'] = 6
        portrayal['h'] = 4
    
    #elif isinstance(agent, NurseAgent):
#    else:
 #       print("Is nurse!!!")
  #      portrayal['Color'] = 'red'
   #     portrayal['Layer'] = 0
    #    portrayal['Shape'] = 'circle'
     #   portrayal['r'] = 2
    else:
         print("Is nurse!!! {agent.heading}")
         portrayal['Color'] = 'black'
         portrayal['Layer'] = 2
         portrayal['Shape'] = 'arrowHead'
         portrayal['scale'] = 6
         
    print(portrayal)
    return portrayal

grid = CanvasGrid(agent_portrayal, NUMBER_OF_CELLS, NUMBER_OF_CELLS, SIZE_OF_CANVAS_IN_PIXELS_X,SIZE_OF_CANVAS_IN_PIXELS_Y)

server = ModularServer(CareHomeModel, 
                        [grid], 
                        "CareHomeModel", 
                        simulation_params)
server.port = 8521 # The default
server.launch()