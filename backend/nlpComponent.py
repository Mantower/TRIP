from pycorenlp import StanfordCoreNLP
from flickrComponent import PyFlickr
class PyNLP:

    nlp = ''
    properties = ''
    flickr = ''

    def __init__(self, port):
        address = 'http://localhost:'
        address += port
        global nlp
        nlp = StanfordCoreNLP(address)
        global properties
        properties ={
          'annotators': 'tokenize,ssplit,pos,depparse,parse,ner,openie',
          'outputFormat': 'json'
        }
        format_flickr = 'parsed-json'
        global flickr

        flickr = PyFlickr()

    def eval_input(self, input_string):
        split_text = input_string.split()
        tag_list = []
        if len(split_text) < 3:
            output_list = split_text
            print(output_list)
            tag_list.append(output_list)
        else:
            output = nlp.annotate(input_string, properties)
            output_list = output['sentences'][0].get(u'openie')[0]
            nlp_object = output_list.get(u'object')
            nlp_subject = output_list.get(u'subject')
            print(nlp_object)
            print(nlp_subject)
            if nlp_object != None:
                tag_list.append(nlp_object)
            if nlp_subject != None:
                tag_list.append(nlp_subject)

        results = flickr.get_image_data(tag_list)

        return results
