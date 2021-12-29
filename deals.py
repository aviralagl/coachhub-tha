import requests

url = 'https://www.cheapshark.com/api/1.0/deals'

headers = {
    'accept': 'application/json'
}

response = requests.get(
    url,
    headers=headers
)

print(response.text)
