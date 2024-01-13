import os
from datetime import datetime
from config.app_contex import base_dir
from prometheus_client import Gauge, Counter

# Metrics definition
total_tests = Gauge('total_test', 'Total number of tests')
seasons = ['summer', 'winter', 'spring']
metrics = {season: Gauge(f'total_{season}_tests', f'Total number of {season} tests') for season in seasons}
files_with_year = {year: Gauge(f'number_tests_in_{year}', f'Number of tests in "{year}"') for year in range(2000, datetime.now().year + 1)}
files_served = Counter('files_served', 'Total number of files served through the route')
serves_per_file = Gauge('serves_per_file', 'Number of times each file is served', ['filename'])
files_served._value.set(0)

def initialize_metrics():
    total_test_metric()
    for season in seasons:
        total_season_test_metric(season)
    files_with_year_metric()

def total_test_metric():
    total_tests.set(count_files_in_directory(base_dir))

def total_season_test_metric(season):
    metrics[season].set(count_files_in_directory_season(base_dir, season))

def files_with_year_metric():
    current_year = datetime.now().year
    for year in range(2000, current_year + 1):
        files_with_year[year].set(count_files_containing_year(base_dir, str(year)))

def count_files_in_directory(directory):
    file_count = len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])
    return file_count

def count_files_in_directory_season(directory, season):
    file_count = len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and season in f])
    return file_count

def count_files_containing_year(directory, year):
    file_count = len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and year in f])
    return file_count
