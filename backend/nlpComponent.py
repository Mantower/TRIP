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
            print(properties)
            output = nlp.annotate(input_string, properties)
            print(output)
            output_list = output['sentences'][0].get(u'openie')
            print(output_list)
            nlp_object = ''
            nlp_subject = ''
            if not output_list:
                parse_items = output['sentences'][0].get(u'enhancedPlusPlusDependencies')
                iter_nlp = iter(parse_items)
                next(iter_nlp)
                for item in iter_nlp:
                    if item.get(u'dep') == u'amod':
                        nlp_object += item.get(u'governorGloss') + ' '
                        nlp_object += item.get(u'dependentGloss')
            else:
                nlp_object = output_list[0].get(u'object')
                nlp_subject = output_list[0].get(u'subject')
            print(nlp_object)
            print(nlp_subject)

            tag_list = nlp_object + ' ' + nlp_subject
        print(tag_list)
        results = flickr.get_image_data(tag_list)

        return results
