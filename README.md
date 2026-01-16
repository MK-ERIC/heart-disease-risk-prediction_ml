<<<<<<< HEAD
Heart Disease Risk Prediction System

Course: ITLML801 – Machine Learning

Registration Number: 25RP21640
Environment Name: ITML\_801\_S\_A\_25RP21640

1. Project Overview

This project implements a complete end-to-end Heart Disease Risk Prediction System using machine learning.
The system predicts five levels of heart disease risk based on routinely collected clinical and diagnostic data and deploys the best model using a Flask REST API connected to a responsive web frontend.

The system is designed as a clinical decision support tool to assist healthcare professionals at CHUB Hospital.

2. Dataset Description

Total samples: 5000 patients

Total features: 13 input features

Target variable: heart\_disease

Target Classes
Label	Description
0	No Disease
1	Very Mild
2	Mild
3	Severe
4	Immediate Danger
Input Features

Age

Sex

Chest pain type (cp)

Resting blood pressure (trestbps)

Cholesterol (chol)

Fasting blood sugar (fbs)

Rest ECG (restecg)

Maximum heart rate (thalach)

Exercise-induced angina (exang)

Oldpeak

Slope

Number of vessels (ca)

Thalassemia (thal)

3. Virtual Environment Setup
   Environment Name (MANDATORY)
   ITML\_801\_S\_A\_25RP21640

Create Environment
python -m venv ITML\_801\_S\_A\_25RP21640

Activate Environment

Windows

ITML\_801\_S\_A\_25RP21640\\Scripts\\activate

Install Dependencies
pip install -r requirements.txt

4. Project Structure
   ITML\_801\_S\_A\_25RP21640/
   │
   ├── deployment/
   │   ├── heart\_model.pkl
   │   ├── feature\_columns.txt
   │   └── class\_names.txt
   │
   │
   ├── video/
   │   └── exam video.mp4
   │
   ├── training\_notebook.ipynb
   ├── app\_25RP21640.py
   ├── index\_25RP21640.html
   ├── requirements.txt
   ├── README.md
   └── test.py
   └── Heart\_Disease\_Report.pdf
5. Exploratory Data Analysis (EDA)

The following analyses were performed:

Dataset loading and inspection

Dataset shape (instances \& features)

Data types and detailed information

Missing values analysis

Descriptive statistics (numerical features)

Class distribution and percentage contribution

Balance/imbalance analysis

Visualizations:

Class distribution bar plot

Correlation heatmap (numerical features only)

Age vs heart disease box plot

Cholesterol vs heart disease box plot

Missing values percentage bar chart

6. Data Preprocessing

Target encoding (5-class mapping)

Stratified 80/20 train-test split

Numerical pipeline:

Missing value imputation

StandardScaler

Categorical pipeline:

Most-frequent imputation

OneHotEncoder (handle unknown)

Combined using ColumnTransformer

Verified:

Zero missing values after transformation

All transformed features are numeric

7. Model Training \& Evaluation
   Models Trained

MLP / ANN

Random Forest

Support Vector Machine (SVM)

K-Nearest Neighbors (KNN)

Gradient Boosting

Techniques Used

Full preprocessing + model pipelines

Hyperparameter tuning with GridSearchCV

Cross-validation accuracy

Training time measurement

Model Comparison

A comparison table was created with:

Best CV accuracy

Train accuracy

Test accuracy

Overfitting gap

Fit status (Overfit / Underfit / Best Fit)

Best Model

The best-performing model was selected based on highest test accuracy and minimal overfitting gap.

8. Model Persistence

Saved artifacts inside deployment/:

Full trained pipeline (.pkl)

Feature column names

Class names

Verification

Reloaded model and tested on random test samples

Created new patient samples and generated predictions

Verified predictions consistency

9. Flask API Deployment
   API Endpoints

/ → API status

/api/info → Model information

/api/predict → Heart disease prediction

Run Flask App
python app\_25RP21640.py

10. Frontend Application

Single-page HTML interface

Input form for all 13 features

Color-coded risk output

Confidence score and probabilities

Fully responsive (mobile, tablet, desktop)

Connected to Flask API using Fetch API

11. Testing

Three patient cases tested

Predictions compared across:

Training notebook

Flask API

Frontend interface

Identical results confirmed

Run API tests:

python test.py

12. Documentation \& Video

Included:

Professional PDF report

5-minute video demonstration:

Training code

Flask API running

Frontend prediction

Prediction consistency verification

13. Conclusion

This project successfully demonstrates a complete machine learning lifecycle, from data analysis and model training to deployment and user interaction.
The system provides a reliable and interpretable heart disease risk prediction tool suitable for clinical decision support at CHUB Hospital.

=======
# heart-disease-risk-prediction_ml
practical exam
>>>>>>> 843bb56c4dd513279a5203f2ac995d6e1f2ef44c
