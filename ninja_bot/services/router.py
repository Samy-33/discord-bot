from services.from_api.yomomma import yomomma

class Router:
    def __init__(self):
        self._routes = self._initialize_routes()

    def _initialize_routes(self):
        routes = {
            'yomomma': {
                'call': yomomma.get_data_as_dict,
            }
        }
        return routes

    def get_yomomma(self):
        return self._routes['yomomma']['call']


router = Router()