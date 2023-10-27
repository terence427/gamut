
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# RGB primaries for different color spaces
srgb = np.array([[0.64, 0.33], [0.30, 0.60], [0.15, 0.06]])
rec709 = np.array([[0.64, 0.33], [0.30, 0.60], [0.15, 0.06]])
adobergb = np.array([[0.64, 0.33], [0.21, 0.71], [0.15, 0.06]])
ntsc = np.array([[0.67, 0.33], [0.21, 0.71], [0.14, 0.08]])
dci_p3 = np.array([[0.68, 0.32], [0.265, 0.69], [0.15, 0.06]])

custom_rgb = np.array([[0.7331, 0.2653], [0.1089, 0.8521], [0.1405, 0.0234]])

# Create a plot
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Plot RGB primaries and lines
ax.plot(*srgb.T, 'r', label='sRGB')
ax.plot(*rec709.T, 'g', label='REC.709')
ax.plot(*adobergb.T, 'b', label='AdobeRGB')
ax.plot(*ntsc.T, 'y', label='NTSC')
ax.plot(*dci_p3.T, 'm', label='DCI-P3')
ax.plot(*custom_rgb.T, 'k', label='Custom RGB')

# Fill the gamut triangles
gamuts = [srgb, rec709, adobergb, ntsc, dci_p3,custom_rgb]
colors = ['r', 'g', 'b', 'y', 'm','k']
for i, gamut in enumerate(gamuts):
    polygon = Polygon(gamut, closed=True, edgecolor=colors[i], facecolor='none')
    ax.add_patch(polygon)

# Function to calculate the area of a triangle
def triangle_area(points):
    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]
    return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

# Calculate the area of the custom RGB gamut triangle
custom_area = triangle_area(custom_rgb)

# Calculate and print the area ratio for each color space
gamuts = [srgb, rec709, adobergb, ntsc, dci_p3]
gamut_names = ['sRGB', 'REC.709', 'AdobeRGB', 'NTSC', 'DCI-P3']

for i, gamut in enumerate(gamuts):
    area = triangle_area(gamut)
    area_ratio = custom_area / area
    print(f"Area ratio of Custom RGB to {gamut_names[i]}: {area_ratio:.4f}")
    
# Add labels and legend
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.legend()

# Show the plot
plt.show()
