import streamlit as st
import os
import pickle
from data_processing import load_data
from crop_dictionary import crop_dict


@st.cache_data
def memoized_load_data(file_path):
    return load_data(file_path)


def impute_season_values(selected_season):
    seasons = ['Kharif', 'Rabi', 'Summer', 'Whole Year', 'Winter']
    imputed_values = [0] * len(seasons)
    if selected_season in seasons:
        imputed_values[seasons.index(selected_season)] = 1
    return imputed_values


def get_predictors(feature_forecasts, state):
    columns = feature_forecasts[feature_forecasts['State'] == state].columns[1:]
    values = feature_forecasts[feature_forecasts['State'] == state].values[0][1:]
    predictors = dict(zip(columns, values))
    return predictors


def get_crop(crop):
    return crop_dict[crop]


def predict_yield(model, data, state, district, crop, year, selected_season, area):
    package_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(package_dir, 'Feature_forecast.csv')

    # Use the memoized functions to load data and model
    feature_data = memoized_load_data(file_path)
    # Getting predictors using ARIMA Modelling
    predictors = get_predictors(feature_data, state)

    # Impute the season values
    imputed_season_values = impute_season_values(selected_season)

    # Encoded Crop Value
    encoded_crop = get_crop(crop)
    # Construct the feature vector including temperature and humidity data
    X = [[encoded_crop]+ [year] +
         [predictors['Humidity']] + [predictors['Rainfall']] + [predictors['Temperature']] + [predictors[
             'Surface_Soil_Wetness']] +
          [predictors['Profile_Soil_Moisture']] + [predictors['Root_Zone_Soil_Wetness']] + [area] +
         [predictors['Yield_lag1']] + [predictors['Humidity_lag1']] + [predictors['Temperature_lag1']] + [predictors[
             'Rainfall_lag1']] +
          [predictors['Surface_Soil_Wetness_lag1']] +
          [predictors['Profile_Soil_Moisture_lag1']] + [predictors['Root_Zone_Soil_Wetness_lag1']] +
         imputed_season_values]

    # Make prediction using the loaded model
    predicted_yield = model.predict(X)
    return predicted_yield[0]
