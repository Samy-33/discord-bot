import requests as rq
from services.abstract_api import BaseAPIClass
from constants.bot_constants import NEWS_API_KEY
from utils.helpers import empty_string_if_none as esin


class NewsAPI(BaseAPIClass):

    def _get_data(self, vars: dict):

        vars.update({
            'apiKey': self._api_key
        })

        rq_obj = rq.get(self._endpoint, params=vars)
        return rq_obj

    def _parse_returned_data(self, data):
        data = data.json()

        to_send = ''
        if len(data['articles']) > 3:
            articles = data['articles'][:3]
        else:
            articles = data['articles']
        if data['status'] == 'ok':
            for article in articles:
                to_send += '**Source**: ' + esin(article['source']['name']) + '\n'
                to_send += '**Author**: ' + esin(article['author']) + '\n'
                to_send += '**Published At**: ' + esin(article['publishedAt']) + '\n'
                to_send += '**Link**: ' + esin(article['url']) + '\n'
                to_send += '**Description**: ' + esin(article['description']) + '\n\n'
                to_send += '---------------------------------------\n\n'

        else:
            to_send = 'Some Error Occured while parsing the news data.'
        return to_send


options = {
    'about': 'q'
}

news = NewsAPI('https://newsapi.org/v2/everything',
                api_key=NEWS_API_KEY,
                map_message_to_query=options)