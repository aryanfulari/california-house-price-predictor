![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Linear%20Regression-orange?logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)
🏡 California House Price Predictor using Linear Regression

## 🌐 Live Demo

🔗 https://california-house-price-predictor-aryanfulari.streamlit.app


A Machine Learning web application that predicts California house prices using **Linear Regression** and the **California Housing Dataset** from Scikit-learn.

The application provides an interactive web interface built with **Streamlit**, allowing users to enter housing features and instantly receive a predicted house price.

---

## 📸 Application Preview

### Home Screen

![Home Screen](screenshots/home.png)

### Prediction Result

![Prediction](screenshots/prediction.png)

---

## 🚀 Features

- Predict California house prices
- Interactive Streamlit web application
- Linear Regression model trained using Scikit-learn
- Simple and clean user interface
- Real-time predictions

---

## 🧠 Machine Learning Workflow

1. Load the California Housing Dataset
2. Split the dataset into training and testing sets
3. Train a Linear Regression model
4. Evaluate the model using RMSE and R² Score
5. Save the trained model using Joblib
6. Load the saved model inside the Streamlit application
7. Accept user inputs and predict house prices

---

## 📊 Input Features

The model uses the following features:

- Median Income
- House Age
- Average Rooms
- Average Bedrooms
- Population
- Average Occupancy
- Latitude
- Longitude

---

## 🛠️ Technologies Used

- Python
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Git
- GitHub

---

## 📂 Project Structure

```text
HousePricePredictionLR/
│
├── app.py
├── train.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── model/
│   └── house_price_model.pkl
│
├── screenshots/
│   ├── home.png
│   └── prediction.png
│
└── venv/
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/aryanfulari/california-house-price-predictor
```

Move into the project folder:

```bash
cd HousePricePredictionLR
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📈 Model Performance

| Metric | Value |
|---------|-------|
| RMSE | 0.745 |
| R² Score | 0.576 |

---

## 🎯 Key Learning Outcomes

- Implemented a Linear Regression model using Scikit-learn.
- Split data into training and testing datasets.
- Evaluated model performance using RMSE and R² Score.
- Saved and loaded trained models using Joblib.
- Built an interactive web interface using Streamlit.
- Managed the project using Git and GitHub.

---

## 🚀 Future Improvements

- Add Random Forest Regression for comparison.
- Compare multiple regression algorithms.
- Improve the user interface.
- Deploy the application online.
- Add feature importance visualizations.

---

## 👨‍💻 Author

**Aryan Fulari**

Second-year Information Technology student passionate about Machine Learning, AI, and software development.

