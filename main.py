# main.py
import time
from datetime import datetime
from extract import extract_weather_data
from transform import transform_weather_data
from load import load_to_sqlite

def run_etl_pipeline():
    """
    Execute the full ETL pipeline
    """
    print(f"Starting ETL pipeline at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Extract
    print("Extracting data...")
    raw_data = extract_weather_data()
    print(f"Extracted weather data for {len(raw_data)} cities")
    
    # Transform
    print("Transforming data...")
    transformed_data = transform_weather_data(raw_data)
    print(f"Transformed into {len(transformed_data)} records")
    
    # Load
    print("Loading data to database...")
    load_result = load_to_sqlite(transformed_data)
    
    print("ETL pipeline completed successfully!")
    return transformed_data

if __name__ == "__main__":
    # Run the pipeline
    result = run_etl_pipeline()
    
    # Display sample of resulting data
    print("\nSample of transformed data:")
    print(result[['city_name', 'date', 'temp_celsius', 'weather_main']].head())