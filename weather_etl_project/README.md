# Weather ETL Pipeline Documentation

## Project Overview

This project implements a complete ETL (Extract, Transform, Load) pipeline for weather data. It collects current weather information from multiple cities via the OpenWeatherMap API, processes the data into a structured format, and stores it in a SQLite database for analysis and visualization.

## System Requirements

- Python 3.7+
- Required Python packages:
  - requests
  - pandas
  - matplotlib
  - sqlalchemy
  - jupyter
  - schedule (for automated runs)

## Project Structure

```
weather_etl_project/
├── config.py          # Configuration settings
├── extract.py         # Data extraction module
├── transform.py       # Data transformation module
├── load.py            # Database loading module
├── main.py            # Main ETL pipeline orchestration
├── scheduler.py       # Automated scheduling (optional)
├── exploration.ipynb  # Data analysis notebook
└── weather_data.db    # SQLite database (generated)
```

## Component Details

### config.py

Contains all configuration settings for the project:

- `API_KEY`: Your OpenWeatherMap API key
- `CITIES`: List of cities to collect weather data for
- `BASE_URL`: Base URL for the OpenWeatherMap API
- `DATABASE_PATH`: Path to the SQLite database file

### extract.py

Handles the extraction of raw weather data:

- Function: `extract_weather_data()`
- Makes HTTP requests to the OpenWeatherMap API for each city
- Adds collection timestamp and city name to the data
- Returns a pandas DataFrame containing raw JSON data

### transform.py

Processes and cleans the raw data:

- Function: `transform_weather_data(raw_df)`
- Flattens nested JSON structures
- Extracts relevant weather metrics
- Creates standardized datetime fields
- Returns a structured DataFrame ready for storage

### load.py

Manages database operations:

- Function: `load_to_sqlite(df)`
- Creates or connects to SQLite database
- Appends new data to the existing table
- Function: `get_connection()`
- Provides direct database connections for queries

### main.py

Orchestrates the entire ETL process:

- Function: `run_etl_pipeline()`
- Coordinates extraction, transformation, and loading
- Provides logging of pipeline execution
- Can be run directly to perform a complete ETL cycle

### scheduler.py (Optional)

Handles automated pipeline execution:

- Schedules the ETL pipeline to run at regular intervals
- Uses the `schedule` library to manage timing
- Can be configured to run hourly, daily, etc.

### exploration.ipynb

Jupyter notebook for data analysis:

- Connects to the SQLite database
- Provides sample queries and visualizations
- Demonstrates how to analyze the collected weather data

## Setup Instructions

1. **Clone or create the project structure**:
   - Create the directory structure as shown above
   - Create each file with the provided code

2. **Install required dependencies**:
   ```bash
   pip install requests pandas matplotlib sqlalchemy jupyter schedule
   ```

3. **Get an API key**:
   - Sign up for a free account at [OpenWeatherMap](https://openweathermap.org/)
   - Navigate to your account to get your API key
   - Note: The API key may take a few hours to activate

4. **Configure the project**:
   - Edit `config.py` to include your API key
   - Add or modify the list of cities you want to track

## Usage Instructions

### Running the ETL Pipeline

To execute a single run of the ETL pipeline:

```bash
python main.py
```

This will:
1. Extract current weather data for configured cities
2. Transform the data into a structured format
3. Load the data into the SQLite database
4. Print a summary of the operation

### Setting Up Scheduled Runs

To set up automated data collection:

```bash
python scheduler.py
```

This will:
1. Run the ETL pipeline immediately
2. Schedule future runs at the configured interval
3. Continue running until manually stopped

### Analyzing the Data

To explore and visualize the collected data:

1. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

2. Open `exploration.ipynb`

3. Run the cells to:
   - Connect to the database
   - Query collected weather data
   - Visualize weather patterns and trends

## Customization

### Adding More Cities

Modify the `CITIES` list in `config.py`:

```python
CITIES = ["London", "New York", "Tokyo", "Sydney", "Paris", "Your City"]
```

### Changing Collection Frequency

Edit the schedule in `scheduler.py`:

```python
# For hourly collection
schedule.every().hour.do(job)

# For daily collection at noon
schedule.every().day.at("12:00").do(job)

# For collection every 30 minutes
schedule.every(30).minutes.do(job)
```

### Extending the Pipeline

The modular design allows for easy extension:
- Add new transformation steps in `transform.py`
- Create additional analysis notebooks
- Implement data export features
- Add error handling and notification systems

## Troubleshooting

### API Connection Issues

- Ensure your API key is correctly entered in `config.py`
- Check that your API key is activated (can take a few hours)
- Verify internet connectivity

### Database Errors

- Ensure the database directory is writable
- Check that SQLite is installed properly
- Verify the database isn't locked by another process

### Scheduling Problems

- Make sure the `schedule` library is installed
- Check that the scheduling script remains running
- Verify system time is correct

## Further Enhancements

Potential improvements to consider:
- Add error handling and retry logic
- Implement logging to a file
- Create a web dashboard for visualizations
- Export data to other formats (CSV, Excel)
- Implement data quality checks
- Add historical data collection capabilities