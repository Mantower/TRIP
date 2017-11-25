import requests

class FinnAir:
    host = ''
    departure_code = ''
    adults = 1

    def __init__(self):
        global host
        host = 'https://offer-junction.ecom.finnair.com'
        global departure_code
        departure_code = 'HEL'
        global adults
        adults = 1

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
