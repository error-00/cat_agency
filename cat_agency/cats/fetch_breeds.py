import requests

def fetch_cat_breeds():
    url = "https://api.thecatapi.com/v1/breeds"
    response = requests.get(url)
    if response.status_code == 200:
        return {breed['name'].lower(): breed for breed in response.json()}
    else:
        return None