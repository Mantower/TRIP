import flickrapi
import json

class PyFlickr:

    settings = ''
    key = ''
    secret = ''
    flickr = ''

    def __init__(self):
        global key
        key = u'779602574bed525a7747ab7ebf957fec'
        global secret
        secret = u'b80ac52abe87ed2d'
        global flickr
        flickr = flickrapi.FlickrAPI(key, secret, format='parsed-json')


    def get_image_data(self, tags):
        photos_list = []
        for seperate_tag in tags:
            photos = flickr.photos.search(tags=seperate_tag, per_page='10', format='json', has_geo='1', extras="url_c,geo")
            json_return = json.loads(photos)
            photos_list.append(json_return)

        return photos_list

    def get_random(self, all_tags):
        photos_list = []
        for tag in all_tags:
            photos = flickr.photos.search(tags=tag, per_page='2', format='json', has_geo='1', extras="url_c,geo")
            json_return = json.loads(photos)
            photos_list.append(json_return)

        print(photos_list)
        return photos_list
