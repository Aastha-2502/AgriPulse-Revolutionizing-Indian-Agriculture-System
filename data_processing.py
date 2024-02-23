import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def get_districts_for_state(data, state):
    return list(data[data['State'] == state]['District'].unique())