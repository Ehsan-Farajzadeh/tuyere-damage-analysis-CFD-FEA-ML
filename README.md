# Tuyere Damage Analysis using CFD-FEA-ML

## Overview
This project presents an advanced predictive framework for analyzing thermal stress damage in blast furnace tuyeres during hydrogen-rich fuel injection. The study integrates Computational Fluid Dynamics (CFD), Finite Element Analysis (FEA), and Machine Learning (ML) techniques to assess tuyere performance under various injection scenarios involving COG, RCOG, and hydrogen. 

By leveraging validated CFD simulations, structural FEA analysis, and XGBoost-based ML models, this project provides a robust tool for predicting tuyere behavior and optimizing operational conditions to minimize damage, reduce carbon emissions, and enhance blast furnace durability.

---

## Project Structure
```
tuyere-damage-analysis-CFD-FEA-ML/
│
├── data/               # Input data for ML and sample CFD results (non-sensitive)
├── fea/                # FEA setup files, stress data, and results (if shareable)
├── cfd/                # CFD simulation setup, scripts, and validation plots
├── ml/                 # ML code: XGBoost model, heatmap, PDP analysis
│   ├── xgboost_model.py
│   ├── feature_analysis.py
│   └── utils.py
├── figures/            # Key plots, diagrams, and model outputs
├── notebooks/          # Interactive Jupyter Notebooks for demo and results
├── results/            # Output summaries, charts, and metrics
├── README.md           # Project overview and instructions
├── .gitignore          # Files and folders to exclude from Git
└── requirements.txt    # Python dependencies for ML components
```

---

## Key Components

### ✅ CFD Simulation
- Models gas dynamics, temperature fields, and chemical reactions.
- Evaluates fuel injection scenarios with COG, RCOG, and H₂.
- Built using Fluent with transient, 3D Euler–Euler multiphase framework.

### ✅ FEA Analysis
- Conducted in ANSYS Static Structural.
- Uses one-way FSI to import CFD thermal loads.
- Evaluates von Mises stress on copper core and Fe-Cr coating.

### ✅ Machine Learning (XGBoost)
- Identifies key features influencing thermal stress.
- Performs feature importance, heatmap correlation, and PDP analysis.
- Enables data-driven optimization of operational parameters.

---

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/tuyere-damage-analysis-CFD-FEA-ML.git
   cd tuyere-damage-analysis-CFD-FEA-ML
   ```

2. (Optional) Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Explore interactive demos in `notebooks/` or run ML models in `ml/` folder.

---

## Confidentiality Note
Some CFD/FEA datasets and CSV outputs used in this study are confidential and not included in this repository. Dummy examples or synthetic data can be used to reproduce model training pipelines.

---

## Citation
If you use this work, please cite:
> Farajzadeh E., Zhuo Y., Shen Y. (2024). Advanced predictive tuyere damage analysis using CFD, FEA, and Machine Learning methods. *In preparation.*

---

## License
This project is for academic and non-commercial use only.
