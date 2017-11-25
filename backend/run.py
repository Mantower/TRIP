from flask import Flask
from flask import request
from flask import jsonify
from flask_autodoc import Autodoc
from nlpComponent import PyNLP
import json

app = Flask(__name__)
auto = Autodoc(app)

FLICKR_KEY = '779602574bed525a7747ab7ebf957fec'
FLICKR_SECRET = 'b80ac52abe87ed2d'

@app.route("/")
def doc():
    return auto.html(
        title='API Documentation for FinnAir TRIP backend'
    )

@app.route("/v1/search", methods=["GET"])
@auto.doc()
def search():
    text = request.args.get('term', '')
    pyNLP = PyNLP('9000')
    print(text)
    output = pyNLP.eval_input(text)
    print(output)
    #json_return = json.loads(photos)
    #json_lists = json_return["photos"]["photo"]

    return jsonify(output[0])

@app.errorhandler(404)
def not_found(error):
    return "Not found", 404
