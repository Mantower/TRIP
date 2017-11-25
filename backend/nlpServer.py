from pycorenlp import StanfordCoreNLP
import flickrapi
import json

nlp = StanfordCoreNLP('http://localhost:9000')


text = 'ice fishing'
properties={
  'annotators': 'tokenize,ssplit,pos,depparse,parse,ner,openie',
  'outputFormat': 'json'
}

output = nlp.annotate(text, properties)

print(output['sentences'][0]['openie'])

with open('output.txt', 'w') as f:
    f.write(str(output))


flickr_key = u'779602574bed525a7747ab7ebf957fec'
flickr_secret = u'b80ac52abe87ed2d'

nlp_tag = 'ice fishing'

flickr = flickrapi.FlickrAPI(flickr_key, flickr_secret, format='parsed-json')
photos = flickr.photos.search(tags=nlp_tag, per_page='10', format='json', has_geo='1')

print(photos)
json_return = json.loads(photos)
json_lists = json_return["photos"]["photo"]

print(json_return[0]["u'id'"])

#for key, value in dict.items(json_return["photos"]["photo"]):
#    print key, value
