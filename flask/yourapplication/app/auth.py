import functools
import random
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
# from flaskr.db import get_db

# # blueprints
# bp = Blueprint('general', __name__, url_prefix='/auth')

# # views
# @bp.route('/hello', methods=["GET"])
# def hello():
#     if request.method == 'GET':
#         return f'test: {random.randbytes(10)}'

print("auth.py: nothing to show here")