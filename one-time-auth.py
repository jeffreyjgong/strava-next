import pickle

from stravalib.client import Client
from dotenv import dotenv_values


config = dotenv_values('.env')
print(config)

client = Client()

authorize_url = client.authorization_url(client_id=int(config['CLIENT_ID']), redirect_uri='http://127.0.0.1:5000/authorization', scope=['read_all', 'profile:read_all', 'activity:read_all'])

print(authorize_url)

CODE = config['ONE_TIME_CODE']

access_token = client.exchange_code_for_token(client_id=int(config['CLIENT_ID']), client_secret=config['CLIENT_SECRET'], code=CODE)

with open('access_token.pickle', 'wb') as f:
    pickle.dump(access_token, f)

with open('access_token.pickle', 'rb') as f:
    access_token = pickle.load(f)

print(f'Latest access token read from file: {access_token}')