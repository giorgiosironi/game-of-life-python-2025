from flask import Flask, render_template

# question these two generated values. They appear to work empirically within `make dev`
app = Flask(__name__, template_folder='../templates')

@app.route('/')
def hello():
    return render_template('index.html')
