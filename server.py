import mesa
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
from model import CarehomeModel
from mesa.visualization.modules import CanvasGrid
from agent import ResidentAgent

NUMBER_OF_CELLS = 100

SIZE_OF_CANVAS_IN_PIXELS_X = 500
SIZE_OF_CANVAS_IN_PIXELS_Y = 700

simulation_params = {
    'number_of_agents' : UserSettableParameter(
        'slider',
        'Number of Agents',
        50, #default
        10, #min
        200, #max
        1, #step
        description="choose how many games to include in the simulation",
    ),
    'width': NUMBER_OF_CELLS,
    'height': NUMBER_OF_CELLS,
}
def third_test_portrayal(agent):
    if agent is None:
        return
    portrayal = {}

    # define the portrayal features such as layers, shapes, colours etc.
    # can make this dependent on agent values, such as energy variable etc.
    if type(agent) is ResidentAgent:
        portrayal = {"Shape": "circle",
                     "scale": 1,
                     "Color": "red",
                     "Filled": "true",
                     "Layer": 1,
                     "r": 0.5,
                     "text": "ᕕ( ՞ ᗜ ՞ )ᕗ",
                     "text_color": "black",
                     "scale": 1
                     } 
    return portrayal

grid = CanvasGrid(agent_portrayal, NUMBER_OF_CELLS, NUMBER_OF_CELLS, SIZE_OF_CANVAS_IN_PIXELS_X,SIZE_OF_CANVAS_IN_PIXELS_Y)
server = ModularServer(CarehomeModel, 
                        [grid], 
                        "Money Model", 
                        simulation_params)
server.port = 8521 # The default
server.launch()