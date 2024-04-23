import pandas as pd
import pickle

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def load_model(file_path):
    with open(file_path, 'rb') as f:
        model = pickle.load(f)
    return model

def get_districts_for_state(data, state):
    return list(data[data['State'] == state]['District'].unique())