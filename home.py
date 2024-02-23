import streamlit as st
from data_processing import load_data, get_districts_for_state
from prediction import predict_yield, load_model

def main():
    st.title('Crop Yields Prediction')
    st.write('Welcome to Crop Yields prediction app!')

    data = load_data('../main_data.csv')
    states_list = list(sorted(data['State'].unique()))

    state = st.selectbox('Select State', [''] + states_list)

    if state:
        districts = get_districts_for_state(data, state)
        district = st.selectbox('Select District', [''] + districts)
    else:
        district = ''

    year = st.number_input('Enter Year', min_value=2018, max_value=2021, step=1)

    season = st.selectbox('Select Season', ['Autumn', 'Kharif', 'Rabi', 'Summer', 'Whole Year', 'Winter'])

    area = st.number_input('Enter Area (Hectare)', min_value=0.0)

    production = st.number_input('Enter Production (Tonnes)', min_value=0.0)

    if st.button('Predict Yield'):
        if not state or not district or not year or not season or not area or not production:
            st.warning('Please fill in all the fields')
        else:
            model = load_model()
            # You can pass these inputs to your prediction function
            predicted_yield = predict_yield(model, data, state, district, year, season, area, production)
            st.success(f'Predicted yield for {state}, {district} in {year} ({season}): {predicted_yield}')

    st.write('Developed by Punters')

if __name__ == "__main__":
    main()