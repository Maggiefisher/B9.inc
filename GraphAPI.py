import requests

ACCESS_TOKEN = 'EAAzpW9FP5ZB4BOZB4jTX6sRVkkx4HjfsmpcIrrpzulvfkghQnaKlRGfL5nXnlhJImlMj20jUnbZAtmZB4mxsutCa6QqqBmcI185sFswZCX2vygFqI8SRFkXoJ7gTY8NxGeEGWTzDNRX3B48UHZBRX8iMmj95a8TnyEx5LXHt9j5EhGI8em50SOGXNS58BLPmshD32UFzvH2ILGIaaZBka8CeeEuMbjFoyoZCL4Rj974tbQm7'

INSTAGRAM_BUSINESS_ACCOUNT_ID = '17841403777123276'

url = f'https://graph.facebook.com/v12.0/{INSTAGRAM_BUSINESS_ACCOUNT_ID}?fields=followers_count&access_token={ACCESS_TOKEN}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Total Followers:", data.get('followers_count'))
else:
    print("Failed to retrieve data:", response.status_code, response.text)