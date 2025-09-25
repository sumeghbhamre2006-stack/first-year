#Predicting house prices using tensor flow.
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt




# Example data: house sizes (sqft) and corresponding prices ($1000s)
house_sizes = np.array([500, 750, 1000, 1250, 1500, 1750, 2000, 2250, 2500], dtype=float)
house_prices = np.array([150, 200, 250, 300, 350, 400, 450, 500, 550], dtype=float)




# Normalize data
house_sizes /= 2500
house_prices /= 550




# Build the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])




model.compile(optimizer='adam', loss='mean_squared_error')




# Train the model
model.fit(house_sizes, house_prices, epochs=500, verbose=0)




# Test prediction




new_house_size = np.array([1800 / 2500])
predicted_price = model.predict([new_house_size]) * 550




print(f"Predicted price for 1800 sqft house: ${predicted_price[0][0]:.2f}K")




# Plot the results
plt.scatter(house_sizes * 2500, house_prices * 550, color='blue', label='Data')
predicted_prices = model.predict(house_sizes) * 550
plt.plot(house_sizes * 2500, predicted_prices, color='red', label='Prediction')
plt.xlabel('Size (sqft)')
plt.ylabel('Price ($1000s)')
plt.legend()
plt.show()
