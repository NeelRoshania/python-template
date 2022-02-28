from . import auth
from .app import create_app
from .endpoints import FlasktemplateView # make views avaliable to module

print("__init__.py started")
__all__ = [
    "auth",
    "create_app",
    "FlasktemplateView"
]