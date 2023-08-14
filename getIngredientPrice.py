import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def getIngredientPrice(access_token, location_id, product_id):

    url = f"https://api.kroger.com/v1/products/{product_id}?filter.locationId={location_id}"

    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + access_token
    }

    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        if data:
            price = data["data"]["items"][0]["price"]["regular"]
            return price
        else:
            return None
    else:
        print(f"Error: {response.status_code}")
        return None
