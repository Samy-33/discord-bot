from abc import abstractmethod
from bs4 import BeautifulSoup as bs
import requests as rq


class BaseScraper(BaseService):
    def __init__(self, endpoint: str, params: list,
                 method: str,
                 map_message_to_query={}):
        self._endpoint = endpoint
        self._params = params
        self._method = method
        super().__init__(map_message_to_query=map_message_to_query)

    def _get_soup(self, params: dict):
        
        rq_obj = None
        if method == 'POST':
            rq_obj = rq.post(self._endpoint, params)
        elif method == 'GET':
            rq_obj = rq.get(self._endpoint, params)

        soup = bs(rq_obj.text, 'html.parser')

        return soup

    @abstractmethod
    def _extract_data(self, soup):
        pass

    @abstractmethod
    def _parse_returned_data(self, data):
        pass

    def respond(self, vars: list):
        vars_dict = self._parse_query_data(vars)

        if not vars_dict:
            return 'Invalid Syntax. Type `!!help` for more info.'

        for key in vars_dict.keys():
           if key not in self._map_message_to_query.values():
                return 'Invalid Query data. Type `!!help` for more info.'

        soup = self._get_soup(vars_dict)
        data = self._extract_data(soup)
        return self._parse_returned_data


