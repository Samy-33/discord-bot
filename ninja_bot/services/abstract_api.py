from abc import ABC, abstractmethod


class BaseAPIClass(ABC):
    def __init__(self, endpoint: str,
                 api_key = '',
                 map_message_to_query={}):
        self._endpoint = endpoint
        self._variables = vars
        self._api_key = api_key
        self._map_message_to_query = map_message_to_query
        super().__init__()

    @abstractmethod
    def _get_data(self, vars: dict):
        pass

    @abstractmethod
    def _parse_returned_data(self, data):
        pass

    def _parse_query_data(self, args: list):

        query = {}
        for argument in args:
            if not isinstance(argument, str):
                return None
            splitted = argument.split(':')
            if len(splitted) != 2:
                return None
            if splitted[0] not in self._map_message_to_query.keys():
                return None
            
            key = self._map_message_to_query[splitted[0]]
            value = splitted[1]

            query[key] = value

        return query

    def respond(self, vars: list):

        vars_dict = self._parse_query_data(vars)

        if not vars_dict:
            return 'Invalid Syntax. Type `!!help` for more info.'

        for key in vars_dict.keys():
           if key not in self._map_message_to_query.values():
                return 'Invalid Query data. Type `!!help` for more info.'

        data = self._get_data(vars_dict)
        return self._parse_returned_data(data)