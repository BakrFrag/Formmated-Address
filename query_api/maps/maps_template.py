from abc import ABC, abstractmethod
class QueryMapsApi(ABC):
    """
    generic / abstract class to query maps api services
    """

    def set_search_query(self, query):
        """
        handle query to search 
        """
        if query is None or query == "":

            return "search query can't be empty"
        else:
            self.search_query = query

    @abstractmethod
    def send_query_request(self, query):
        """
        send request to maps api , fetch info
        """
        pass

    @abstractmethod
    def handle_results(self, search_results):
        """
        handle maps api search response
        """
        pass

    @abstractmethod
    def extract_address(self, results):
        """
        extract addresses from maps pai response 
        """
        pass