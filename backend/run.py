from flask import Flask
from flask import request
from flask import jsonify
from flask_autodoc import Autodoc
from nlpComponent import PyNLP
from finnairComponent import FinnAir
import json
import math

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

@app.route("/v1/destination", methods=["GET"])
@auto.doc()
def search_for_nearest_airport():
    longitude = float(request.args.get('longitude', ''))
    latitude = float(request.args.get('latitude', ''))
    finnAir = FinnAir()
    airports = finnAir.search_for_nearest_airport(latitude, longitude)
    for airport in airports:
        print(airport)
        airport["extras"] = {
            "longitude": longitude,
            "latitude": latitude,
            "distance": math.hypot(airport["longitude"] - longitude, airport["latitude"] - latitude) * 1000 * 111,
            "unit": "cm"
        }
    return jsonify(airports)

@app.errorhandler(404)
def not_found(error):
    return "Not found", 404
