
import open3d.visualization
import open3d
import numpy as np
import matplotlib as plt
import pandas as pd
from dataset.kitti.kitti_dataset import KITTIDataset

def oriented_bbox(pcd, labels, min_points=30, max_points=400):
    """
    Compute oriented bounding boxes (OBBs) for clusters in a point cloud.

    Parameters:
    - pcd (o3d.geometry.PointCloud): Input point cloud.
    - labels (np.ndarray): Array of cluster labels corresponding to each point in the point cloud.
    - min_points (int): Minimum number of points required in a cluster to compute a bounding box.
    - max_points (int): Maximum number of points allowed in a cluster to compute a bounding box.

    Returns:
    - obbs (list): List of axis-aligned bounding boxes for each valid cluster.
    """

    obbs = []

    # Create a list of indices for each cluster
    indices = pd.Series(range(len(labels))).groupby(labels, sort=False).apply(list).tolist()

    # Iterate over each cluster
    for i in range(len(indices)):

        # Select points belonging to the current cluster
        num_points = len(pcd.select_by_index(indices[i]).points)

        # Check if the number of points in the cluster is within the specified range
        if min_points < num_points < max_points:

            # Extract the subset of the point cloud for the current cluster
            sub_cloud = pcd.select_by_index(indices[i])

            # Compute the axis-aligned bounding box for the subset
            obb = sub_cloud.get_axis_aligned_bounding_box()
            obb.color = (0, 0, 0) # Set the color of the bounding box
            obbs.append(obb)

    # Print the number of bounding boxes calculated
    print(f"Number of Bounding Boxes calculated {len(obbs)}")

    return obbs

def ransac(pcd, iterations=10, tolerance=0.25):
    """
    Apply RANSAC to fit a plane to the point cloud and separate inliners from outliners.
    """

    # Perform RANSAC to fit a plane model the point cloud
    plane_model, inliers = pcd.segment_plane(distance_threshold=tolerance, ransac_n=3, num_iterations=iterations)

    # Extract the inlier points (points that fit the plane model)
    inlier_cloud = pcd.select_by_index(inliers)

    # Extract the outlier points (points that do not fit the plane model)
    outlier_cloud = pcd.select_by_index(inliers, invert=True)

    # Paint inliers blue and outliers red for visualization
    outlier_cloud.paint_uniform_color([1, 0, 0]) # R, G, B - Red color for outliers
    inlier_cloud.paint_uniform_color([0, 1, 0])

    return inlier_cloud, outlier_cloud

def dbscan(pcd, eps=0.45, min_points=7, print_progress=False, debug=False):
    """
    Apply DBSCAN clustering to a point cloud.

    Parameters:
    - pcd (o3d.geometry.PointCloud): Input point cloud.
    - eps (float): The maximum distance between two points for them to be considered as in the same neighborhood.
    - min_points (int): The number of points required to form a dense region.
    - print_progress (bool): Whether to print the progress of the clustering.
    - debug (bool): If True, sets the verbosity level to Debug to show detailed logs.

    Returns:
    - pcd (o3d.geometry.PointCloud): Point cloud with colors assigned to each cluster.
    - labels (np.ndarray): Cluster labels for each point.
    """

    # Set the verbosity level for Open3D logging
    verbosityLevel = open3d.utility.VerbosityLevel.Warning
    if debug:
        verbosityLevel = open3d.utility.VerbosityLevel.Debug
    with open3d.utility.VerbosityContextManager(verbosityLevel) as cm:
        
        # Perform DBSCAN clustering on the point cloud
        labels = np.array(pcd.cluster_dbscan(eps=eps, min_points=min_points, print_progress=print_progress))

    # Determine the number of clusters
    max_label = labels.max()
    print(f"point cloud has {max_label + 1} clusters")

    # Generate colors for each cluster using a colormap
    colors = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))
    colors[labels < 0] = 0 # Assign black color to noise points
    pcd.colors = open3d.utility.Vector3dVector(colors[:, :3]) # Set colors in the point cloud

    return pcd, labels

def object_detection_pipeline(pcd: open3d.geometry.PointCloud,  downsample_factor=0.25, iterations=100, tolerance=0.3, eps=0.4, min_points=5, debug=True):
    
    open3d.visualization.draw_geometries([pcd])

    # Apply voxel grid filtering to downsampled point cloud.
    down_sample_pcd = pcd.voxel_down_sample(voxel_size=downsample_factor)
    open3d.visualization.draw_geometries(down_sample_pcd)

    inlier_pts, outlier_pts = ransac(pcd, iterations=iterations, tolerance=tolerance)
    open3d.visualization.draw_geometries([outlier_pts, inlier_pts])


    outlier_pts, labels = dbscan(outlier_pts, eps=eps, min_points=min_points, print_progress=False, debug=debug)
    open3d.visualization.draw_geometries([outlier_pts, inlier_pts])

    bboxes = oriented_bbox(outlier_pts, labels)

    outlier_with_bboxes = [outlier_pts]
    outlier_with_bboxes.extend(bboxes)
    outlier_with_bboxes.append(inlier_pts)

    open3d.visualization.draw_geometries(outlier_with_bboxes)


def visulaization_video(dataset):

    viz = open3d.visualization.Visualizer()
    viz.create_window(False)

    for idx, data in dataset:
        pcd = data.get_lidar_pcl()
        visuals = object_detection_pipeline(pcd)

        for vi in visuals:
            viz.add_geometry(vi)
            viz.update_geometry(vi)

        viz.get_view_control().set_zoom(0.4)
        viz.upate_renderer()
        viz.poll_events()

        viz.capture_screen_image("temp_%4d.png" % idx)

        for vi in visuals:
            viz.remove_geometry(vi)


    viz.destroy_window()





if __name__ == "__main__":

    dataset = KITTIDataset()

    pcd = dataset.get_lidar_pcl(7)

    object_detection_pipeline()