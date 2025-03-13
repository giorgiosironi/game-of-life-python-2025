from flask import Flask, render_template, request
from view_model import construct_view_model
from world import evolve
from alive_cell import AliveCell

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def hello():
    return render_template('index.html')

world_state_containing_a_blinker = [
    AliveCell(2, 3),
    AliveCell(3, 3),
    AliveCell(4, 3),
]

@app.route('/examples/blinker')
def blinker_example():
    generation = request.args.get('generation', '1')
    width, height = 8, 6
    world_state = world_state_containing_a_blinker
    if generation == 2:
        world_state = evolve(world_state)
    displayed_cells = construct_view_model(world_state, max_x=width-1, max_y=height-1)
    return render_template('generation.html', displayed_cells=displayed_cells, title="Blinker Example")
