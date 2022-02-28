from flask import make_response
from flask.views import MethodView

class FlasktemplateView(MethodView):
    
    """
    Views for endpoints which return xxxxx
    """

    def post(self):
        pass

    def put(self, user_id):
        pass

    def delete(self, user_id):
        pass

    def get(self, user_id):
        return make_response(f'get: url configured correctly', 200)

    def search(self):
        return make_response(f'search: url configured correctly', 200)
        pass
