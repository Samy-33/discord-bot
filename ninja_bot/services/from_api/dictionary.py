import requests as rq
import os
from services.abstract_api import BaseAPIClass
from utils.helpers import empty_string_if_none as esin
from utils.helpers import remove_html_from_string as rhfs


class Dictionary(BaseAPIClass):
    
    def _get_data(self, vars: dict):

        full_url = os.path.join(self._endpoint, vars['word'])
        rq_obj = rq.get(full_url)

        if rq_obj.status_code != 200:
            return None

        return rq_obj

    def _parse_returned_data(self, data):
        data = data.json()['data']

        if not data:
            return 'Meaning Not Found. -_-'

        data_list = data['content'][:3]
        to_send = '**' + esin(data['displayForm']) + ':**\n'

        four_spaces = ' ' * 4
        index = 1
        for data_element in data_list:
            to_add = '{}**{}**:\n'.format(four_spaces, index)
            entry = data_element['entries'][0]

            if 'posBlocks' not in entry.keys():
                continue

            pos_block = entry['posBlocks'][0]
            definitions = pos_block.get('definitions') 
            if not definitions:
                continue
            definition = rhfs(definitions[0]['definition'])
            to_add += '{}**Def: ** *{}*\n\n'.format(four_spaces*2, definition)

            to_send += to_add
            index += 1

        return to_send
            

options = {
    'word': 'word'
}

dictionary = Dictionary('https://api-portal.dictionary.com/dcom/pageData',
                        map_message_to_query=options)