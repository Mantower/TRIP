import requests
import csv
from rtree import index

class FinnAir:
    host = ''
    departure_code = ''
    adults = 1
    airports = None

    def __init__(self):
        global host
        host = 'https://offer-junction.ecom.finnair.com'
        global departure_code
        departure_code = 'HEL'
        global adults
        adults = 1

        # build R-tree
        global airports
        airports = index.Rtree()

        # import csv
        with open('../model/finnair_airport_geo.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if reader.line_num == 1:
                    continue
                airports.insert(reader.line_num, (float(row[6]), float(row[5])), row)

    def search_flights(self, destination_code, departure_date):
        url = host + "/api/offerList"
        payload = {
            "adults": adults,
            "departureLocationCode": departure_code,
            "destinationLocationCode": destination_code,
            "departureDate": departure_date
        }
        response = requests.get(url, params=payload)
        print(response.url)
        return response.json()

    def search_for_nearest_airport(self, latitude, longitude):
        return list(airports.nearest((longitude, latitude), 1, objects="raw"))
