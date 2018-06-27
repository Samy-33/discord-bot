from abc import ABC


class BaseService(ABC):

    def __init__(self, map_message_to_query):
        self._map_message_to_query = map_message_to_query
        super().__init__()

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