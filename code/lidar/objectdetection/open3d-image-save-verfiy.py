import open3d as o3d
import numpy as np

# Load your point cloud or create a sample one
# pcd = o3d.io.read_point_cloud("your_point_cloud.ply")
# For this example, let's create a sample point cloud
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(np.random.rand(1000, 3))

# Create a visualizer object
vis = o3d.visualization.Visualizer()
# Create a window, but make it invisible
vis.create_window(visible=False)

# Add the geometry to the visualizer
vis.add_geometry(pcd)

# Set up the camera view
ctr = vis.get_view_control()
ctr.set_front([0, 0, -1])
ctr.set_lookat([0, 0, 0])
ctr.set_up([0, 1, 0])
ctr.set_zoom(0.8)

# Render the image
vis.poll_events()
vis.update_renderer()

# Capture the image and save it
image = vis.capture_screen_float_buffer(False)
o3d.io.write_image("output_image.png", image)

# Destroy the window
vis.destroy_window()

print("Image has been saved as 'output_image.png'")
