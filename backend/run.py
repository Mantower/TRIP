from flask import Flask
from flask import request
from flask import jsonify
from flask_autodoc import Autodoc
from pycorenlp import StanfordCoreNLP
import flickrapi
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
    nlp = StanfordCoreNLP('http://localhost:9000')
    text = request.args.get('term', '')
    properties={
      'annotators': 'tokenize,ssplit,pos,depparse,parse,ner,openie',
      'outputFormat': 'json'
    }
    output = nlp.annotate(text, properties)

    print(output['sentences'][0]['openie'])

    with open('output.txt', 'w') as f:
        f.write(str(output))

    nlp_tag = text

    flickr = flickrapi.FlickrAPI(FLICKR_KEY, FLICKR_SECRET, format='parsed-json')
    photos = flickr.photos.search(tags=nlp_tag, per_page='10', format='json', has_geo='1', extras="url_c,geo")

    print(photos)
    json_return = json.loads(photos)
    json_lists = json_return["photos"]["photo"]

    return jsonify(json_lists)

@app.errorhandler(404)
def not_found(error):
    return "Not found", 404
