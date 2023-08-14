import requests
from secrets import SECRETS

# returns the access token for the Kroger API
def getAccessToken():
    url = 'https://api.kroger.com/v1/connect/oauth2/token'

    response = requests.post(
        url, 
        auth=(SECRETS["KROGER_CLIENT_ID"], SECRETS["KROGER_CLIENT_SECRET"]),
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={
            "grant_type": "client_credentials",
            "scope": "product.compact"
        }
    )

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        return None
