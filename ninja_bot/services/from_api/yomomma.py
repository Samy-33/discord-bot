import requests as rq
from services.abstract_api import BaseAPIClass


class YoMomma(BaseAPIClass):

    def _get_data(self, vars: dict):
        rq_obj = rq.get(self._endpoint, params=vars)
        return rq_obj

    def _parse_returned_data(self, data):
        return data.json()['joke']


yomomma = YoMomma('http://api.yomomma.info')