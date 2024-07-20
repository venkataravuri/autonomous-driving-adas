# LiDAR - Light Detection and Ranging

LiDAR sensor works with light. LiDAR stands for Light Detection And Ranging. LiDAR sensors measure the time it takes for every laser beam hit an obstactcle to reflect and come back. The ouput is a point cloud. 

- LiDAR sensors capture millions of data points per second, creating dense point clouds that represent the vehicle's surroundings in rich 3D scenes of environment.
- Point clouds are rich in spatial information, they lack semantic context.
- Point clouds represent the world in 3D. The LiDAR sensor gets the exact (X,Y,Z) position of every impact point.
- LiDARs don’t work well in bad weather conditions. In cases of fog, the lasers can hit it and muddle the scene. Similar to rain drops or dirt.

> RADARs measure the world by sending radio waves, and SONARs sending sound waves, LiDAR do it using light waves.

#### How LiDARs estimate Velocity?

LiDAR estimate velocity as difference between two consecutive measurements. RADARs, on the other hand, can estimate the velocity using Doppler effect.

Obstacle detection process that generally include folliwng steps.
- Point cloud processing
- Point cloud Segmentation
- Obstacle clustering
- Bounding box fitting.

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

- [OUSTER](https://ouster.com/) formerly Velodyne


## 

**References**

- https://www.linkedin.com/pulse/auto-annotating-labeling-lidar-data-self-driving-vehicles-bertini/
- https://www.thinkautonomous.ai/blog/voxel-vs-points/
- https://www.thinkautonomous.ai/blog/types-of-lidar/
- https://www.thinkautonomous.ai/blog/how-lidar-detection-works/
