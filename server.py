import mesa
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
from model import CareHomeModel
from mesa.visualization.modules import CanvasGrid

NUMBER_OF_CELLS = 100

SIZE_OF_CANVAS_IN_PIXELS_X = 500
SIZE_OF_CANVAS_IN_PIXELS_Y = 700

simulation_params = {
    'n_residents' : UserSettableParameter(
        'slider',
        'number of residents',
        4, #default
        10, #min
        50, #max
        1, #step
        description="choose how many games to include in the simulation",
    ),
    'n_robots' : UserSettableParameter(
        'slider',
        'Number of Robots',
        4, #default
        10, #min
        50, #max
        1, #step
        description="choose how many games to include in the simulation",
    ),
    'width': NUMBER_OF_CELLS,
    'height': NUMBER_OF_CELLS,
}

def agent_portrayal(agent):
    portrayal = {
        "Shape": "arrowHead",
        "Filled": "true",
        "Layer": 0.2,
        "Color": "blue",
        "r":10 ,
    }
    if isinstance(agent, ResidentAgent):
        portrayal['Color'] = 'blue'
        portrayal['Layer'] = 0
    else:
        portrayal['Color'] = 'red'
        portrayal['Layer'] = 1
        portrayal['r'] = 0.2  
    return portrayal

grid = CanvasGrid(agent_portrayal, NUMBER_OF_CELLS, NUMBER_OF_CELLS, SIZE_OF_CANVAS_IN_PIXELS_X,SIZE_OF_CANVAS_IN_PIXELS_Y)
server = ModularServer(CareHomeModel, 
                        [grid], 
                        "CareHomeModel", 
                        simulation_params)
server.port = 8521 # The default
server.launch()