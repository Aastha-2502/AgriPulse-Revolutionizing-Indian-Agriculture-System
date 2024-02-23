import streamlit as st
from data_processing import load_data, get_districts_for_state
from prediction import predict_yield

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

    year = st.number_input('Enter Year', min_value=1900, max_value=2100, step=1)

    if st.button('Predict Yield'):
        if not state or not district or not year:
            st.warning('Please fill in all the fields')
        else:
            predicted_yield = predict_yield(state, district, year)
            st.write(f'Predicted yield for {state}, {district} in {year}: {predicted_yield}')

    st.write('Developed by Punters')

if __name__ == "__main__":
    main()
