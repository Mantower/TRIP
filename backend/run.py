from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_autodoc import Autodoc
from nlpComponent import PyNLP
from flickrComponent import PyFlickr
from finnairComponent import FinnAir
from random_city import RandomCity
import json
import math

app = Flask(__name__)
auto = Autodoc(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)

@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('static/images', path)

@app.route('/fonts/<path:path>')
def send_fonts(path):
    return send_from_directory('static/fonts', path)

@app.route("/doc")
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

@app.route("/v1/random", methods=["GET"])
@auto.doc()
def get_lucky():
    tags = RandomCity().get_cities()
    pyFlickr = PyFlickr()
    data = pyFlickr.get_random(tags)
    finalized = []
    print(data)
    for sub_im in data:
        finalized.append(sub_im["photos"]["photo"][0])
    print(finalized)
    return jsonify(finalized)
