import plotly.graph_objs as go
import plotly.express as px
import pandas as pd

def generate_single_charts(new_data, crop):
    new_data = new_data.groupby(['Crop', 'Year'], as_index=False)['Yield'].sum()
    crop_data = new_data[new_data['Crop'] == crop]
    crop_data = crop_data.sort_values('Year')  # Ensure data is sorted by year

    animation_data = crop_data.copy()
    animation_data['Year'] = pd.Categorical(animation_data['Year'])  # This ensures the correct ordering
    animation_data['ID'] = range(len(animation_data))  # Unique ID for each frame

    # Create the animated line chart
    # line_chart = px.line(
    #     animation_data,
    #     x='Year',
    #     y='Yield',
    #     animation_frame='ID',  # Animate over the ID
    #     range_y=[crop_data['Yield'].min(), crop_data['Yield'].max()]
    # )
    #
    # line_chart.update_layout(
    #     title='Crop Production Over the Years (Animated Line Chart)',
    #     xaxis_title='Year',
    #     yaxis_title='Production Volume'
    # )
    # Line Chart
    line_chart = go.Figure()
    line_chart.add_trace(go.Scatter(x=crop_data['Year'], y=crop_data['Yield'], mode='lines+markers', name=crop))
    line_chart.update_layout(title='Crop Production Over the Years (Line Chart)',
                             xaxis_title='Year',
                             yaxis_title='Production Volume',
                             legend_title='Crop')

    # Area Chart
    area_chart = go.Figure()
    area_chart.add_trace(go.Scatter(x=crop_data['Year'], y=crop_data['Yield'], fill='tozeroy', name=crop))
    area_chart.update_layout(title='Crop Production Over the Years (Area Chart)',
                             xaxis_title='Year',
                             yaxis_title='Production Volume',
                             legend_title='Crop')

    # Bar Chart
    bar_chart = go.Figure()
    bar_chart.add_trace(go.Bar(x=crop_data['Year'], y=crop_data['Yield'], name=crop))
    bar_chart.update_layout(title='Crop Production Over the Years (Bar Chart)',
                            xaxis_title='Year',
                            yaxis_title='Production Volume',
                            legend_title='Crop')

    return line_chart, area_chart, bar_chart


def generate_comparison_charts(new_data, crops):
    # Filter data for the selected crops
    new_data = new_data.groupby(['Crop', 'Year'], as_index=False)['Yield'].sum()
    comparison_data = new_data[new_data['Crop'].isin(crops)]

    # Line Chart
    line_chart = go.Figure()
    for crop in crops:
        crop_data = comparison_data[comparison_data['Crop'] == crop]
        line_chart.add_trace(go.Scatter(x=crop_data['Year'], y=crop_data['Yield'], mode='lines+markers', name=crop))

    line_chart.update_layout(title='Crop Yield Comparison Over the Years (Line Chart)',
                             xaxis_title='Year',
                             yaxis_title='Yield',
                             legend_title='Crops')

    # Stacked Area Chart
    stacked_area_chart = go.Figure()
    for crop in crops:
        crop_data = comparison_data[comparison_data['Crop'] == crop]
        stacked_area_chart.add_trace(
            go.Scatter(x=crop_data['Year'], y=crop_data['Yield'], mode='lines', stackgroup='one', name=crop))

    stacked_area_chart.update_layout(title='Crop Yield Comparison Over the Years (Stacked Area Chart)',
                                     xaxis_title='Year',
                                     yaxis_title='Yield',
                                     legend_title='Crops')

    # Grouped Bar Chart
    grouped_bar_chart = go.Figure()
    for crop in crops:
        crop_data = comparison_data[comparison_data['Crop'] == crop]
        grouped_bar_chart.add_trace(go.Bar(x=crop_data['Year'], y=crop_data['Yield'], name=crop))

    grouped_bar_chart.update_layout(title='Crop Yield Comparison Over the Years (Grouped Bar Chart)',
                                    xaxis_title='Year',
                                    yaxis_title='Yield',
                                    barmode='group',
                                    legend_title='Crops')

    return line_chart, stacked_area_chart, grouped_bar_chart