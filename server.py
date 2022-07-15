import mesa
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
from model import CareHomeModel
from agent import ResidentAgent
from mesa.visualization.modules import CanvasGrid

NUMBER_OF_CELLS = 64

SIZE_OF_CANVAS_IN_PIXELS_X = 100
SIZE_OF_CANVAS_IN_PIXELS_Y = 200

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
    'width': NUMBER_OF_CELLS,
    'height': NUMBER_OF_CELLS,
}

def agent_portrayal(agent):
    print(f"Uid: {agent.unique_id}")
    portrayal = {
            "Shape": "arrowHead",
            "Filled": "true",
            "Layer": 2,
            "Color": ["#00FF00", "#99FF99"],
            "stroke_color": "#666666",
            "Filled": "true",
            "text": agent.unique_id,
            "text_color": "white",
            "scale": 0.8,
        }
    # portrayal = {
    #     "Shape": "cicrle",
    #     "Filled": "true",
    #     "Layer": 0,
    #     "Color": "blue",
    #     "r":50 ,
    # }
    # if isinstance(agent, ResidentAgent):
    #     portrayal['Color'] = 'blue'
    #     portrayal['Layer'] = 0
    # else:
    #     portrayal['Color'] = 'red'
    #     portrayal['Layer'] = 1
    #     portrayal['r'] = 0.2  
    print(portrayal)
    return portrayal

grid = CanvasGrid(agent_portrayal, NUMBER_OF_CELLS, NUMBER_OF_CELLS, SIZE_OF_CANVAS_IN_PIXELS_X,SIZE_OF_CANVAS_IN_PIXELS_Y)

server = ModularServer(CareHomeModel, 
                        [grid], 
                        "CareHomeModel", 
                        simulation_params)
server.port = 8521 # The default
server.launch()