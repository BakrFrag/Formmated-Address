from query_api.maps.query_google_maps import QueryGoogleMaps
import sys


class ArgumentParser(object):
    def __init__(self, parsed_args):
        self.args = parsed_args
        self.number_of_args = len(self.args)
        self.helper_text = """
        -h for displaying helper text 
        -t for parse address to search in quote
        example -t structured_address.py “5 Av. Anatole, Paris, Champ de Mars"
        """
        self.invalid_arguments_flags = {
            "helper_message": self.helper_text, "status": "INVALID_ARGUMENTS_FLAGS"}

    def validate_arguments(self):
        """
        validate parsed arguments number , values & flags 
        """
        if self.number_of_args > 3 or self.number_of_args < 2:
            self.invalid_arguments_flags.update(
                {"error_message": "invalid number of arguments"})

        elif self.number_of_args == 2:
            if self.args[1] == "-h":
                return {"status": "OK", "helper_message": self.helper_text}
            elif self.args[1] == "-t":
                self.invalid_arguments_flags.update(
                    {"error_message": "text address not parsed"})

            else:

                self.invalid_arguments_flags.update(
                    {"error_message": "invalid flags"})

        elif self.number_of_args == 3:
            if self.args[1] != "-t" or self.args[2] == "":

                self.invalid_arguments_flags.update(
                    {"error_message": "invalid arguments flags or values"})

            else:
                return {"status": "OK"}
        return self.invalid_arguments_flags

    def parse_arguments(self, argument):

        google_maps = QueryGoogleMaps()
        google_maps.set_search_query(argument)
        return google_maps.send_query_request()


if __name__ == "__main__":
    """
    arguments handler from CLI
    """
    args = sys.argv
    parser_arguments = ArgumentParser(args)
    parse_arguments_results = parser_arguments.validate_arguments()
    if parse_arguments_results.get("status") == "OK":
        if args[1] == "-h":
            print(parse_arguments_results.get("helper_message"))
        else:
            results = parser_arguments.parse_arguments(args[2])
            if type(results) == str:
                print(results)
            elif type(results) == dict:
                print(results.get("status"))
                print(results.get("error_message"))
            else:
                print(*results, sep="\n")
    else:
        print(parse_arguments_results.get("error_message"))
        print(parse_arguments_results.get("helper_message"))