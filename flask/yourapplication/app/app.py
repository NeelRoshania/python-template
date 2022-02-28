import pkg_resources
import random
import connexion

from connexion.resolver import MethodViewResolver
from flask import send_from_directory
from os.path import dirname, join
from . import auth
from .endpoints import FlasktemplateView

API_SPEC = pkg_resources.resource_filename(__name__, "openapi/swagger.yaml")
# OPTIONS = {"swagger_url": "/docs"}

# application factory function
def create_app(**kwargs):

    # create and configure the app
    print('API_SPEC: ', API_SPEC)
    print("dirname: ", dirname(__name__))
    
    # define connexion
    app = connexion.FlaskApp(
        __name__, 
        specification_dir="/openapi" 
        # options=OPTIONS
        )
    app.add_api(API_SPEC, resolver=MethodViewResolver(__name__.split(".")[0]))
    
    # define url rules - this shouldn't need to be configured manually
    flasktemplate_view = FlasktemplateView.as_view('flask-template')
    app.add_url_rule(
        '/flask_template/', 
        defaults={'user_id': None},
        view_func=flasktemplate_view, methods=['GET',]
    )

    return app