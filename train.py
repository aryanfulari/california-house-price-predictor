import joblib
import numpy as np

from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


# ----------------------------------------
# Load Dataset
# ----------------------------------------

housing = fetch_california_housing()

X = housing.data
y = housing.target

feature_names = housing.feature_names

print("Features:")
print(feature_names)

print("\nNumber of samples:", X.shape[0])
print("Number of features:", X.shape[1])


# ----------------------------------------
# Train-Test Split
# ----------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=67
)


# ----------------------------------------
# Train Model
# ----------------------------------------

model = LinearRegression()

model.fit(X_train, y_train)


# ----------------------------------------
# Predictions
# ----------------------------------------

y_pred = model.predict(X_test)


# ----------------------------------------
# Evaluation
# ----------------------------------------

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\nModel Performance")
print("---------------------")
print(f"RMSE : {rmse:.3f}")
print(f"R²   : {r2:.3f}")


# ----------------------------------------
# Save Model
# ----------------------------------------

joblib.dump(model, "model/house_price_model.pkl")

print("\nModel saved successfully!")