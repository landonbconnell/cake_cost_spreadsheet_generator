import requests

def getLocation(access_token, zip_code):
    url = f"https://api.kroger.com/v1/locations?filter.zipCode.near={zip_code}"

    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + access_token
    }

    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        locations = response.json()['data']
        if locations:
            return locations[0]
        else:
            return None
    else:
        return None