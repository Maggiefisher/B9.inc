import requests
from datetime import datetime, timedelta

ACCESS_TOKEN = 'EAAzpW9FP5ZB4BOww0uSKTRaeh1pQYoUToqoNblrYML5rR6NFbw5kxi76G3D2XcduxbvtGUGLpnNSGH0dPsBPzFBkiivNEuApWuOxVd6DOdZCG6ymj505cKXXf4axFx38vXY8ZCPWBeZBUhOyynivFGHzKoS32qjbpvzW8SdNesnH4VNm3qbWvVemMZAUB6amOOXsbKYIG36wbU07MiHIMGYZAFy3XGrGoV6n0hl8bunpkZD'

INSTAGRAM_BUSINESS_ACCOUNT_ID = '17841403777123276'
DAYS_TO_AGGREGATE = 7

# Function to make API requests
def get_daily_insight(metric, date):
    since = int(date.timestamp())
    until = int((date + timedelta(days=1)).timestamp())
    url = f'https://graph.facebook.com/v12.0/{INSTAGRAM_BUSINESS_ACCOUNT_ID}/insights?metric={metric}&metric_type=total_value&period=day&since={since}&until={until}&access_token={ACCESS_TOKEN}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data for {metric} on {date.strftime('%Y-%m-%d')}:", response.status_code, response.text)
        return None

# Aggregate data over specified days
aggregate_value = 0
current_date = datetime.utcnow() - timedelta(days=DAYS_TO_AGGREGATE)
error_occurred = False

for _ in range(DAYS_TO_AGGREGATE):
    data = get_daily_insight('follows_and_unfollows', current_date)
    if data:
        if 'data' in data and len(data['data']) > 0 and 'values' in data['data'][0]:
            daily_value = data['data'][0]['values'][0]['value']
            aggregate_value += daily_value
        current_date += timedelta(days=1)
    else:
        error_occurred = True
        break

if not error_occurred:
    print(f"Net follower change (follows minus unfollows) over {DAYS_TO_AGGREGATE} days:", aggregate_value)
else:
    print("An error occurred, stopping data retrieval.")