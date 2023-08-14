import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def getIngredientPrice(access_token, location_id, product_id, product_url):
    url = 'https://api-ce.kroger.com/v1/products'

    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + access_token
    }

    params = {
        'filter.productId': product_id,
        'filter.locationId': location_id,
    }

    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        print(data)
        if data:
            try:
                price = data[0]['items'][0]['price']['regular']
                return price
            except:
                price = webScrapeIngredientPrice(product_url)
                return price
        else:
            return None
    else:
        return None

async def webScrapeIngredientPrice(url):
    # Set up Chrome options for headless browsing
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    
    # Ensure the web driver is on your PATH or specify its path directly
    browser = webdriver.Chrome(options=chrome_options)
    
    # Set the implicit wait
    browser.implicitly_wait(10)  # WebDriver will wait up to 10 seconds for an element to be available

    browser.get(url)

    try:
        # Directly using Selenium to find the element
        element = browser.find_element(By.CSS_SELECTOR, ".kds-Price.kds-Price--alternate.mb-8")
        price_value = element.get_attribute("value")
        print(price_value)
        
        if price:
            print(price)
            return price
        else:
            return None
            
    except Exception as e:
        print(f"Error: {e}")
        return None

    finally:
        # Close the browser to release resources
        browser.quit()

# async def webScrapeIngredientPrice(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0'
#     }

#     print(url)

#     response = requests.get(url, headers=headers)
#     content = response.text

#     soup = BeautifulSoup(content, 'html.parser')
#     price = soup.find('data', {'typeof': 'Price'}).get('value')

#     if price:
#         print(price)
#         return price
#     else:
#         return None
