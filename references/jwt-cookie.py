
from flask import Flask, request, jsonify, abort
import psycopg2
from psycopg2 import sql
import hashlib
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from env_variables import DATABASE_CONFIG
from oswap_jwt import get_token_payload
from faker import Faker
import random
import datetime
import jwt
import bcrypt
import datetime
import json


"""
  References,
    - bcryp password hashing, https://github.com/pyca/bcrypt/
    - jwt json web tokens, https://jwt.io/
"""

app = Flask(__name__)
fake = Faker()

def get_credit_card():
    credit_card_number = 180068442175005
    return credit_card_number

# single direction hashing
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# generate jwt token
def generate_token(username):
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=3600),
        'iat': datetime.datetime.utcnow(),
        'sub': username
    }
    return jwt.encode(
        payload,
        'secret',
        algorithm='HS256'
    )

# comparing encoded passwords
def validate_password(password, hashed_password):
    hashed = bcrypt.checkpw(password.encode(), hashed_password.encode())
    return hashed


def log_information(data):
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("[%Y-%m-%d %H:%M:%S]")
    print(timestamp ,data)


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        abort(400, description="Username and password are required")

    # identify authenticated user
    with psycopg2.connect(**DATABASE_CONFIG) as conn:
        with conn.cursor() as cur:
            query = sql.SQL("SELECT password FROM users WHERE username = %s")
            cur.execute(query, (username,))
            hashed_password = cur.fetchone()
            
    result = validate_password(password, hashed_password[0])

    if not result:
        abort(401, description="Invalid credentials")

    log_information(generate_token(username)) # log non senstive data

    # this is arguably not required for this application
    # user_information = pickle.loads(f'username:{username}, password: {password}, credit_card: {get_credit_card()}, token: {token}')' # pickle will
    # user_information = json.loads(f'username:{username}, password: {password}, credit_card: {get_credit_card()}, token: {token}')'
    # log_information(user_information["token"]) # log non senstive data

    return jsonify({"token": token}), 200

if __name__ == '__main__':
    app.run(debug=True)
