#  Indonesian Earthquake Forecasting using Advanced Markov Chain

**Probabilistic Earthquake Forecasting Using Markov Chain Models**  
*IEEE Paper Research Project - Assessment of Learning (AoL) AI*

---

##  Overview

Advanced earthquake forecasting system for Indonesia using **2nd-order Multi-Feature Markov Chain** model. This project implements probabilistic forecasting to predict earthquake probabilities across magnitude, depth, and spatial dimensions.

### Key Features
-  **2nd-Order Markov Chain** - considers 2 previous events for better accuracy
-  **Multi-Dimensional States** - magnitude (5 bins)  depth (3 bins)  region (9 zones) = 135 states
-  **Comprehensive Data** - USGS earthquake catalog (2010-2024, M4.0)
-  **Advanced Features** - inter-event time, spatial distance, seismic energy, b-value
-  **Validated Forecasts** - train/test split with baseline comparison
-  **IEEE Paper Ready** - automated report and publication-quality figures

---

##  Quick Start

### Prerequisites
```powershell
# Install dependencies
pip install -r requirements.txt
```

### Run Full Pipeline
```powershell
# Execute complete workflow (5-10 minutes)
python run_full_pipeline.py
```

### Or Run Step-by-Step
```powershell
# Step 1: Download data from USGS
python 1_download_earthquake_data.py

# Step 2: Build and train model
python 2_advanced_markov_model.py

# Step 3: Evaluate and visualize
python 3_evaluate_and_visualize.py
```

---

##  Generated Outputs

After running the pipeline, you'll have:

###  Data Files
- indonesia_earthquakes_usgs.csv - Raw USGS earthquake data
- processed_earthquake_data.csv - Feature-engineered dataset
- data_statistics.txt - Dataset summary statistics

###  Model Files
- 	ransition_matrix_order2.npy - Trained 2nd-order transition matrix

###  Results (IEEE Paper)
- ieee_paper_report.txt - Comprehensive analysis report
- 	ransition_matrix_heatmap.png - Transition probability visualization
- magnitude_distribution.png - Training vs test comparison
- orecast_comparison.png - Markov vs baseline performance
- 	emporal_patterns.png - Temporal analysis plots

---

##  Model Performance

The model provides probabilistic forecasts:
- **1-day forecast:** P(M5.5 in next 24 hours)
- **5-day forecast:** P(M5.5 in next 5 days)  
- **10-day forecast:** P(M5.5 in next 10 days)

Validated against baseline Poisson model with 80/20 train/test split.

---

##  References

**Key Paper:**  
Susilo, A. et al. (2018). "Earthquake Analysis in East Java, Indonesia Between 1960-2017 Using Markov Chain Model"

**Data Source:**  
USGS Earthquake Hazards Program - https://earthquake.usgs.gov/

---

##  Academic Info

**Institution:** Bina Nusantara University  
**Course:** Artificial Intelligence (Semester 3)  
**Assessment:** Assessment of Learning (AoL)  
**Paper Title:** "Probabilistic Earthquake Forecasting Using Hidden Markov Models"

---

 **Ready to generate results for your IEEE paper!**
