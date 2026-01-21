#libraries used
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#1.Generate Random House Prices (NumPy)
# Set seed for reproducibility
np.random.seed(42)

# Generate 10,000 house prices (normal distribution)
# Mean = 5,000,000 | Std Dev = 1,500,000
house_prices = np.random.normal(loc=5000000, scale=1500000, size=10000)

# Convert to positive values (no negative prices)
house_prices = np.abs(house_prices)
#2.average calcualtion
average_price = np.mean(house_prices)
print(f"Average House Price: ₹{average_price:,.2f}")

#3.Outlier Detection & Removal (IQR Method)
# Calculate quartiles
Q1 = np.percentile(house_prices, 25)
Q3 = np.percentile(house_prices, 75)

# Interquartile Range
IQR = Q3 - Q1

# Define bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Remove outliers
filtered_prices = house_prices[
    (house_prices >= lower_bound) &
    (house_prices <= upper_bound)
]

print("Original Count:", len(house_prices))
print("After Outlier Removal:", len(filtered_prices))

#Visualization
plt.figure(figsize=(8,5))
plt.hist(filtered_prices, bins=50)
plt.title("House Price Distribution (After Outlier Removal)")
plt.xlabel("House Price")
plt.ylabel("Frequency")
plt.show()

#Box Visualization)
plt.figure(figsize=(8,3))
plt.boxplot(filtered_prices, vert=False)
plt.title("Box Plot of House Prices")
plt.xlabel("House Price")
plt.show()

