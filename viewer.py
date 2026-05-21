import sys
import nibabel as nib
import pyvista as pv
import numpy as np

# Check argument
if len(sys.argv) < 2:
    print("Usage: python viewer.py <nifti_file>")
    sys.exit(1)

filename = sys.argv[1]

# Load NIfTI file
img = nib.load(filename)
data = img.get_fdata()

print("Loaded:", filename)
print("Shape:", data.shape)

# Create PyVista volume
grid = pv.ImageData()

grid.dimensions = data.shape
grid.spacing = (1, 1, 1)
grid.origin = (0, 0, 0)

grid.point_data["values"] = data.flatten(order="F")

# Create viewer
plotter = pv.Plotter(window_size=[1200, 800])

plotter.add_volume(
    grid,
    cmap="gray",
    opacity="sigmoid"
)

plotter.add_axes()
plotter.show_grid()

plotter.show(title="MedMarvel 3D Viewer")