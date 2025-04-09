# transform.py
import pandas as pd

def transform_weather_data(raw_df):
    """
    Transform raw weather data into a cleaner, more usable format
    """
    # Create an empty DataFrame for the transformed data
    transformed_data = []
    
    # Process each row in the raw DataFrame
    for _, row in raw_df.iterrows():
        # Extract nested data
        main_data = row['main']
        wind_data = row['wind']
        weather_data = row['weather'][0]  # Get first weather condition
        
        # Create a flattened record
        transformed_record = {
            # Metadata
            'city_name': row['city_name'],
            'collection_time': row['timestamp'],
            'weather_time': pd.to_datetime(row['dt'], unit='s'),
            
            # Location data
            'latitude': row['coord']['lat'],
            'longitude': row['coord']['lon'],
            'country': row['sys']['country'],
            
            # Main weather metrics
            'temp_celsius': main_data['temp'],
            'feels_like_celsius': main_data['feels_like'],
            'humidity_percent': main_data['humidity'],
            'pressure_hpa': main_data['pressure'],
            
            # Wind information
            'wind_speed_ms': wind_data['speed'],
            'wind_direction_degrees': wind_data.get('deg', None),
            
            # Weather description
            'weather_main': weather_data['main'],
            'weather_description': weather_data['description'],
            'weather_icon': weather_data['icon']
        }
        
        transformed_data.append(transformed_record)
    
    # Convert to DataFrame
    result_df = pd.DataFrame(transformed_data)
    
    # Add day, month, year columns for easier querying
    result_df['date'] = result_df['weather_time'].dt.date
    result_df['year'] = result_df['weather_time'].dt.year
    result_df['month'] = result_df['weather_time'].dt.month
    result_df['day'] = result_df['weather_time'].dt.day
    result_df['hour'] = result_df['weather_time'].dt.hour
    
    return result_df