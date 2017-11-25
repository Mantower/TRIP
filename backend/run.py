from flask import Flask
from flask import request
from flask import jsonify
from flask_autodoc import Autodoc
from nlpComponent import PyNLP
from flickrComponent import PyFlickr
from finnairComponent import FinnAir
from random_city import RandomCity
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
def search_photos():
    text = request.args.get('term', '')
    pyNLP = PyNLP('9000')
    print(text)
    output = pyNLP.eval_input(text)
    print(output)
    #json_return = json.loads(photos)
    #json_lists = json_return["photos"]["photo"]

    return jsonify(output[0]["photos"]["photo"])

@app.route("/v1/flights", methods=["GET"])
@auto.doc()
def search_flights():
    destination_code = request.args.get('destination_code', '')
    departure_date = request.args.get('departure_date', '')
    finnAir = FinnAir()
    flights = finnAir.search_flights(destination_code, departure_date)
    return jsonify(flights)

@app.errorhandler(404)
def not_found(error):
    return "Not found", 404

@app.route("/v1/random", methods=["GET"])
@auto.doc()
def get_lucky():
    tags = RandomCity().get_cities()
    pyFlickr = PyFlickr()
    data = pyFlickr.get_random(tags)
    finalized = []
    for sub_im in data:
        finalized.append(sub_im["photos"]["photo"][0])
    print(finalized)
    return jsonify(finalized)
