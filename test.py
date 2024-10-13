import pickle
import time

from stravalib.client import Client
from dotenv import dotenv_values

client = Client()
config = dotenv_values('.env')

def get_access_token():
    with open('access_token.pickle', 'rb') as f:
        access_token = pickle.load(f)

    return access_token

def set_up_to_date_token():
    access_token = get_access_token()

    if time.time() > access_token['expires_at']:
        print('Token has expired, will refresh')

        refresh_response = client.refresh_access_token(
            client_id=int(config['CLIENT_ID']),
            client_secret=config['CLIENT_SECRET'],
            refresh_token=access_token['refresh_token'],
        )

        access_token = refresh_response

        with open('access_token.pickle', 'wb') as f:
            pickle.dump(refresh_response, f)

        client.access_token = refresh_response['access_token']
    else:
        print('Token still valid')
        client.access_token = access_token['access_token']

set_up_to_date_token()

def athlete_info():
    athlete = client.get_athlete()
    print(f"Athlete's name is {athlete.firstname} {athlete.lastname}, based in {athlete.city}, {athlete.country}")

athlete_info()

