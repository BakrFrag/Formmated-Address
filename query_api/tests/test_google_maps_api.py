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