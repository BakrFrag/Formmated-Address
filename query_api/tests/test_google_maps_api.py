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

    