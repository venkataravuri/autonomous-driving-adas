# LiDAR - Light Detection and Ranging

LiDAR sensors capture millions of data points per second, creating dense point clouds that represent the vehicle's surroundings in three dimensions.

The main idea of a LiDAR instrument is that it's built to measure distance directly. They send a light wave to the world, and measure the time it takes to reflect and come back. For more about it refer to, [Types of Lidar](https://www.thinkautonomous.ai/blog/types-of-lidar/)

point clouds are rich in spatial information, they lack semantic context

> RADARs measure the world by sending radio waves, and SONARs sending sound waves, LiDAR do it using light waves.

## Annotation & Labeling LiDAR Data

LiDAR point cloud data requires annotation and labeling to be useful for training autonomous vehicles.

- Object Detection: Annotators identify and label objects within the point cloud, including cars, pedestrians, cyclists, and other relevant objects.
- Semantic Segmentation: Assigning a label to each point in the cloud, creating a pixel-wise segmentation of objects and their boundaries.
- Instance Segmentation: Separating individual instances of the same object class, such as distinguishing between different vehicles.
- 3D Bounding Boxes: Defining 3D bounding boxes around objects, including their dimensions, orientation, and location in 3D space.
- Lane and Road Markings: Annotating the road layout, lane markings, and other navigational information.

Automated annotation and labeling of LiDAR data

### Annotaiton Tools

MOSAIK Suite from MicroVision

## LiDAR Datasets

https://www.cvlibs.net/datasets/kitti/index.php

## LiDAR Object Detection Algorithms

- MOSAIK Suite from MicroVision – Comprehensive and professional object detection software, including lane detection and free space detection. Sign recognition is slated to release in MOSAIK 2.0 in Sept. 2023. MicroVision Tools Login
- PointNet: A deep learning architecture designed for processing point cloud data directly. PointNet
- PointNet++: An extension of PointNet that handles large-scale point cloud data more effectively. PointNet++
- VoteNet: A model for 3D object detection in point clouds, which can be applied to LiDAR data. VoteNe

## Hardware

## 

**References**

- https://www.linkedin.com/pulse/auto-annotating-labeling-lidar-data-self-driving-vehicles-bertini/
- https://www.thinkautonomous.ai/blog/voxel-vs-points/
- https://www.thinkautonomous.ai/blog/types-of-lidar/
