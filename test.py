import requests

url = "http://127.0.0.1:5000/predict"

# Example: Immediate Danger
test_input = {
    "age": 68,
    "sex": "Male",
    "cp": "Asymptomatic",
    "trestbps": 170,
    "chol": 320,
    "fbs": "True",
    "restecg": "LV hypertrophy",
    "thalach": 110,
    "exang": "Yes",
    "oldpeak": 3.5,
    "slope": "Downsloping",
    "ca": 3,
    "thal": "Reversible defect"
}

response = requests.post(url, json=test_input)

if response.status_code == 200:
    result = response.json()
    print("Prediction:", result["prediction"])
    print("Probabilities:")
    for cls, prob in result["probabilities"].items():
        print(f"  {cls}: {prob*100:.1f}%")
else:
    print("Error:", response.text)
