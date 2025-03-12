from flask import Flask, render_template
from view_model import AliveCell, construct_view_model

# question these two generated values. They appear to work empirically within `make dev`
app = Flask(__name__, template_folder='../templates')

@app.route('/')
def hello():
    return render_template('index.html')

def blinker_view_model():
    width, height = 8, 6
    alive_cells = [
        AliveCell(2, 3),
        AliveCell(3, 3),
        AliveCell(4, 3),
    ]
    return construct_view_model(alive_cells, max_x=width-1, max_y=height-1)

@app.route('/examples/blinker')
def blinker_example():
    displayed_cells = blinker_view_model()
    return render_template('generation.html', displayed_cells=displayed_cells, title="Blinker Example")
