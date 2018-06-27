from abc import ABC, abstractmethod
from services.base_service import BaseService
 

class BaseAPIClass(BaseService):
    def __init__(self, endpoint: str,
                 api_key = '',
                 map_message_to_query={}):
        self._endpoint = endpoint
        self._variables = vars
        self._api_key = api_key
        # self._map_message_to_query = map_message_to_query
        super().__init__(map_message_to_query=map_message_to_query)

    @abstractmethod
    def _get_data(self, vars: dict):
        pass

    @abstractmethod
    def _parse_returned_data(self, data):
        pass

    def respond(self, vars: list):

        vars_dict = self._parse_query_data(vars)

        if vars_dict is None:
            return 'Invalid Syntax. Type `!!help` for more info.'

        for key in vars_dict.keys():
           if key not in self._map_message_to_query.values():
                return 'Invalid Query data. Type `!!help` for more info.'

        data = self._get_data(vars_dict)

        if not data:
            return 'Bad Request. Why are you doing this? I am just helping. :('

        return self._parse_returned_data(data)