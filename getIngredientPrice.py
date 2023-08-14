import requests
from bs4 import BeautifulSoup

def getIngredientPrice(url):

# def getIngredientPrice(access_token, location_id, product_id):
#     url = 'https://api-ce.kroger.com/v1/products'

#     headers = {
#         'Accept': 'application/json',
#         'Authorization': 'Bearer ' + access_token
#     }

#     params = {
#         'filter.productId': product_id,
#         'filter.locationId': location_id,
#         'filter.limit': '1',
#     }

#     response = requests.get(url, headers=headers, params=params)

#     # Check if the request was successful
#     if response.status_code == 200:
#         data = response.json()['data']
#         if data:
#             print(data[0])
#             return data[0]['items'][0]['price']['regular']
#         else:
#             return None
#     else:
#         return None

def