from services.from_api.yomomma import yomomma
from services.from_api.news import news
from services.sendhelp import sendhelp

class Router:
    def __init__(self):
        self._routes = self._initialize_routes()

    def _initialize_routes(self):
        routes = {
            'yomomma': {
                'call': yomomma.respond
            },
            'news': {
                'call': news.respond
            },
            'help': {
                'call': sendhelp.respond
            }
        }
        return routes

    def get_yomomma(self):
        return self._routes['yomomma']['call']

    def get_news(self):
        return self._routes['news']['call']

    def get_help(self):
        return self._routes['help']['call']

router = Router()