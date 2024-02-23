import streamlit as st
import pickle

def load_model(file_path="D:\\Ishaan\\Capstone_project\\2020-2022\\capstone_deployment\\model.pkl"):
    with open(file_path, 'rb') as f:
        model = pickle.load(f)
    return model


def impute_season_values(selected_season):
    seasons = ['Kharif', 'Rabi', 'Summer', 'Whole Year', 'Winter']
    imputed_values = [0] * len(seasons)
    if selected_season in seasons:
        imputed_values[seasons.index(selected_season)] = 1
    return imputed_values


def get_temperature_and_humidity_data(data, state, year):
    # Load the data

    # Filter the DataFrame based on the state and year provided by the user
    filtered_data = data[(data['State'] == state) & (data['YEAR'] == year)]

    # Retrieve temperature data for all months
    temperature_data = filtered_data[['jan_t', 'feb_t', 'mar_t', 'apr_t', 'may_t', 'jun_t',
                                      'jul_t', 'aug_t', 'sep_t', 'oct_t', 'nov_t', 'dec_t']].iloc[0].tolist()

    # Retrieve humidity data for all months
    humidity_data = filtered_data[['jan_h', 'feb_h', 'mar_h', 'apr_h', 'may_h', 'jun_h',
                                   'jul_h', 'aug_h', 'sep_h', 'oct_h', 'nov_h', 'dec_h']].iloc[0].tolist()

    return temperature_data, humidity_data


def predict_yield(model,data, state, district, year, selected_season, area, production):
    # Get temperature and humidity data for the specified state and year
    temperature_data, humidity_data = get_temperature_and_humidity_data(data, state, year)

    # Impute the season values
    imputed_season_values = impute_season_values(selected_season)

    # Construct the feature vector including temperature and humidity data
    X = [[year] + imputed_season_values + [area, production] + temperature_data + humidity_data]

    # Make prediction using the loaded model
    predicted_yield = model.predict(X)
    return predicted_yield[0]