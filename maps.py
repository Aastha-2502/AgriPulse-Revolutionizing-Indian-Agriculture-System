import folium
import os
import json
import pandas as pd
import numpy as np

from state_coords import state_coords, state_code_mapping


def create_india_map(data, crop, year):
    # Filter the dataset based on user input for crop and year
    filtered_data = data[(data['Crop'] == crop) & (data['YEAR'] == year)]

    if filtered_data.empty:
        return folium.Map(location=[20.5937, 78.9629], zoom_start=5)  # Return an empty map if no data found

    # Map state names to state codes
    filtered_data['state_code'] = filtered_data['State'].map(state_code_mapping)

    # Aggregate yield by state code
    state_codes = []
    state_yield = []
    state_names = []

    for state_code in filtered_data['state_code'].unique():
        total_yield = np.sum(filtered_data[filtered_data['state_code'] == state_code]['Yield (Tonne/Hectare)'])
        state_codes.append(state_code)
        state_yield.append(total_yield)
        state_names.append(filtered_data[filtered_data['state_code'] == state_code]['State'].iloc[0])

    new_data = pd.DataFrame({
        'state_code': state_codes,
        'yield': state_yield,
        'state': state_names
    })

    # Load the geoJSON file
    package_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(package_dir, 'states_india.geojson')

    with open(file_path, 'r', encoding='utf-8') as file:
        up_geojson = json.load(file)

    # Create a folium map
    map_india = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

    # Add markers for each state
    for state, lat, lon in state_coords:
        folium.Marker(location=[lat, lon], popup=f"State: {state}").add_to(map_india)

    # Create a choropleth layer
    choropleth = folium.Choropleth(
        geo_data=up_geojson,
        name='choropleth',
        data=new_data,
        columns=['state_code', 'yield'],
        key_on='feature.properties.state_code',
        fill_color='viridis',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name=f'Yield for {crop} in {year}'
    ).add_to(map_india)

    # Add a LayerControl and display the map
    folium.LayerControl().add_to(map_india)

    return map_india
