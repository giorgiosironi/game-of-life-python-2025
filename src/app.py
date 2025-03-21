from flask import Flask, render_template, request, url_for
from view_model import construct_world_window
from evolution import evolve
from world import AliveCell, WorldState

app = Flask(__name__, template_folder='../templates')


@app.route('/')
def hello() -> str:
    return render_template('index.html')


world_state_containing_a_blinker = [
    AliveCell(2, 3),
    AliveCell(3, 3),
    AliveCell(4, 3),
]


def evolve_to_generation(world_state: WorldState, generation: int) -> WorldState:
    for _ in range(2, generation + 1):
        world_state = evolve(world_state)
    return world_state


@app.route('/examples/blinker')
def blinker_example() -> str:
    generation = int(request.args.get('generation', '1'))
    width = int(request.args.get('width', '8'))
    height = int(request.args.get('height', '6'))
    world_state = evolve_to_generation(
        world_state_containing_a_blinker, generation)

    world_window = construct_world_window(
        world_state, max_x=width-1, max_y=height-1)
    next_state_path = url_for(
        'blinker_example', generation=generation + 1, width=width, height=height)

    return render_template(
        'generation.html',
        world_window=world_window,
        title="Blinker Example",
        next_state_path=next_state_path,
    )
