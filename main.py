import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point
# --- 1. Synthetic Data Generation ---
# Generate synthetic data for delivery locations and distances
np.random.seed(42)  # for reproducibility
num_deliveries = 100
delivery_locations = gpd.GeoDataFrame(
    {
        'order_id': range(num_deliveries),
        'customer_latitude': np.random.uniform(34, 35, num_deliveries),
        'customer_longitude': np.random.uniform(-118, -117, num_deliveries),
        'distance_km': np.random.uniform(1, 10, num_deliveries),
        'delivery_cost': np.random.uniform(5, 20, num_deliveries)
    },
    geometry=[Point(xy) for xy in zip(np.random.uniform(34,35,num_deliveries), np.random.uniform(-118,-117,num_deliveries))]
)
# --- 2. Data Cleaning and Preprocessing ---
# (In this synthetic dataset, no significant cleaning is needed)
# --- 3. Analysis ---
# Calculate total delivery costs
total_cost = delivery_locations['delivery_cost'].sum()
print(f"Total delivery cost: ${total_cost:.2f}")
# Analyze the relationship between distance and delivery cost
correlation = delivery_locations['distance_km'].corr(delivery_locations['delivery_cost'])
print(f"Correlation between distance and cost: {correlation:.2f}")
# Identify potential areas for cost reduction (e.g., high-cost deliveries)
high_cost_deliveries = delivery_locations[delivery_locations['delivery_cost'] > 15]
print("\nHigh-cost deliveries:")
print(high_cost_deliveries)
# --- 4. Visualization ---
# Create a scatter plot of delivery locations and costs
plt.figure(figsize=(10, 6))
plt.scatter(delivery_locations['customer_longitude'], delivery_locations['customer_latitude'], c=delivery_locations['delivery_cost'], cmap='viridis')
plt.colorbar(label='Delivery Cost')
plt.title('Delivery Locations and Costs')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
# Save the plot to a file
output_filename = 'delivery_locations.png'
plt.savefig(output_filename)
print(f"Plot saved to {output_filename}")
# --- 5. Route Optimization Suggestions (Illustrative) ---
# (This section would involve more sophisticated algorithms in a real-world scenario)
#  For this example, we'll suggest a simple strategy.
print("\nRoute Optimization Suggestions:")
print("1. Investigate high-cost deliveries (identified above) for potential route adjustments or alternative delivery methods.")
print("2. Explore route clustering algorithms to group deliveries geographically and optimize routes.")
print("3. Consider negotiating lower rates with delivery partners for high-volume areas.")
#Example of potential cost reduction based on identified high-cost deliveries
potential_savings = high_cost_deliveries['delivery_cost'].sum() * 0.15 #15% reduction
print(f"\nPotential cost savings from optimizing high-cost deliveries: ${potential_savings:.2f}")
#Note: This is a simplified analysis. A real-world application would require more complex algorithms and data.