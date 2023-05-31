Default to square plots (some length x and y axis)


Update for numpy array of coordinates. Example:
```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

coords = np.array([[1389, 2300], [1390, 2301], [1394, 2305], [1404, 2309], [1409, 2304], [1409, 2302], [1408, 2301], [1408, 2300], [1357, 2343], [1352, 2344], [1353, 2329], [1351, 2324], [1348, 2323], [1349, 2304], [1368, 2306], [1374, 2300], [1379, 2299], [1383, 2299], [1389, 2300]], dtype=np.int32)

# Create a polygon and add it to a patch collection
polygon = Polygon(coords, closed=True)
patches = [polygon]

# Create figure and axes
fig, ax = plt.subplots()

# Create a patch collection. With facecolor set to none, this will be a line plot.
p = PatchCollection(patches, facecolor='none', edgecolor='black')

# Add the collection to the plot
ax.add_collection(p)

# Automatically adjust view to the data
ax.autoscale_view()

plt.show()
```


