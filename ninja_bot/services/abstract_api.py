from abc import ABC, abstractmethod


class BaseAPIClass(ABC):
    def __init__(self, endpoint: str, vars = []):
        self._endpoint = endpoint
        self._variables = vars
        super().__init__()

    @abstractmethod
    def _get_data(self, vars: dict):
        pass

    @abstractmethod
    def _parse_returned_data(self, data):
        pass

    def get_data_as_dict(self, vars: dict):
        for key in vars.keys():
           if key not in self._variables:
                return {'error': 'Invalid Query data'}

        data = self._get_data(vars)
        return self._parse_returned_data(data)