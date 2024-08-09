# LiDAR - Light Detection and Ranging

- [LiDAR Overview](#introduction)
- [LiDAR Datasets](#lidar-datasets)
  - [LiDAR Data Annotation & Labeling](#lidar-data-annotation--labeling)
  - [Annotaiton Tools](#annotaiton-tools)
- [LiDAR Devices](#lidar-devices)
  - [Projection Methods](#projection-methods)
  - [Volumetric (Voxel) Methods](#volumetric-voxel-methods)
  - [Raw Point Cloud Methods](#raw-point-cloud-methods)
- [Hands-on Lab](#hands-on-lab)
  - ?
  - ?   
- [LiDAR 3D Object-Detection Methods](#lidar-3d-object-detection-methods)

- [FAQ](#faq)

<img align="right" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRexJXGGhK719BgaGSQI5BouU79zlI-NWCOlql5wlISgRugJOwWsFUU1bUw7HBjD1j52u8" width="30%" height="30%" />

## LiDAR Overview

LiDAR device functions by emitting laser (light) pulses and measuring the duration it takes for these pulses to return after bouncing off of things. This time delay, known as the “time of flight”, is used to calculate precise distances, allowing for the creation of detailed three-dimensional maps of the environment.

- LiDAR sensor readings are given in a set of 3D coordinates called a Point Cloud (PCL), which gives accurate depth information of each point’s surroundings and intensity levels. 
- LiDAR sensors capture millions of data points per second, creating dense point clouds that represent the vehicle's surroundings in rich 3D scenes of environment.
- Point clouds are rich in spatial information, they lack semantic context.
- Point clouds represent the world in 3D. The LiDAR sensor gets the exact (X,Y,Z) position of every impact point.
- LiDARs don’t work well in bad weather conditions. In cases of fog, the lasers can hit it and muddle the scene. Similar to rain drops or dirt.

> RADARs measure the world by sending radio waves, and SONARs sending sound waves, LiDAR do it using light waves.

## LiDAR Datasets
- [10 Lidar Datasets for Autonomous Driving](https://segments.ai/blog/lidar-driving-datasets)
- [5 Best LiDAR Datasets to Learn & Process Point Clouds Data](https://www.thinkautonomous.ai/blog/lidar-datasets/)

### KITTI Dataset

KITTI is a popular computer vision dataset designed for autonomous driving research. It contains a diverse set of challenges for researchers, including object detection, tracking, and scene understanding. The dataset is derived from the autonomous driving platform developed by the Karlsruhe Institute of Technology and the Toyota Technological Institute at Chicago.

The KITTI dataset includes a collection of different sensors and modalities, such as stereo cameras, LiDAR, and GPS/INS sensors, which provides a comprehensive view of the environment around the vehicle. The data was collected over several days in the urban areas of Karlsruhe and nearby towns in Germany. The dataset includes more than 200,000 stereo images and their corresponding point clouds, as well as data from the GPS/INS sensors, which provide accurate location and pose information.

KITTI dataset is a widely used computer vision dataset for training and evaluating algorithms for tasks like object detection, 3D object tracking, and scene understanding. 

- [Explain label file of kitti dataset](https://medium.com/@abdulhaq.ah/explain-label-file-of-kitti-dataset-738528de36f4)
- [KITTI calibration file explained P0–3, R0_rect, Tr_velo_to_cam, and Tr_imu_to_velo](https://medium.com/@abdulhaq.ah/kitti-calibration-file-explained-p0-3-r0-rect-tr-velo-to-cam-and-tr-imu-to-velo-fb47b3f254e6)

[Exploring KITTI Dataset: Visual Odometry for autonomous vehicles](https://medium.com/@jaimin-k/exploring-kitti-visual-ododmetry-dataset-8ac588246cdc)

### LiDAR Data Annotation & Labeling

LiDAR point cloud data requires annotation and labeling to be used for training autonomous vehicles.
- Object Detection: Annotators identify and label objects within the point cloud, including cars, pedestrians, cyclists, and other relevant objects.
- Semantic Segmentation: Assigning a label to each point in the cloud, creating a pixel-wise segmentation of objects and their boundaries.
- Instance Segmentation: Separating individual instances of the same object class, such as distinguishing between different vehicles.
- 3D Bounding Boxes: Defining 3D bounding boxes around objects, including their dimensions, orientation, and location in 3D space.
- Lane and Road Markings: Annotating the road layout, lane markings, and other navigational information.

### Annotaiton Tools

- MOSAIK Suite from MicroVision

### LiDAR Data Formats

| Data Format | Dataset | Details |
|---|---|---|
|bin|KITTI|?|
|LAS |KITTI|?|
XYZ & ASCII
PLY

## LiDAR Hardware

- [OUSTER](https://ouster.com/) formerly Velodyne

## LiDAR Point Cloud Visualization

## LiDAR 3D Object-Detection Methods

Point cloud representation methods divided into,
- Projection
- Voxel
- Raw point cloud.

> Refer to [Multi-modal sensor data fusion approaches]()

### Projection Methods
The projection method transforms the 3D data points into a 2D space using plane (image), spherical, cylindrical, or bird’s-eye view (BEV) projection techniques. The projected data can be processed using the standard 2D methods and regressed to obtain the 3D bounding boxes. It is hard to detect occluded objects in 2D plane representations. 

### Volumetric (Voxel) Methods

The volumetric method discretizes the unstructured and sparse 3D point clouds into a volumetric 3D grid of voxels (volume elements) and uses a series of voxels to represent a 3D point cloud. Voxels are similar to image pixels, but in 3D representation that explicitly provides depth information.

Another limitation of the voxel representation is that it uses 3D convolution for CNN models, increasing the computational cost and involving a trade-off between resolution and memory.

### Raw Point Cloud Methods

The LiDAR data projection and volumetric methods cause spatial information loss during conversion to another domain, so processing point clouds directly are important to keep this spatial information. However, the raw point cloud methods have high sparsity and computational costs due to 3D convolutions.

PointNet is a unified architecture for 3D object classification, part segmentation, and semantic segmentation that directly uses raw point cloud data.

## LiDAR Object Detection Algorithms

Traditional CNNs cannot be applied to Point Clouds. Images have a fixed width and height, it's a rectangular matrix where every pixel lies between 0 and 255, nearby pixels belong to the same object, and it's all flat 2D. Point clouds are 3D structure has no order, no color, and no continuity between the points.

PointNet/PointNet++ is used to extract features, later these features used in 3D Object Detectors.

- MOSAIK Suite from MicroVision – Comprehensive and professional object detection software, including lane detection and free space detection. Sign recognition is slated to release in MOSAIK 2.0 in Sept. 2023. MicroVision Tools Login
- PointNet: A deep learning architecture designed for processing point cloud data directly. PointNet
- PointNet++: An extension of PointNet that handles large-scale point cloud data more effectively. PointNet++
- VoteNet: A model for 3D object detection in point clouds, which can be applied to LiDAR data.

### Voxels Vs. Point Clouds

A voxel is a 3D image. Splits the space (yes, the "air") into 50*50*50 cm grids, and consider these as voxels. You then take the average of the points inside and give it a value. If no point is inside, you consider it empty.

By converting  point cloud to a set of "voxels", we can use 3D Convolutions.

Point and Voxel based approaches are the 2 "main" ways to process point clouds with 3D Deep Learning, 

5 Approaches we can use to process point clouds using 3D Deep Learning, 

## Hands-on Lab

### 1. LiDAR Object Detection Non-ML Algorithms

Processing and analyzing 3D point cloud data, particularly for object detection and segmentation tasks,

Github Repo: https://github.com/AlirezaHabibi1377/3D-LiDAR-Based-Object-Detection

### 2. OpenPCDet

OpenPCDet is a PyTorch-based toolbox for 3D object detection from point cloud. It currently supports multiple state-of-the-art 3D object detection methods with highly refactored codes for both one-stage and two-stage 3D detection frameworks.

Github Repo: https://github.com/open-mmlab/OpenPCDet/

## FAQ

#### How LiDARs estimate Velocity?

LiDAR estimate velocity as difference between two consecutive measurements. RADARs, on the other hand, can estimate the velocity using Doppler effect.

#### How LiDARs point clouds can be stored efficiently?

- Point cloud data is stored in formats like LAS, LAZ, or PLY, with metadata like color or intensity values.
- Data is structured using techniques like octrees or k-d trees. These structures enable faster data access and manipulation.
- Data compression is applied to reduce storage needs while maintaining accuracy.
  
- [Storing Point Clouds in PostgreSQL](https://oslandia.com/wp-content/uploads/2018/05/Lemoine-Oslandia-Pointcloud.pdf)

## References

- https://www.linkedin.com/pulse/auto-annotating-labeling-lidar-data-self-driving-vehicles-bertini/
- https://www.thinkautonomous.ai/blog/voxel-vs-points/
- https://www.thinkautonomous.ai/blog/types-of-lidar/
- https://www.thinkautonomous.ai/blog/how-lidar-detection-works/
