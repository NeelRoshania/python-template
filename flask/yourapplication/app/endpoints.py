from flask import make_response
from flask.views import MethodView

class FlasktemplateView(MethodView):
    
    """
    Views for endpoints which return xxxxx
    """
    
    def get(self, user_id):
        return make_response(f'response: url configured correctly', 200)

    def post(self):
        pass

    def delete(self, user_id):
        pass

    def put(self, user_id):
        pass

    def search(self):
        pass
