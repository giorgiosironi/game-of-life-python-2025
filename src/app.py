from flask import Flask, render_template

# question these two generated values. They appear to work empirically within `make dev`
app = Flask(__name__, template_folder='../templates')

@app.route('/')
def hello():
    return render_template('index.html')

def blinker_view_model():
    width, height = 8, 6
    rows = []
    for y in range(height):
        row = []
        for x in range(width):
            cell = y == 3 and 2 <= x <= 4
            row.append(cell)
        rows.append(row)
    return rows

@app.route('/examples/blinker')
def blinker_example():
    displayed_cells = blinker_view_model()
    return render_template('generation.html', displayed_cells=displayed_cells, title="Blinker Example")
