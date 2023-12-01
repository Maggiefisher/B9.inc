import requests
from datetime import datetime, timedelta

ACCESS_TOKEN = 'EAAzpW9FP5ZB4BOZB4jTX6sRVkkx4HjfsmpcIrrpzulvfkghQnaKlRGfL5nXnlhJImlMj20jUnbZAtmZB4mxsutCa6QqqBmcI185sFswZCX2vygFqI8SRFkXoJ7gTY8NxGeEGWTzDNRX3B48UHZBRX8iMmj95a8TnyEx5LXHt9j5EhGI8em50SOGXNS58BLPmshD32UFzvH2ILGIaaZBka8CeeEuMbjFoyoZCL4Rj974tbQm7'

INSTAGRAM_BUSINESS_ACCOUNT_ID = '17841403777123276'
DAYS_TO_AGGREGATE = 100  

def get_daily_insight(metric, date):
    since = int(date.timestamp())
    until = int((date + timedelta(days=1)).timestamp())
    url = f'https://graph.facebook.com/v12.0/{INSTAGRAM_BUSINESS_ACCOUNT_ID}/insights?metric={metric}&period=day&since={since}&until={until}&access_token={ACCESS_TOKEN}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data for {metric} on {date.strftime('%Y-%m-%d')}:", response.status_code, response.text)
        return None

aggregate_value = 0
current_date = datetime.utcnow() - timedelta(days=DAYS_TO_AGGREGATE)
for _ in range(DAYS_TO_AGGREGATE):
    data = get_daily_insight('website_clicks', current_date)
    if data and 'data' in data and len(data['data']) > 0 and 'values' in data['data'][0]:
        daily_value = data['data'][0]['values'][0]['value']
        aggregate_value += daily_value
    current_date += timedelta(days=1)

print(f"Total website clicks over {DAYS_TO_AGGREGATE} days:", aggregate_value)