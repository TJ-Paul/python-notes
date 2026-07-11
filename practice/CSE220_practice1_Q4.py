import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# --- Data setup ---
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
north = np.array([120, 135, 128, 142, 150, 158, 162, 170, 168, 180, 185, 195])
south = np.array([110, 118, 125, 130, 138, 145, 150, 155, 160, 168, 172, 180])
central = np.array([100, 108, 115, 120, 130, 140, 148, 152, 158, 165, 170, 175])

plt.figure(figsize=(12, 8))

# --- Subplot 1: Monthly profit trend for all branches (line chart) ---
plt.subplot(2, 2, 1)
plt.plot(months, north, linestyle='solid', color='blue', label='North')
plt.plot(months, south, linestyle='dashed', color='green', label='South')
plt.plot(months, central, linestyle='dotted', color='red', label='Central')

plt.title('Monthly Branch Profit (2025)')
plt.xlabel('Month')
plt.ylabel('profit (in thousand dollars)')
plt.grid()
plt.legend()

# --- Subplot 2: Total yearly profit per branch (bar chart) ---
plt.subplot(2, 2, 2)
area_labels = np.array(['north', 'south', 'central'])
area_sums = np.array([north.sum(), south.sum(), central.sum()])  # sum across all 12 months per branch
area_colors = np.array(['blue', 'green', 'red'])

plt.bar(area_labels, area_sums, color=area_colors)
plt.grid(axis='y')

plt.title('December profit comparison')
plt.ylabel('profit (in thousand dollars)')

# --- Subplot 3: North branch monthly profit distribution (scatter plot) ---
plt.subplot(2, 2, 3)
sizes = np.array([60] * len(months))
plt.scatter(months, north, color='blue', s = sizes)

plt.title('North Branch Profit Distribution')
plt.xlabel('Month')
plt.ylabel('profit (in thousand dollars)')
plt.grid()

# --- Subplot 4: Quarterly profit per branch (stacked bar chart) ---
plt.subplot(2, 2, 4)
x_labels = np.array(['Q1', 'Q2', 'Q3', 'Q4'])

# Reshape 12 monthly values into 4 groups of 3 months, then sum each group to get quarterly totals
north_q = north.reshape(4, 3).sum(axis=1)
south_q = south.reshape(4, 3).sum(axis=1)
central_q = central.reshape(4, 3).sum(axis=1)

plt.bar(x_labels, north_q, color='blue', label='North')
plt.bar(x_labels, south_q, color='green', label='South', bottom=north_q)  # without bottom = north_q two graphs will stack on top of each other
plt.bar(x_labels, central_q, color='red', label='Central', bottom=north_q + south_q)

plt.title('Quarterly Branch Profit')
plt.xlabel('Quarter')
plt.ylabel('profit (in thousand dollars)')
plt.grid(axis='y')
plt.legend()

plt.tight_layout()  # Fix spacing issues across the grid
plt.show()