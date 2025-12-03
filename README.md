# Indonesian Earthquake Markov Chain Model

A comprehensive Python implementation of a discrete-time Markov Chain model for analyzing earthquake patterns in Indonesia using the Kaggle earthquake dataset.

## 📊 Project Overview

This project implements a first-order Markov Chain to model earthquake state transitions in Indonesia, providing insights into seismic sequence patterns and earthquake occurrence probabilities.

### 🎯 Key Features

- **Magnitude-based State Classification**: Small (<4.0), Medium (4.0-6.0), Large (≥6.0)
- **Geographic Region Integration**: 9 regional zones covering Indonesian archipelago
- **Multi-step Transition Analysis**: Compute n-step transition probabilities
- **Comprehensive Statistical Analysis**: State persistence, steady-state distributions
- **Synthetic Data Testing**: Built-in demo with realistic earthquake patterns

## 🔬 Methodology

### State Definition
1. **Magnitude-only states**: Three categories based on earthquake magnitude
2. **Combined states**: Magnitude + geographical regions for spatial analysis

### Geographic Binning
- **Latitude bins**: [-12, -6, 0, 6] (Southern, Central, Northern regions)
- **Longitude bins**: [90, 110, 130, 150] (Western, Central, Eastern regions)
- **Total regions**: 9 distinct geographical zones

### Analysis Components
- Transition count matrices
- Transition probability matrices
- N-step transition calculations (2, 5, 10 steps)
- Steady-state distribution analysis
- State persistence evaluation

## 📁 Dataset

**Source**: [Indonesian Earthquakes Dataset](https://www.kaggle.com/datasets/kekavigi/earthquakes-in-indonesia)

**Format**: TSV (Tab-separated values)

**Key Columns**:
- `tgl`: Event date
- `ot`: Origin time
- `lat`: Latitude
- `lon`: Longitude
- `mag`: Magnitude
- `depth`: Hypocenter depth

## 🚀 Quick Start

### Prerequisites
```bash
pip install pandas numpy jupyter
```

### Usage
1. Download the dataset from Kaggle
2. Update the `DATA_PATH` variable in cell 4
3. Run all cells in sequence
4. Execute `results = main()` to perform full analysis

### Demo Mode
Run the synthetic data demo without downloading the dataset:
```python
demo_results = run_demo()
```

## 📈 Sample Results

### Transition Probabilities (Demo Data)
```
         Large  Medium   Small
Large   0.1379  0.4138  0.4483
Medium  0.0403  0.2500  0.7097
Small   0.0607  0.2341  0.7052
```

### Key Insights
- **Small earthquakes dominate**: ~69% of events
- **High persistence**: P(Small→Small) = 70.5%
- **Large to small tendency**: Large earthquakes often followed by smaller ones
- **Quick convergence**: Steady-state reached within 5 steps

## 🛠️ Model Architecture

### Core Functions
- `assign_magnitude_state()`: Classify earthquakes by magnitude
- `assign_region_state()`: Geographic binning
- `compute_transition_matrix()`: Build Markov chain
- `n_step_transition_matrix()`: Multi-step analysis
- `analyze_markov_chain()`: Comprehensive evaluation

### Additional Utilities
- `save_results_to_file()`: Export analysis results
- `compute_steady_state()`: Long-term distribution
- `analyze_steady_state()`: Equilibrium analysis

## 🎓 Educational Applications

### Seismology Research
- Understanding earthquake sequence patterns
- Baseline for complex models (HMM, PSHA)
- Statistical seismology education

### Data Science Learning
- Markov chain implementation
- Time series state modeling
- Scientific data preprocessing

## ⚠️ Model Limitations

### Assumptions
1. **First-order Markov property**: Next state depends only on current state
2. **Time-homogeneous**: Constant transition probabilities
3. **Discrete states**: Finite earthquake categories
4. **Sequential dependence**: Event order matters

### Limitations
1. **No temporal spacing**: Time between events not modeled
2. **Coarse spatial resolution**: Limited regional binning
3. **No "quiet" periods**: Only event-to-event transitions
4. **Stationarity assumption**: May not capture long-term changes
5. **Historical data dependency**: Limited by available records

## 📚 Technical Implementation

### Dependencies
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations and matrix operations
- **datetime**: Timestamp processing

### Performance
- **Memory efficient**: Optimized for large datasets
- **Scalable**: Handles thousands of earthquake events
- **Robust**: Error handling and data validation

## 🔮 Future Enhancements

### Model Extensions
- Higher-order Markov chains (2nd, 3rd order)
- Hidden Markov Models (HMM) integration
- Temporal spacing incorporation
- Continuous state spaces

### Analysis Features
- Spatial clustering algorithms
- Seasonal pattern detection
- Uncertainty quantification
- Cross-validation framework

## 📄 License

This project is developed for educational purposes as part of the AI coursework at Bina Nusantara University.

## 👨‍💻 Author

**Course**: Artificial Intelligence (AI) - Semester 3  
**Institution**: Bina Nusantara University  
**Project Type**: Assessment of Learning (AoL)

## 🙏 Acknowledgments

- **Kaggle** for providing the Indonesian earthquake dataset
- **BMKG** (Indonesian Meteorological, Climatological, and Geophysical Agency) for earthquake monitoring
- **Seismology research community** for methodological foundations

---

*For detailed implementation and usage instructions, please refer to the Jupyter notebook: `test.ipynb`*