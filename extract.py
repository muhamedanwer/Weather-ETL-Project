import requests
import pandas as pd 
from datetime import datetime
import config


def extract_weather():
    data = []

    for city in config.CITIES:
        params = {
            'q' : city,
            'appid' : config.API_KEY,
            'units' : 'metric'      # for temp in celsius
        }
        response = requests.get(config.BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()

            # Add timestamp and city for tracking
            data['timestamp'] = datetime.now().isoformat()
            data['city_name'] = city
            
            data_list.append(data)
        else:
            print(f"Error fetching data for {city}: {response.status_code}")
    
    # Return as DataFrame
    return pd.DataFrame(data_list)