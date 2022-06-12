from decouple import config 
from maps.google_maps_api import QueryGoogleMaps
import unittest

class TestQueryGoogleMaps(unittest.TestCase):
    def setUp(self):
        """
        init nessary variables for all tests 
        """
        self.key = config("KEY")
        self.url = config("GOOGLE_MAPS_URL")
        self.wrong_key = self.key[0:10]

    def test_set_query_search(self):
        """
        test set search query to empty string
        """
        google_maps = QueryGoogleMaps()
        result = google_maps.set_search_query("")
        self.assertEqual(result, "search query can't be empty")

    def test_send_query_request(self):
        """
        test with wrong key
        """
        google_maps = QueryGoogleMaps()
        google_maps.key = self.wrong_key
        google_maps.set_search_query("5 Av. Anatole, Paris, Champ de Mars")

        response = google_maps.send_query_request()
        self.assertEqual(response.get("status"), "REQUEST_DENIED")
        self.assertEqual(response.get("error_message"),
                         "The provided API key is invalid. ")
        self.assertFalse(response.get("results"))

        """
        test with empty address 
        """
        google_maps.key = self.key
        google_maps.search_query = ""
        response = google_maps.send_query_request()
        self.assertEqual(response.get("status"), "INVALID_REQUEST")
        self.assertEqual(response.get("error_message"),
                         "Invalid request. Missing the 'address', 'components', 'latlng' or 'place_id' parameter.")
        self.assertFalse(response.get("results"))

    def test_extract_address(self):
        google_maps = QueryGoogleMaps()
        google_maps.key = self.key

        google_maps.set_search_query("5 Av. Anatole, Paris, Champ de Mars")
        results = google_maps.send_query_request()

        self.assertEqual(results, ["2 All. Adrienne Lecouvreur,75007,Paris,France",
                                   "5 Av. Anatole France,75007,Paris,France"])

        google_maps.set_search_query("St Anthony's Hospital")
        results = google_maps.send_query_request()

        self.assertEqual(
            results, "1200 7th Ave N,33705,St. Petersburg,United States")

        google_maps.set_search_query("Croydon united kingdom")
        results = google_maps.send_query_request()

        self.assertEqual(results, " ,,Croydon,United Kingdom")

        google_maps.set_search_query("Rembrandt House Museum")
        results = google_maps.send_query_request()
       
        self.assertEqual(
            results, "4 Jodenbreestraat,1011 NK,Amsterdam,Netherlands")

        google_maps.set_search_query("Royal Marsden Hospital - Sutton")
        results = google_maps.send_query_request()
       
        self.assertEqual(results, " Downs Rd,SM2 5PT,,United Kingdom")