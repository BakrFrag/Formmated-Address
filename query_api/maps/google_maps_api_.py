import requests
from decouple import config
from .maps_template import QueryMapsApi


class QueryGoogleMaps(QueryMapsApi):
    def __init__(self):
        """
        init instance variables url , key , search_query
        """
        self.url = config("GOOGLE_MAPS_URL")
        self.key = config("KEY")
        self.search_query = ""

    def send_query_request(self):
        """
        send request with search query to maps api 
        """
        params = {
            "key": self.key,
            "address": self.search_query
        }
        try:
            search_results = requests.get(self.url, params=params)

        except Exception as E:
            
            return "error query google maps - check internet connection or may be network connection error"
        else:
            return self.handle_results(search_results.json())

    def handle_results(self, search_results):
        """
        handle google maps api response 
        """

        if search_results.get("status") == "OK":

            return self.extract_address(search_results['results'])
        return {
            "status": search_results.get("status"),
            "error_message": search_results.get("error_message")
        }

    def extract_address(self, results):
        """
        extract address/es from google maps api response 
        """
        number_of_address: int = len(results)
        if number_of_address == 1:
            address_components = results[0]['address_components']
            street_number = ""
            route = ""
            postal_code = ""
            city = ""
            country = ""
            address = f""
            for i in address_components:
                types = i.get("types")
                if i.get("types") == ["street_number"]:
                    street_number = i.get("long_name")
                elif i.get("types") == ["route"]:
                    route = i.get("short_name")
                elif i.get("types") == ["postal_code"]:
                    postal_code = i.get("long_name")
                elif i.get("types") == ["locality", "political"]:
                    city = i.get("long_name")
                elif i.get("types") == ["country", "political"]:
                    country = i.get("long_name")
            address = f"{street_number} {route},{postal_code},{city},{country}"
            return address
        else:
            list_of_address: list[str] = []
            for i in range(number_of_address):
                address_components = results[i]['address_components']
                street_number = ""
                route = ""
                postal_code = ""
                city = ""
                country = ""
                address = f""
                for i in address_components:
                    types = i.get("types")
                    if i.get("types") == ["street_number"]:
                        street_number = i.get("long_name")
                    elif i.get("types") == ["route"]:
                        route = i.get("short_name")
                    elif i.get("types") == ["postal_code"]:
                        postal_code = i.get("long_name")
                    elif i.get("types") == ["locality", "political"]:
                        city = i.get("long_name")
                    elif i.get("types") == ["country", "political"]:
                        country = i.get("long_name")
                address = f"{street_number} {route},{postal_code},{city},{country}"
                list_of_address.append(address)
            return list_of_address