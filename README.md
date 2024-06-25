### Dataset
- Primary Source: Collected from the Indian government website india.gov.in.
- Converted into a pandas-readable format using the openpyxl library.
- Supplementary Data: Extracted from NASA's website, including features such as soil, temperature, and rainfall.
- The dataset contains around 200,000 data points covering at least 30 different Indian crop IDs.

### Techniques Used
- Data Preprocessing:

  - Data conversion and cleaning using pandas and openpyxl.
  - Integration of supplementary data (soil, temperature, rainfall) from NASA.

- Modeling:

  - ARIMA: Used for predicting temperature, rainfall, and soil conditions.
  - Random Forest: Implemented for crop yield prediction based on the preprocessed dataset.
    
### Future Model Suggestions
Incorporating Crop Intelligence: Using advanced models like LSTM (Long Short-Term Memory) to improve predictions by capturing temporal dependencies in the data.

### Project Basis
This project is based on the Gaia Theory, which emphasizes the interconnectedness and circularity in the demand and supply of agricultural crops in India.

### Conclusion
By leveraging a scarce dataset and advanced modeling techniques, this project aims to enhance the understanding and prediction of agricultural patterns in India, ultimately contributing to more sustainable and efficient agricultural practices.
