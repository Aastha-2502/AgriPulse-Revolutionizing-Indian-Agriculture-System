import streamlit as st
from data_processing import load_data, get_districts_for_state
from prediction import predict_yield, load_model

# Define SessionState class to persist tab selection across pages
class SessionState:
    def __init__(self):
        self.selected_tab = "Crop Yields Prediction"

def main():
    # Create a SessionState object
    session_state = SessionState()

    # Set page title and introduction
    st.title('Crop Yields Prediction')
    st.write('Welcome to the Crop Yields Prediction app!')

    data = load_data('../main_data.csv')
    states_list = list(sorted(data['State'].unique()))

    # Create tabs
    tabs = ["Crop Yields Prediction", "Distribution Across India"]
    selected_tab = st.sidebar.radio("Select Page", tabs, index=tabs.index(session_state.selected_tab))

    # Store the selected tab in session state
    session_state.selected_tab = selected_tab

    if selected_tab == "Crop Yields Prediction":
        # Sidebar customization for the "Crop Yields Prediction" page
        st.sidebar.header("Prediction Options")
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
    elif selected_tab == "Distribution Across India":
        # Sidebar customization for the "Distribution Across India" page
        st.sidebar.header("Distribution Options")
        st.sidebar.write("Customize your distribution map here.")

        # You can include your distribution map visualization code here
        st.write("Distribution Across India Tab Selected")
        # Add your distribution map visualization code here

if __name__ == "__main__":
    main()
