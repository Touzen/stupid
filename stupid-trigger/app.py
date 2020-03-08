from flask import Flask
from .control import triggerFan as trigger_fan

app = Flask(__name__)


@app.route('/')
def hello_world():
    trigger_fan()
    return 'Triggggeerrredddddd :OO'


if __name__ == '__main__':
    app.run()
