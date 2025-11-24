import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv("home_dataset.csv")
houseSize = data['HouseSize'].values
housePrice = data ['HousePrice'].values

plt.scatter(houseSize, housePrice)
plt.title('House Price vs House Size')
plt.xlabel("House Size (sq. ft)")
plt.ylabel("House Price (millions $)")
plt.show()

# Split the data into training and testing sets 80/20
x_train, x_test, y_train, y_test = train_test_split(houseSize, housePrice, test_size=0.2, random_state=42)

x_train = x_train.reshape(-1, 1)
x_test = x_test.reshape(-1, 1)

model = LinearRegression()
model.fit(x_train, y_train)


#prediction for test set
predictions = model.predict(x_test)

#visualize prediction
plt.scatter(x_test, y_test, marker = 'o', color = 'blue', label = 'Actual Prices')
plt.plot(x_test, predictions, color = 'red', linewidth=2, label="Predicted Prices")
plt.title("Property Price Prediction with Linear Regression")
plt.xlabel("House Size (sq. ft)")
plt.ylabel("House Price (millions $)")
plt.legend()
plt.show()

