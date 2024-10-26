# :camera: Perception
- [Overview]()
- [Conventional Approach]()
    - [Object Detection]()
        - [Measures]()
    - [Semantic Segmentation]()
        - [Measures]()
    - [Object Tracking]()
        - [Measures]()
        - [Kalman Filters]()
        - [Multi Object Trackers]()
- [ML Model based Approaches]()
    - [Bird-Eye-View (BEV)]()
        - [BEVFusion]()
        - [BEVFormer]()
    - [Occupancy Networks]()


## Overview

> Perception refers to the processing and interpretation of sensor data to detect, identify, classify and track objects.

Perception provides information about surroundings, static and movable obstacles. Perception helps car to see the world around itself, as well as recognize and classify the things that it sees.
- The car needs to see and classify traffic lights, pedestrians, road signs, walkways, parking spots, lanes, and much more.
- Not only that, it also needs to know the exact distance between itself and the objects around it.

To achieve such a high level of perception, a self-driving car should use one or more below sensors:
- Camera
- LiDAR
- RADAR

## Camera - Visual Perception

Camera provides vision to the car, enabling multiple tasks like classification, segmentation, and localization.

## LiDAR

LiDAR stands for Light Detection And Ranging, it’s a method to measure the distance of objects by firing a laser beam and then measuring how long it takes for it to be reflected by something.

LiDAR perceives spatial information. 

 LiDAR sensor uses lasers or light to measure the distance of the nearby object. It will work at night and in dark environments, but it can still fail when there’s noise from rain or fog. That’s why we also need a RADAR sensor.

## RADAR

Radio detection and ranging (RADAR) is a key component in many military and consumer applications. It was first used by the military to detect objects. It calculates distance using radio wave signals.

RADARs are highly effective because they use radio waves instead of lasers, so they work in any conditions. 

Radars are noisy sensors, means that even if the camera sees no obstacle, the radar will detect some obstacles.

<img src="https://i0.wp.com/neptune.ai/wp-content/uploads/2022/10/Self-driving-cars-lidar.png?ssl=1" height="50%" width="50%" />
<img src="https://i0.wp.com/neptune.ai/wp-content/uploads/2022/10/Self-driving-cars-radar.png?ssl=1" height="50%" width="50%" />

RADAR data should be cleaned in order to make good decisions and predictions. We need to separate weak signals from strong ones; this is called thresholding. We also use Fast Fourier Transforms (FFT) to filter and interpret the signal. 

Generate the trajectories of objects and bounding box (bbox). The labels on top of a bbox (for example, [21] (0.24)) show the car ID (for example, 21), and the tracking confidence (for example, 0.24), respectively.

Generating the trajectory of an object requires identifying the same object over time even when there are abrupt changes in visual appearance or motion dynamics. 

multi-object trackers (MOT).

simple online and real-time tracker (SORT) that uses a Kalman filter for state estimation and a data association algorithm for target association based on the target bounding boxes from the detector. 

detection errors include partial or double detections and missed detections
 environmental occlusions

 The accuracy of object tracking plays a critical role in robust distance-to-object and object velocity estimations.

vehicle tracking, Pedestrian tracking

Multi-Sensor Kalman Filter



|  object tracker types | ML Models | Technology | Hardware & Devices | Papers |
| --- | --- | --- | --- | --- |
| ? | ? | ? | ? | ? |
| ? | ? | ? | ? | ? |

Sources
- [DRIVE Labs: Tracking Objects With Surround Camera Vision](https://developer.nvidia.com/blog/drive-labs-tracking-objects-with-surround-camera-vision/)

Sensor fusion is the merging of data from at least two sensors. Sensor fusion along with perception enables an autonomous vehicle to develop a 3D model of the surrounding environment that feeds into the vehicle’s control unit.

### Object-Level Fusion

Traditional _object-level fusion_ approach, perception is done separately on each sensor.

<img src="https://leddartech.com/app/uploads/2022/03/figure1.png" width="50%" height="50%" />

This is not optimal because when sensor data is not fused before the system makes a decision, it may need to do so based on contradicting inputs. For example, if an obstacle is detected by the camera but was not detected by the LiDAR or the radar, the system may hesitate as to whether the vehicle should stop.

### Raw Data Sensor Fusion

In a raw-data fusion approach, objects detected by the different sensors are first fused into a dense and precise 3D environmental RGBD model, then decisions are made based on a single model built from all the available information.

<img src="https://leddartech.com/app/uploads/2022/03/figure2.png" height="50%" width="50%" />

Fusing raw data from multiple frames and multiple measurements of a single object improves the signal-to-noise ratio (SNR), enables the system to overcome single sensor faults and allows the use of lower-cost sensors. This solution provides better detections and less false alarms, especially for small obstacles and unclassified objects.

full autonomous driving requires complete, 360-degree surround camera vision.

 surround camera object tracking software currently leverages a six-camera, 360-degree surround perception setup that has no blind spots around the car. The software tracks objects in all six camera images, and associates their locations in image space with unique ID numbers as well as time-to-collision (TTC) estimates.

 feature points which are invariant to rotation and translation are detected by the Harris Corner Detector [1]. Small templates centered on the corner points are tracked by the Lucas-Kanade template tracking algorithm

 Ghost tracks due to objects moving out of the scene are the main cause of false positive braking. Removing them with low latency and without missing any object tracks is a challenging task. 

 variety of seasons, routes, times of the day, illumination conditions, highway, and urban roads.

Surround-view fisheye cameras

Advanced driver assistance systems rely on front and rear cameras to perform ,
1. Automatic cruise control (ACC)
2. and lane keep assist.

## Semantic Segmentation

Segmentation: Uses RANSAC to identify inliers and outliers, fitting a geometric model to the data.
Clustering: Applies DBSCAN to the outliers to group them into clusters.

## Object Tracking

There are two main types of tracking algorithm family: 
1) Single Object Tracker (SOT)
2) Multiple Object Tracker (MOT)
   
Multiple Object Tracking (MOT) refers to the computer vision task that addresses to track every single object of interest in the images or videos. In usual case, MOT integrates a technique known as tracking-by-detection. It entails running a tracker on the set of detections after an independent detector has been applied to images or videos in order to gather expected detections. Unique IDs are then assigned to the bounding box of detected objects and estimation algorithms are used to track moving object’s future actions without losing assigned IDs. As conclusion, the following three steps are shared by the majority of MOT algorithms in high level:
- Detect objects
- Create a unique ID for each detected objects
- Track object as they move, maintaining the assigned IDs.

### real-time object tracking methods.

#### Primitive Techniques

Kalman filters

State Estimation: Kalman filter is applied to to predict the future location of the target by optimally solving the velocity components. Then the detected bounding box in the previous step is used to update the target state.
Target Association: Kalman filter just estimates the object’s new location, which needs to be optimized. 

Hungarian algorithms 

#### Performance Metrics

Metrics for evaluating multi-object tracking (MOT) performance.
- [HOTA](https://jonathonluiten.medium.com/how-to-evaluate-tracking-with-the-hota-metrics-754036d183e1) (Higher Order Tracking Accuracy). 
- MOTA
- IDF1
- Track mAP

### Raw Point Cloud Methods

The LiDAR data projection and volumetric methods cause spatial information loss during conversion to another domain, so processing point clouds directly are important to keep this spatial information. However, the raw point cloud methods have high sparsity and computational costs due to 3D convolutions.


### Voxels Vs. Point Clouds

A voxel is a 3D image. Splits the space (yes, the "air") into 50*50*50 cm grids, and consider these as voxels. You then take the average of the points inside and give it a value. If no point is inside, you consider it empty.

By converting  point cloud to a set of "voxels", we can use 3D Convolutions.

Point and Voxel based approaches are the 2 "main" ways to process point clouds with 3D Deep Learning, 

5 Approaches we can use to process point clouds using 3D Deep Learning, 


### 1. LiDAR Object Detection Non-ML Algorithms

Processing and analyzing 3D point cloud data, particularly for object detection and segmentation tasks,

Github Repo: https://github.com/AlirezaHabibi1377/3D-LiDAR-Based-Object-Detection

### 2. OpenPCDet

OpenPCDet is a PyTorch-based toolbox for 3D object detection from point cloud. It currently supports multiple state-of-the-art 3D object detection methods with highly refactored codes for both one-stage and two-stage 3D detection frameworks.

Github Repo: https://github.com/open-mmlab/OpenPCDet/

## ML-driven Object Detection, Object Classification & Semantic Segmentation

### LiDAR Only Object Detection Algorithms

Traditional CNNs cannot be applied to Point Clouds. Images have a fixed width and height, it's a rectangular matrix where every pixel lies between 0 and 255, nearby pixels belong to the same object, and it's all flat 2D. Point clouds are 3D structure has no order, no color, and no continuity between the points.

|Year|Model|Description|Paper|
|---|---|---|---|
||PointNet|PointNet is a unified architecture for 3D object classification, part segmentation, and semantic segmentation that directly uses raw point cloud data.||
||PointNet++|PointNet++ is used to extract features, later these features used in 3D Object Detectors.||
||VoteNet|||

### Sensor Fusion ML Models

### BEV-based Models

### BEVFusion

<img src="diagrams/bevfusion-1.jpg" />

<img src="diagrams/bevfusion-2.jpg" />

### BEVFormer

<img src="diagrams/bevformer-1.png" />

### Camera Features Extraction
 
For each camera, we use a backbone network (e.g., a ResNet or FPN) to extract features from the 2D images. Let’s assume the output feature map from each camera image has the following properties:
 
Input image resolution: 1280x720
 
Backbone reduces spatial resolution by a factor of 4, so the output feature map has a size of 320x180X256 (width x height x channels).
Now, for each camera, we have feature maps of size 320x180x256. These features are in the image's perspective view, meaning they represent the scene from the camera's point of view.

### LiDAR Features Extraction
 
For the LiDAR, use a point-based or voxel-based backbone (e.g., PointNet, VoxelNet, or a variant) to extract features from the raw point cloud.
 
Assume the point cloud is divided into voxels in 3D space, with a voxel size of 0.2 meters (i.e., each voxel represents a 0.2m x 0.2m x 0.2m cube in the real world).
 
We discretize the point cloud into a BEV feature map with spatial dimensions, where each voxel represents a cell in the BEV grid.



### How Image Features and Point Cloud Features are Geometrically Aligned in BEV Space?

Let’s assume the BEV feature map is 400x400 with 128 channels. This grid represents a 40m x 40m region around the vehicle (i.e., each cell in the BEV grid represents a 0.1m x 0.1m area in the real world).

To fuse camera image features and LiDAR point cloud features in the BEV space, the following steps are typically performed:
 
- **Projecting Camera Features to BEV Space**: Camera images are captured in a 2D perspective space, while the BEV is essentially a top-down 2D view of the 3D world. To align the camera features with the BEV space, a geometric transformation known as **Inverse Perspective Mapping (IPM)** is applied. This transforms the 2D image features into a BEV format by projecting the features onto the ground plane based on the known camera calibration intrinsic and extrinsic parameters and the vehicle's pose.

Each camera covers a specific Field of View (FoV), and the features extracted from each camera are transformed to the BEV format based on the camera’s position, orientation, and coverage area. Since each camera only covers a portion of the 360-degree field, their features are fused together in the BEV space

- **Intrinsic Parameters**: These describe the camera’s focal length and principal point, defining how the 3D world is projected onto the 2D image plane.
- **Extrinsic Parameters**: These describe the camera’s position and orientation relative to the ego vehicle.
 
Using these parameters, we perform Inverse Perspective Mapping (IPM), which transforms 2D image pixels to 3D world coordinates. Specifically, we map each pixel in the camera image (after feature extraction) to a point on the ground plane in the world space. This involves:
 
- Ray-casting from each pixel in the 2D image into the 3D world.
- Assuming that objects are on the ground plane (common assumption for BEV).
- Calculating where each ray intersects the ground plane in the world space, which corresponds to a point in the BEV grid.
 
**Example of Camera Feature Projection**
 
Let’s say the front camera captures a portion of the road in front of the vehicle. After IPM, each feature in the 320x180x256 front camera feature map is projected onto a corresponding location in the BEV space (40m x 40m around the vehicle).
 
The resulting BEV feature map for the front camera would have dimensions that align with the BEV grid, say 400x400x256 (with spatial dimensions matching the LiDAR BEV grid and feature channels from the camera).
 
This process is repeated for all cameras, projecting each camera’s feature map to its respective region in the BEV space. For example:
 
- The front camera features project to the front area of the BEV grid.
- The rear camera features project to the rear area of the BEV grid, and so on.
  
Each camera covers a different FoV, so after projecting all six cameras to the BEV space, we get feature maps that correspond to different regions of the BEV grid. The feature maps from each camera are combined (e.g., through summation, concatenation, or learned fusion mechanisms) to form a unified camera-based BEV feature map.
 
- **Projecting LiDAR Point Cloud to BEV Space**: LiDAR directly provides 3D spatial information, so converting it to BEV is simpler. The LiDAR point cloud is projected onto the ground plane, which naturally fits into a BEV format, where **_each point cloud is mapped to its respective BEV cell or grid location_**.

LiDAR points are already in 3D space, so converting them to BEV space is straightforward. The point cloud is projected directly onto the ground plane (i.e., the XY-plane).
 
Each point is assigned to a voxel or grid cell in the BEV space, based on its  and  coordinates.
 
Feature extraction from the LiDAR point cloud gives us a 400x400x128 BEV feature map.
 
**Alignment in BEV**: After projection, both image and LiDAR features exist in the BEV space, which is effectively a common spatial grid. This allows the features to be aligned at the same resolution and spatial location, where each cell represents a specific location in the world. Features from the camera and LiDAR corresponding to the same physical location can now be fused.
 
#### Fusing Camera and LiDAR Features in BEV Space

Once we have both the camera-based BEV features (e.g., 400x400x256) and the LiDAR-based BEV features (e.g., 400x400x128), we can fuse them to form a comprehensive representation of the environment.

Fusion Techniques: The features from both sensors can be fused using techniques like:
 
- **Concatenation**: Simply concatenating the camera and LiDAR features along the channel dimension, resulting in a BEV feature map of size 400x400x(256+128) = 400x400x384.
- **Summation or Weighted Fusion**: Taking a weighted sum of the camera and LiDAR features at each grid cell in the BEV space.
- **Learned Attention Mechanisms**: Using neural networks (e.g., attention layers) to learn how to weight and combine the features from the two modalities.

#### Generating Semantic Segmentation from BEV Features
 
**Segmentation Head**: 

Once the fused BEV feature map is generated (e.g., 400x400x384), it is passed through a segmentation head (typically a convolutional network) to produce a semantic segmentation map.

Segmentation head (usually a convolutional neural network or a fully connected network) processes the fused BEV features to predict class labels for each BEV grid cell. 

Output Segmentation Map: The final output would be a 400x400 BEV map where each cell is assigned a class label (e.g., road, vehicle, pedestrian).
 
The segmentation map can then be projected back to the image space if needed, or used in the BEV space for navigation, object detection, or planning.
 
In summary, the process of fusing camera and LiDAR features in a BEV space for object detection and semantic segmentation involves _geometric transformations, sensor calibration, feature fusion, and projection techniques_ to generate a unified perception of the environment.

This process aligns and fuses image and point cloud features in the BEV space, allowing for comprehensive environmental perception around the ego vehicle.

**Summary of Dimensions**:
 
- Camera images are 1280x720.
- Camera feature maps after backbone: 320x180x256.
- LiDAR point cloud projected to BEV: 400x400x128.
- Fused BEV feature map: 400x400x384 (after concatenating camera and LiDAR features).
- Final BEV semantic segmentation: 400x400, where each cell represents a class label (e.g., road, vehicle).

#### Does BEVfusion or BEVformer capable of detecting road lane markings, lane width, lane joins and more. 

BEVFusion and BEVFormer are state-of-the-art machine learning models that primarily focus on perceiving the environment in a bird’s-eye view (BEV) representation. While they excel at tasks like object detection (e.g., detecting vehicles, pedestrians), semantic segmentation, and sensor fusion, their capabilities related to road lane detection and related attributes (like lane width, lane joins, and more) depend on how they are configured and trained.
 
1. BEVFusion and BEVFormer: Focus and Key Tasks
 
Both BEVFusion and BEVFormer transform sensor data (from LiDAR, cameras, and potentially radar) into a bird's-eye view to perform tasks that are highly relevant for autonomous driving, such as:
 
Object Detection: Detecting cars, pedestrians, cyclists, and more in 3D space.
 
Semantic Segmentation: Understanding the different elements of the environment (e.g., road, sidewalks, vegetation, vehicles) in a top-down view.
 
Sensor Fusion: Integrating multi-modal sensor data (e.g., LiDAR, cameras) for enhanced perception, allowing for accurate detection, classification, and localization of objects.
 
 
2. Lane Detection in BEV Models
 
Detecting road lanes, lane width, lane merges, and more in a BEV model can be achieved, but it depends on the task formulation, data labeling, and training approach. Here's how BEVFusion and BEVFormer might handle lane detection:
 
a. Road Lane Markings and Lane Segmentation:
 
Semantic Segmentation: Both BEVFusion and BEVFormer can be trained to include road lane markings as a class in semantic segmentation. This would allow the model to not only identify vehicles and pedestrians but also recognize lane lines, road boundaries, crosswalks, etc.
 
BEV Representation: Since the output of both models is a bird's-eye view (top-down) of the scene, they are particularly well-suited to detecting lane markings, which naturally align with the top-down perspective of the road.
 
 
b. Lane Width and Lane Joins:
 
Lane Width: While not a direct detection task, lane width could be inferred by analyzing the segmented lane markings in the BEV output. The model could measure the pixel width of the lane marking segments and convert it into real-world distances, since BEV models are typically calibrated to real-world dimensions.
 
Lane Joins and Merges: Lane joins and merges can be identified if the model is trained to recognize lane connectivity patterns in the BEV. By detecting adjacent lane markings, the model could infer when lanes are splitting (diverging) or joining (merging).
 
 
3. Capability of BEVFusion and BEVFormer for Lane Detection
 
BEVFusion:
 
Multi-modal Fusion for Lane Detection: BEVFusion, which integrates data from LiDAR and cameras, is particularly strong at fusing visual features from cameras (which capture lane markings) and geometry from LiDAR (which can capture road surface features and curbs). This makes it possible to train BEVFusion models to detect road lanes, their markings, and geometry.
 
Road Layout Understanding: In autonomous driving, the ability to understand the entire road layout is critical, and BEVFusion’s BEV output makes it easier to perceive lane geometry, road boundaries, and lane transitions.
 
 
BEVFormer:
 
Temporal Consistency for Lane Understanding: BEVFormer excels at incorporating temporal information, which helps maintain lane continuity across frames, making it useful for detecting and tracking lane features like lane markings over time, even as the vehicle moves.
 
Lane Marking and Geometry: BEVFormer, like BEVFusion, can potentially detect road lane markings by being trained on labeled data that includes lane-related classes. The temporal nature of the model ensures that dynamic changes in lane structure, such as merging or splitting lanes, can be handled effectively over multiple frames.
 
 
4. Additional Factors for Lane Detection
 
Training Data: To detect lanes, the model must be trained with data that includes labeled lane information (e.g., lane markings, lane width, merging lanes). Many datasets used for autonomous driving include such annotations.
 
Post-processing Algorithms: For specific tasks like calculating lane width or identifying lane joins, post-processing algorithms can be applied to the BEV output to measure and analyze lane geometry.
 
 
5. Comparison with Other Lane Detection Systems
 
Traditional lane detection algorithms, such as those using monocular cameras or LiDAR-only systems, focus on detecting lane markings directly from raw sensor data (like visual lane detection from cameras). BEVFusion and BEVFormer, on the other hand, transform the sensor data into a unified BEV representation, which offers a more comprehensive understanding of the entire road scene, including lanes, objects, and the overall road layout.
 
 
---
 
Conclusion: Lane Detection Capabilities
 
While BEVFusion and BEVFormer are primarily designed for object detection and scene understanding in a bird's-eye view, they are capable of detecting road lane markings, lane width, lane merges, and more, provided they are trained with the appropriate data and configured for these tasks. These models can:
 
Detect road lane markings and infer lane structure via semantic segmentation.
 
Analyze lane width and lane joins by processing the BEV output.
 
Leverage multi-sensor data (e.g., cameras and LiDAR) to improve lane detection robustness and precision.
 
 
However, specific lane detection functionality may need additional training and post-processing steps tailored to lane geometry and connectivity, depending on the needs of the autonomous driving system.


Late fusion in the context of combining LiDAR and camera data for autonomous driving refers to fusing the results of independent detection processes from each sensor at a higher, decision-making level, rather than fusing the raw or mid-level features from both sensors earlier in the perception pipeline.
 
In late fusion, object detection is performed separately for both LiDAR and camera data, and the results (e.g., detected bounding boxes) are combined after the detection stage. This method allows each sensor to operate with its own specialized detection algorithm and compensates for the strengths and weaknesses of each sensor type.
 
How Late Fusion Works: Step-by-Step Example
 
Let’s break it down using a concrete example of detecting and tracking vehicles and pedestrians on the road in an autonomous driving scenario.
 
 
---
 
Step 1: Independent Object Detection for Each Sensor
 
1. LiDAR Detection:
 
Process: LiDAR generates a 3D point cloud of the environment.
 
Object Detection: A LiDAR-based object detection algorithm (e.g., clustering, DBSCAN, or deep learning methods) processes the point cloud to detect objects like vehicles, pedestrians, or obstacles. The result is a set of 3D bounding boxes around detected objects, along with their estimated positions (x, y, z coordinates).
 
Strengths: LiDAR provides accurate depth and 3D localization, allowing precise measurements of the distance and size of objects.
 
 
Example result:
 
Detected Object 1: 3D bounding box with coordinates (x1, y1, z1), size (w1, h1, l1), object type: unknown.
 
Detected Object 2: 3D bounding box with coordinates (x2, y2, z2), size (w2, h2, l2), object type: unknown.
 
 
 
2. Camera Detection:
 
Process: A camera captures a 2D image of the scene.
 
Object Detection: A 2D object detection model (e.g., YOLO, Faster R-CNN) processes the image to detect objects like vehicles and pedestrians, resulting in 2D bounding boxes in the image frame, along with class labels (car, pedestrian, etc.) and confidence scores.
 
Strengths: Cameras provide rich visual information and object classification (identifying what the object is), such as recognizing a car, a pedestrian, or a cyclist.
 
 
Example result:
 
Detected Object 1: 2D bounding box (x1', y1'), object class: "car", confidence: 0.95.
 
Detected Object 2: 2D bounding box (x2', y2'), object class: "pedestrian", confidence: 0.85.
 
 
 
 
 
---
 
Step 2: Align the Sensor Data (Coordinate Transformation)
 
Before combining the detections from LiDAR and the camera, the two data sets need to be aligned in a common coordinate system. This requires calibration between the LiDAR and camera:
 
Intrinsic Calibration: This deals with the camera’s internal parameters (e.g., focal length, lens distortion).
 
Extrinsic Calibration: This aligns the positions of the camera and LiDAR in relation to each other, creating a transformation matrix to map LiDAR points to the camera’s 2D image plane.
 
 
Once calibrated, you can project the 3D LiDAR points into the camera image, and vice versa, allowing you to correlate objects detected in both sensor modalities.
 
 
---
 
Step 3: Fusion of Detection Results
 
After each sensor independently detects objects, late fusion combines these results at the decision-making stage. There are a few common methods to achieve this:
 
Method 1: Object Matching via Spatial Proximity
 
The 3D bounding boxes from LiDAR detection and the 2D bounding boxes from camera detection are compared by projecting the 3D LiDAR bounding boxes onto the 2D image plane.
 
Association is done by checking how closely the projected 3D bounding box aligns with a 2D bounding box from the camera.
 
If the projection of a LiDAR-detected object onto the image closely overlaps with a camera-detected object, the two detections are considered to represent the same object.
 
 
Example:
 
The 3D bounding box for Object 1 from the LiDAR, when projected onto the image plane, overlaps significantly with the 2D bounding box of the "car" detected by the camera. This suggests that Object 1 is indeed a car.
 
The 3D bounding box for Object 2 from the LiDAR, when projected onto the image plane, overlaps with the 2D bounding box of a "pedestrian" detected by the camera. Hence, Object 2 is classified as a pedestrian.
 
 
Method 2: Confidence Score Fusion
 
Each sensor's detection comes with a confidence score indicating how certain the system is about the detection (e.g., how confident YOLO is that a detected object is a pedestrian).
 
In late fusion, the confidence scores from both LiDAR and camera detections can be weighted and combined to improve decision-making.
 
For example, if the LiDAR system is 90% confident that an object exists in a certain location, but the camera-based YOLO detector is only 60% confident about detecting a car at that position, the system can combine the confidence scores (e.g., using a weighted average) to make a more robust detection decision.
 
 
 
---
 
Step 4: Decision and Classification
 
After associating the objects detected by the LiDAR and camera:
 
Final Decision: The system combines the classification information from the camera (which has better object recognition capabilities) and the localization from LiDAR (which provides accurate 3D positions and sizes of objects).
 
This fusion gives a complete and more reliable representation of each object, including its type (car, pedestrian) and its 3D position and size.
 
 
Example of fused results:
 
Object 1: Detected as a "car" with high confidence, located at coordinates (x1, y1, z1), with bounding box size (w1, h1, l1).
 
Object 2: Detected as a "pedestrian" with medium confidence, located at coordinates (x2, y2, z2), with bounding box size (w2, h2, l2).
 
 
 
---
 
Step 5: Feeding Fused Results into Kalman Filter for Tracking
 
Once the objects have been detected and classified using late fusion, their positions and attributes (e.g., 3D bounding boxes, class labels) are used as inputs for a Kalman filter to track these objects across time.
 
Kalman Filter Input: For each object, the Kalman filter takes the fused bounding box coordinates (x, y, z) and class label and predicts the next state of the object in terms of its position and velocity.
 
Tracking: As new detections come in at each time step, the Kalman filter updates the object's position and motion model, allowing for robust tracking of objects as they move, even if one sensor fails to detect an object in a particular frame.
 
 
The Kalman filter helps:
 
Smooth object motion by predicting positions between detections.
 
Handle missing detections when an object is temporarily occluded or one sensor misses it.
 
Track multiple objects by associating their positions over time.
 
 
 
---
 
Advantages of Late Fusion
 
1. Leverages Sensor Strengths:
 
LiDAR gives accurate 3D localization, while cameras excel at classification (object recognition).
 
Late fusion allows each sensor to work independently in its specialized domain, providing the best of both worlds.
 
 
 
2. Improves Reliability:
 
If one sensor (e.g., LiDAR) misses an object or has low confidence, the other sensor (camera) can still provide useful information, leading to more robust detection.
 
 
 
3. Increased Flexibility:
 
Late fusion allows you to integrate different algorithms for each sensor and does not require combining raw sensor data early in the pipeline, making the system more modular.
 
 
 
 
 
---
 
Example Use Case in Autonomous Driving
 
In an autonomous vehicle navigating a busy city street:
 
Camera Detection: YOLO detects a pedestrian in the camera's image with 85% confidence but lacks depth information.
 
LiDAR Detection: LiDAR independently detects a moving object (cluster of points) at 12 meters away, producing a 3D bounding box but without classifying what the object is.
 
Late Fusion: By associating the 2D camera detection with the 3D LiDAR detection, the system confirms the object is a pedestrian at a distance of 12 meters and updates the Kalman filter to track the pedestrian's movement in 3D space.
 
 
In this way, late fusion creates a more reliable and precise detection and ensures that the object is accurately tracked as the vehicle continues moving forward.




---------------

#### In traditional and legacy autonomous driving system, How LiDAR point cloud is used for object detection independently. I know YOLO can be used object detection in images. How LiDAR information and image based generated data combined. How this is fed into Kalman filters for tracking?
 


LiDAR-Based Object Detection in Traditional Autonomous Driving Systems
 
In legacy or traditional autonomous driving systems, LiDAR (Light Detection and Ranging) plays a crucial role in perceiving the environment because of its ability to provide accurate 3D distance measurements of surrounding objects. Here's how LiDAR point cloud data is used for object detection:
 
1. LiDAR Point Cloud Basics
 
LiDAR sensors emit laser pulses and measure the time it takes for the pulses to return after hitting an object. This generates a dense point cloud, which is a collection of 3D points representing the objects and terrain in the sensor’s field of view. Each point in the cloud has:
 
3D coordinates (x, y, z), representing its position in space.
 
Intensity value, representing the strength of the returned laser pulse.
 
 
2. LiDAR Point Cloud Processing for Object Detection
 
The raw point cloud data is processed to detect objects by identifying clusters of points that represent individual objects. This is done through various steps:
 
Point Cloud Preprocessing: This involves removing noise, ground points (e.g., roads), and redundant points to focus on potential objects.
 
Clustering: Algorithms like DBSCAN (Density-Based Spatial Clustering of Applications with Noise) or Euclidean Clustering are applied to group nearby points into clusters that likely represent discrete objects (e.g., vehicles, pedestrians).
 
Bounding Box Fitting: Once clusters are identified, 3D bounding boxes are fitted around each cluster. These boxes represent the extent of detected objects in the 3D space.
 
Feature Extraction: Additional features like the shape, size, and orientation of the bounding box, as well as the object's motion, can be derived to classify and distinguish between different object types (e.g., cars vs. pedestrians).
 
 
LiDAR-based object detection systems are good at identifying objects' precise locations and sizes but may struggle with object classification (i.e., identifying what the object is) without additional data.
 
Image-Based Object Detection with YOLO
 
For image-based object detection, deep learning models like YOLO (You Only Look Once) are commonly used. YOLO takes a 2D camera image as input and produces:
 
2D bounding boxes around detected objects.
 
Object class labels (e.g., vehicle, pedestrian).
 
Confidence scores for each detection.
 
 
While YOLO can provide detailed classification and detection in 2D, it lacks depth information (i.e., how far the object is from the vehicle), which is where LiDAR becomes crucial.
 
Combining LiDAR and Image Data for Object Detection
 
Sensor fusion combines data from multiple sensors to leverage the strengths of each, resulting in a more robust object detection system. Here's how LiDAR and image data are typically combined:
 
1. Extrinsic and Intrinsic Calibration
 
Before fusing data, it's necessary to perform calibration between the LiDAR and the camera. Calibration establishes a transformation matrix that maps 3D LiDAR points into the 2D image plane of the camera.
 
Intrinsic calibration refers to the internal parameters of the camera (e.g., focal length, lens distortion).
 
Extrinsic calibration aligns the relative positions and orientations of the LiDAR and camera.
 
 
Once calibrated, 3D LiDAR points can be projected onto the 2D image plane.
 
2. Fusion Methods
 
There are several methods for combining LiDAR and camera data:
 
Early Fusion: Raw data from LiDAR and cameras are combined at the sensor level. For example, LiDAR point clouds are projected onto the 2D image, and both the point cloud and pixel data are fed into a neural network for joint object detection.
 
Mid-Level Fusion: LiDAR-based object detection and image-based detection are done separately, and their results are combined. For instance:
 
Use YOLO to detect objects in the 2D image (with 2D bounding boxes).
 
Use LiDAR point clouds to detect objects in 3D space (with 3D bounding boxes).
 
Fuse these results by projecting the 3D LiDAR data onto the 2D image, or by correlating detected objects in both modalities. This improves detection accuracy and helps assign depth to the objects detected by the camera.
 
 
Late Fusion: Object detections from LiDAR and camera are processed independently, and the results are combined at a decision-making stage. For example, after YOLO detects objects in the image, the system might confirm or refine those detections using LiDAR data, improving localization or classification.
 
 
3. How LiDAR and Image Fusion Improves Detection
 
LiDAR provides precise 3D localization (depth information), allowing the system to determine how far away objects are.
 
Cameras provide rich visual information (color, texture) and better object classification.
 
 
Together, these complementary data sources lead to more reliable object detection, where LiDAR provides geometry and localization, and cameras add classification and visual detail.
 
Feeding LiDAR and Image Fusion into Kalman Filters for Object Tracking
 
Once objects are detected from the combined LiDAR and image data, tracking those objects across time is crucial for autonomous driving. This is where Kalman filters come into play.
 
1. Object Detection as Input to Kalman Filter
 
After object detection, each detected object is represented by a bounding box (from the image or LiDAR) and additional features (e.g., class labels, position, velocity). These detections become the measurements for the Kalman filter, which tracks the objects over time.
 
LiDAR provides 3D bounding box coordinates (position and size) in the real-world space (e.g., x, y, z).
 
Cameras provide 2D bounding box coordinates (position in the image plane), along with class labels (e.g., pedestrian, car).
 
 
Both sets of information can be fused to form a comprehensive detection for each object, combining spatial accuracy from LiDAR and visual details from the camera.
 
2. Tracking with Kalman Filter
 
The Kalman filter tracks each object by maintaining a state vector for each detected object, which typically includes:
 
Object's position (e.g., x, y, z from LiDAR)
 
Velocity (inferred from motion between frames)
 
Size (width, height, depth of the 3D bounding box)
 
 
Prediction and Update Cycle:
 
Prediction: At each time step, the Kalman filter predicts the object's next position based on its current velocity and motion model.
 
Update: When new measurements (bounding boxes) arrive from the sensor fusion system (LiDAR and camera), the Kalman filter updates its estimate of the object's position and velocity, correcting any discrepancies between the prediction and the measurement.
 
 
3. Advantages of Using Kalman Filters After Sensor Fusion
 
Robust Tracking: By integrating both LiDAR and camera data, the Kalman filter can track objects even if one of the sensors temporarily fails (e.g., a camera cannot detect objects in poor lighting, or LiDAR misses objects due to occlusion).
 
Handling Missing Detections: If an object is not detected in one frame, the Kalman filter can still predict its position, based on its motion in previous frames.
 
Smooth Object Motion: Kalman filters provide a smoothed estimate of an object's motion over time, reducing the effect of noisy measurements.
 
 
Summary of the Process
 
1. LiDAR Object Detection: LiDAR point clouds are processed to detect objects by clustering points and fitting 3D bounding boxes around them.
 
 
2. Camera-Based Detection (YOLO): YOLO or another detection model identifies objects in 2D images with bounding boxes and class labels.
 
 
3. Fusion of LiDAR and Camera Data: LiDAR point clouds and 2D image data are fused through various methods (early, mid, or late fusion) to improve object detection by combining depth and visual information.
 
 
4. Tracking with Kalman Filters: The detected objects (from fused LiDAR and camera data) are fed into Kalman filters, which track the position and velocity of each object across frames, ensuring continuous and reliable tracking.
 
 
 
This combined approach enhances the perception system’s ability to detect, classify, and track objects in real-time, a critical requirement for autonomous driving.

-----------------------------------------

#### Does BEVfusion or BEVFormer ML models includes object tracking or limited to object detection, semantic segmentation and beyond?
 

BEVFusion and BEVFormer are state-of-the-art machine learning models primarily designed for 3D perception tasks in autonomous driving, focusing on Bird's Eye View (BEV) representation. They extend beyond traditional object detection and semantic segmentation to provide a unified spatial understanding of the environment by fusing multi-modal sensor data, but they are not inherently designed for object tracking.
 
Here’s a breakdown of their roles in object detection, semantic segmentation, and other tasks, and whether they handle object tracking:
 
 
---
 
1. BEVFusion
 
BEVFusion is a model that fuses multiple sensor modalities (e.g., LiDAR, camera, radar) to generate a unified Bird’s Eye View (BEV) representation of the scene. It is primarily used for tasks like:
 
3D Object Detection: Detects objects such as vehicles, pedestrians, and cyclists from a BEV perspective, using multi-modal inputs to enhance the understanding of object location and orientation.
 
Semantic Segmentation: Classifies each pixel or voxel in the BEV representation into different semantic categories (e.g., road, sidewalk, vehicle, building).
 
 
Key Characteristics:
 
Multi-sensor fusion: BEVFusion combines different sensor inputs, including LiDAR, radar, and cameras, which helps it produce more accurate and robust BEV representations for detection and segmentation.
 
 
Object Tracking:
 
No inherent object tracking: BEVFusion itself is limited to object detection and segmentation tasks. It does not handle the temporal aspect of tracking objects across multiple frames. The purpose of BEVFusion is to generate accurate detection and semantic understanding of the current frame.
 
 
To incorporate tracking, BEVFusion would typically be integrated with a separate tracking algorithm (e.g., DeepSORT or Kalman filter-based trackers), which would handle the association of objects across frames over time.
 
 
---
 
2. BEVFormer
 
BEVFormer is another advanced model specifically designed for 3D perception tasks in autonomous driving, focused on representing and reasoning about the environment in a BEV format. It excels at fusing information from sensors and providing BEV outputs.
 
Tasks BEVFormer Handles:
 
3D Object Detection: Detects objects in a BEV format using inputs from cameras or LiDAR. BEVFormer can capture spatial information in both image and BEV space for accurate object detection.
 
Semantic Segmentation: Performs semantic segmentation in the BEV space, allowing it to classify parts of the scene into categories like roads, lanes, and different types of obstacles.
 
Spatio-temporal Features: One key strength of BEVFormer is that it includes a temporal component, allowing the model to reason over multiple frames of data, which is crucial for tasks that require understanding the dynamic nature of the environment.
 
 
Object Tracking:
 
No direct object tracking: Despite its ability to handle temporal data, BEVFormer is primarily focused on tasks like object detection and segmentation. While it captures temporal information and can reason about changes over time, it does not perform object tracking (i.e., it doesn't assign unique IDs to objects and follow them over time across frames).
 
 
BEVFormer could potentially support tracking indirectly by making use of the temporal aspects it captures, but explicit tracking, such as associating objects from frame to frame, is typically done by a separate object tracking module.
 
 
---
 
Differences in Object Tracking Capabilities
 
Both BEVFusion and BEVFormer focus primarily on 3D object detection, semantic segmentation, and BEV-based scene understanding.
 
Neither model natively supports object tracking. Object tracking requires the model to assign unique identities to objects and follow them as they move across frames, which is not their primary design focus.
 
These models work with single-frame or temporal data, but multi-frame object tracking usually involves using a different system or algorithm (like Kalman filters or DeepSORT) to handle temporal consistency and identity assignment over time.
 
 
 
---
 
Where Are They Used in the Perception Pipeline?
 
In autonomous driving perception systems:
 
BEVFusion and BEVFormer are used in the early to mid-stages of the perception pipeline for object detection, semantic segmentation, and understanding the scene layout in 3D. They provide a high-level spatial understanding of objects and their surroundings.
 
For object tracking, these models would typically be followed by a dedicated tracking algorithm (e.g., Kalman filter, DeepSORT) that takes the detected objects and assigns them unique IDs to track them over time.
 
 
Summary:
 
BEVFusion and BEVFormer are powerful models for 3D object detection, semantic segmentation, and BEV-based scene understanding.
 
They do not perform object tracking directly but provide the necessary inputs (like object positions and classifications) for tracking systems to process.
 
Object tracking would need to be handled by additional algorithms designed specifically for associating objects across frames.

#### Explain me deepsort covering aaspects of object detection, bounding boxes, how it integrates with kalman filters, how multi object tracking is done. What are the inputs and outputs. What stage it is used in AV perception scenarios.

DeepSORT (Deep Simple Online and Realtime Tracking) Overview
 
DeepSORT is an advanced version of the SORT (Simple Online and Realtime Tracking) algorithm, designed for multi-object tracking (MOT). It enhances the basic SORT approach by adding appearance features from a deep learning model, which helps to maintain the identity of objects as they move through a scene. DeepSORT integrates object detection, bounding box association, and Kalman filtering to track multiple objects in a scene in real-time.
 
Object Detection in DeepSORT
 
Object detection is the first step in the DeepSORT pipeline. This involves detecting objects in the environment, typically using a pre-trained object detection model such as:
 
YOLO (You Only Look Once)
 
SSD (Single Shot Detector)
 
Faster R-CNN (Region-based Convolutional Neural Network)
 
 
These models produce bounding boxes around the detected objects, which define the object's location and size in the image. The bounding boxes are associated with each object's class (e.g., pedestrian, car, cyclist) and confidence score (how sure the detector is about the object being present).
 
Bounding Boxes and Object Tracking
 
Once objects are detected and their bounding boxes are identified, DeepSORT uses the detected bounding boxes as inputs for the tracking system. These bounding boxes provide:
 
Position (x, y coordinates of the top-left corner of the box)
 
Width and height (to estimate the object's size)
 
Confidence score from the detection model.
 
 
At each time step, new bounding boxes are produced by the object detector, and these need to be associated with the existing tracked objects.
 
Integration with Kalman Filters
 
DeepSORT integrates a Kalman filter to predict and update the state of each tracked object over time. Here’s how this works:
 
1. State Vector: For each object, the Kalman filter maintains a state vector that contains information about the object's position and velocity in the 2D image space. The state might include:
 
Object's x, y position
 
Velocity in x, y directions
 
Width and height of the bounding box
 
 
 
2. Prediction Step: The Kalman filter uses a motion model (usually a constant velocity model) to predict the future position of each object based on its current state. This is particularly useful when an object might temporarily disappear from view (occlusion) or when detection is missed for a few frames.
 
 
3. Update Step: After predicting the object's next state, the Kalman filter receives new measurements from the object detector (new bounding box locations). The filter then updates the predicted state with these measurements, refining the object's position and velocity. This recursive update helps in keeping the track consistent even with noisy detections.
 
 
 
The Kalman filter helps by providing a smoother, more accurate estimate of object movement and compensates for missing or imperfect detections.
 
Multi-Object Tracking (MOT) in DeepSORT
 
One of the key challenges in multi-object tracking is data association, or how to assign new detections (bounding boxes) to the correct tracked object. DeepSORT handles this by combining:
 
1. Kalman filter predictions: Predicting the future positions of objects to narrow down the search area for associations.
 
 
2. Appearance features: DeepSORT improves the original SORT algorithm by incorporating a deep learning-based appearance descriptor (usually a CNN). This appearance model extracts features from each object (from its bounding box), which are then used to measure similarity between detections and previously tracked objects.
 
 
 
This similarity metric helps associate detections with the correct object, even when objects cross paths, overlap, or when the Kalman filter alone might not be sufficient to distinguish between them.
 
Data Association (Matching Bounding Boxes)
 
DeepSORT uses a combination of spatial (position-based) and appearance-based features to solve the data association problem:
 
1. Hungarian Algorithm: This algorithm is used for solving the assignment problem, where new detections (bounding boxes) are matched with predicted object positions based on their spatial proximity.
 
 
2. Appearance Metric: In addition to spatial matching, DeepSORT uses a cosine similarity metric on the appearance features to associate new detections with previously tracked objects. This prevents identity switches (i.e., when the identity of an object is wrongly transferred to another).
 
 
 
Inputs to DeepSORT
 
The inputs to DeepSORT are:
 
Bounding boxes from an object detector (e.g., YOLO or Faster R-CNN), including:
 
Coordinates (x, y, width, height)
 
Class label (e.g., pedestrian, car, etc.)
 
Confidence score (how likely it is that the object is correctly detected)
 
 
Appearance features from a pre-trained deep learning model, extracted from the detected object's bounding box.
 
 
Outputs of DeepSORT
 
The outputs of DeepSORT are:
 
Tracked objects: Each object being tracked has a unique ID, and its updated bounding box coordinates (x, y, width, height) are output at each time step.
 
State information: For each object, the Kalman filter's predicted state (position, velocity) is available.
 
Appearance feature vectors: These are used internally to maintain the identity of objects, especially in crowded or complex environments.
 
 
Temporal Tracking and Occlusion Handling
 
DeepSORT is designed to handle temporal aspects in object tracking. Since Kalman filters predict the next state of an object based on its previous state, DeepSORT is robust to short-term occlusions (when an object is briefly blocked from view). Even if the object is not detected for a few frames, DeepSORT can continue predicting its movement and recover its position once it reappears. The appearance model also helps in correctly re-identifying the object after occlusion.
 
Role in Autonomous Vehicle (AV) Perception Pipeline
 
In autonomous vehicles, DeepSORT would be used in the tracking stage of the perception pipeline. Here’s a typical flow:
 
1. Sensor Fusion: Data from various sensors (camera, LiDAR, radar) is first combined to create a robust perception of the environment.
 
 
2. Object Detection: After sensor fusion, the detection module identifies and localizes objects of interest (e.g., pedestrians, vehicles) in the sensor data (usually in the form of 2D bounding boxes).
 
 
3. Object Tracking: This is where DeepSORT comes into play. The tracking system receives bounding boxes from the object detector and uses DeepSORT to assign unique IDs to each detected object and track their movement over time.
 
 
4. Prediction: The tracked objects are then used for motion prediction, allowing the vehicle to anticipate their future positions, which is crucial for safe path planning and navigation.
 
 
 
Summary
 
Object Detection: DeepSORT uses detections from pre-trained models like YOLO or Faster R-CNN, which provide bounding boxes around objects in each frame.
 
Kalman Filters: Integrated to predict the state of tracked objects (position, velocity), providing robustness to missed detections or occlusions.
 
Appearance Model: A deep learning-based model extracts appearance features to maintain object identities even in complex scenarios.
 
Multi-Object Tracking: Uses the combination of motion (Kalman filter) and appearance features to track multiple objects, ensuring accurate association across frames.
 
Outputs: Tracked objects with unique IDs, positions, and velocities are the key outputs, along with continued tracking over time.
 
Stage in AV Perception: DeepSORT is used after object detection in the perception stage of the AV pipeline, ensuring that multiple objects are tracked accurately across frames for better motion prediction and decision-making.
 
 
DeepSORT is efficient, scalable, and can track multiple objects in real-time, making it suitable for complex environments like autonomous driving.

#### In autonomous driving, Does Kalman filters are used to track surrounding objects? How Kalman filters work? What are the inputs to Kalman filters? Can it take image features and LiDAR point cloud features? What is the output of Kalman filters? To work with Kalman filters, one need to detect objects before with bounding boxes? How temporal aspects works with Kalman filters? What are different libraries for Kalman filters? If we want to convert Kalman filters kind of functionality into ML model, how this can be done? Suggest popular object tracking ML models?
 
Don't answer me as Q&A. Give me detail notes addressing above questions, include additional context where needed.


Kalman Filters in Autonomous Driving for Object Tracking
 
Kalman filters are extensively used in autonomous driving to track surrounding objects like vehicles, pedestrians, and obstacles. They are popular due to their efficiency in estimating the state of a moving object in a noisy environment. Kalman filters use a predictive approach, where they continuously update their estimates based on measurements and predict the object's future state, accounting for uncertainty.
 
Working of Kalman Filters
 
Kalman filters operate based on a recursive two-step process:
 
1. Prediction: Using the previous state estimate and a motion model (like the object's speed and direction), the Kalman filter predicts the current state of the object.
 
 
2. Update: The filter corrects the predicted state using new measurements from sensors (like LiDAR, radar, or camera) and updates the state estimate to minimize the error.
 
 
 
The Kalman filter assumes that both the noise in the measurements and the system dynamics can be modeled as Gaussian distributions. It produces an optimal estimate of the object's state (position, velocity, etc.) by minimizing the mean squared error.
 
Inputs to Kalman Filters
 
The Kalman filter's main inputs are:
 
State vector: This typically represents the object's position, velocity, acceleration, etc., in a multidimensional space (e.g., 2D or 3D).
 
Measurement vector: Sensor data from cameras, LiDAR, radar, etc., which provide noisy observations of the object’s state (such as position or range).
 
Transition model (state transition matrix): This models how the state evolves over time (e.g., how position and velocity change based on motion models).
 
Measurement model: This represents the relationship between the actual state of the system and the measurements received from sensors.
 
Covariance matrices: These quantify uncertainties in the motion model (process noise) and sensor measurements (measurement noise).
 
 
Can Kalman Filters Take Image Features and LiDAR Point Cloud Features?
 
While Kalman filters typically work with simpler, lower-dimensional features like position and velocity, they can be extended to work with image features (e.g., bounding box positions) and LiDAR point cloud features (e.g., object centroids or clusters of points representing obstacles).
 
However, image features such as pixel coordinates or bounding box coordinates need to be converted into meaningful measurements (like object distance or velocity). LiDAR point cloud data may also need preprocessing, such as clustering points to form objects, before being used in the filter.
 
In practice, Kalman filters are often used in conjunction with object detection algorithms that extract these higher-level features and convert them into suitable measurements for tracking.
 
Output of Kalman Filters
 
The output of a Kalman filter is an estimated state of the object, which includes:
 
Position (e.g., x, y, z coordinates)
 
Velocity
 
Acceleration (if modeled)
 
Covariance: A matrix indicating the uncertainty in the estimated state.
 
 
The filter also provides a prediction for the future state of the object, allowing the vehicle to anticipate object movements.
 
Do You Need Object Detection (Bounding Boxes) First?
 
Yes, in most cases, object detection is a prerequisite for tracking with Kalman filters. The Kalman filter itself does not detect objects but instead tracks objects that have already been detected by a sensor system (e.g., a camera detecting bounding boxes around cars, or a LiDAR system identifying clusters of points). The detection system provides the initial position and size of the object, which becomes the input measurement for the Kalman filter to start tracking.
 
Temporal Aspects in Kalman Filters
 
Kalman filters inherently work in the temporal domain. By recursively predicting and updating the state over time, they are designed to handle continuous streams of data, making them suitable for real-time applications like autonomous driving. The filter:
 
Predicts the next state based on the current velocity and acceleration at each timestep.
 
Incorporates new measurements as they arrive to correct the prediction. This ensures smooth and continuous tracking of objects even when some measurements are noisy or momentarily unavailable.
 
 
The time interval between predictions (the filter’s time step) plays a crucial role. A smaller time step provides more frequent updates, improving tracking precision but increasing computational load.
 
Libraries for Implementing Kalman Filters
 
Several libraries exist for implementing Kalman filters in autonomous driving and other applications:
 
OpenCV: Has a built-in Kalman filter implementation in both C++ and Python, widely used in computer vision tasks.
 
pykalman: A Python library for implementing Kalman filters with easy integration into projects.
 
FilterPy: A comprehensive Python library for Kalman filtering, especially useful for teaching and research.
 
SciPy: Provides basic Kalman filtering utilities and state estimation tools.
 
 
Converting Kalman Filter Functionality into a Machine Learning Model
 
To convert the functionality of a Kalman filter into a machine learning model, one can replace the explicit mathematical model with a data-driven model. This involves using machine learning to learn the underlying dynamics of the objects being tracked from data. A neural network or a deep learning model could replace the motion and measurement models in a Kalman filter. The steps could include:
 
1. State Representation: The inputs to the ML model would still include object state information (position, velocity, etc.), as well as sensor data (camera images, point clouds).
 
 
2. Training: Use supervised learning to train the model to predict object states based on sensor data and previous states. Temporal data (i.e., sequences of measurements) would be essential to capture the dynamics.
 
 
3. Recurrent Models: Recurrent neural networks (RNNs) or Long Short-Term Memory (LSTM) networks are well-suited for handling temporal dependencies. They can be trained on time-series data to predict future states based on past states and measurements.
 
 
4. Handling Uncertainty: Bayesian neural networks or probabilistic methods can be integrated to estimate uncertainty, similar to the covariance matrix in Kalman filters.
 
 
 
This approach could allow for tracking without the need for hand-crafted models and equations but would require large datasets for training. Additionally, ML models could potentially capture more complex, non-linear dynamics than Kalman filters.
 
Popular Object Tracking ML Models
 
Several modern machine learning models have been developed for object tracking, especially in autonomous driving scenarios:
 
SORT (Simple Online and Realtime Tracking): A tracking algorithm that combines object detection (bounding boxes) with Kalman filtering. It's a simple yet effective approach.
 
DeepSORT: An extension of SORT that adds appearance features (using a deep neural network) to improve object tracking by maintaining identity consistency.
 
TrackNet: A deep learning-based object tracking framework that directly predicts object positions in a video stream.
 
FairMOT: A real-time multi-object tracking model that combines object detection and tracking into a single neural network, making it efficient for tasks requiring both.
 
ByteTrack: A recent tracking method that handles noisy object detections and association tasks efficiently, improving performance in crowded environments.
 
 
Summary
 
Kalman filters are widely used for tracking in autonomous driving, providing a method to estimate and predict the state of objects using sensor data. They require object detections, which are then tracked using a recursive prediction-update process. While they handle temporal aspects naturally, machine learning models like LSTMs or RNNs can be used to emulate their functionality and capture more complex dynamics. Libraries like OpenCV and pykalman facilitate Kalman filter implementation, and modern tracking methods like DeepSORT offer integrated solutions for object detection and tracking in real-time applications.


#### How object tracking done using ML models rather than Kalman filters? what are different ML models? How do they work? In BEV based system, how do we track objects? What are different model driven tracking mechnisms? Do they be temporal? How memory is used to capture prior?

In modern autonomous driving systems, object tracking can be performed using machine learning (ML) models rather than traditional methods like Kalman filters. These ML-based approaches, especially deep learning models, offer more complex representations and can handle non-linear dynamics, occlusions, and multi-object interactions more effectively.
 
1. Object Tracking Using ML Models
 
Machine learning models for object tracking aim to predict the position, orientation, and motion of objects across successive frames. The key idea is to learn the temporal relationships between object detections in consecutive frames and maintain a unique identifier for each object.
 
Key Concepts:
 
Detection-based tracking: ML models first detect objects in individual frames, then associate these detections across time to form tracks.
 
Feature-based tracking: Models extract features (e.g., appearance, shape) from objects and use these features to link objects across frames.
 
 
2. Types of ML Models for Object Tracking
 
a. Recurrent Neural Networks (RNNs) and Long Short-Term Memory (LSTM)
 
RNNs and LSTMs are types of models used for sequence modeling. They can learn temporal dependencies in object motion, making them well-suited for object tracking.
 
These models take a sequence of object detections and predict the next location based on the historical motion and appearance patterns.
 
 
Example:
 
An LSTM-based model can take in the object's previous positions and velocities, then predict its next position by learning the motion dynamics over time.
 
b. Convolutional Neural Networks (CNNs)
 
CNNs are often used in feature extraction for tracking. They can be trained to learn visual features of objects (like shape, color, etc.) that are consistent across frames.
 
A CNN combined with a correlation filter can track objects based on their visual appearance, helping the system identify the same object across multiple frames.
 
 
c. Transformers (Attention Mechanisms)
 
Transformers, popularized in Natural Language Processing (NLP), have also been applied to object tracking. Attention mechanisms allow the model to focus on different parts of the input (such as different parts of the object) and can handle long-term dependencies.
 
For tracking, a transformer model can learn to focus on the relevant features of an object (shape, texture, etc.) across a sequence of frames, enabling accurate predictions of its movement.
 
 
d. Graph Neural Networks (GNNs)
 
GNNs model the relationships between objects in a scene. In the context of tracking, each object can be represented as a node, and the edges represent the relationships (e.g., distance, velocity). GNNs can model interactions between objects and help track them even in cases of occlusion or close proximity.
 
 
3. Object Tracking in BEV (Bird’s Eye View) Systems
 
In BEV-based systems, object tracking happens in the 3D spatial space, where the perception is represented from a top-down view of the environment. These systems generally use data from LiDAR and camera sensors to detect objects in BEV space, and then track them over time.
 
BEV-based Object Tracking Workflow:
 
1. Object Detection: Objects (e.g., vehicles, pedestrians) are detected in each frame of the BEV. This detection could be done using a 3D CNN or multi-view fusion network that takes inputs from LiDAR and camera.
 
 
2. Data Association: Once objects are detected in the BEV, the model needs to associate objects between frames. This is done by comparing the position, velocity, and appearance of objects in successive frames. Various techniques include:
 
Nearest Neighbor Matching: Associating the closest detections based on Euclidean distance or appearance similarity.
 
IoU (Intersection over Union): Comparing bounding boxes of objects between frames to associate them.
 
 
 
3. Tracking: After association, the movement of objects across frames is modeled. The ML model predicts the future position and velocity of objects based on prior detections. This could involve:
 
Predictive Models (LSTM, RNNs): Learning motion patterns.
 
CNN-based Motion Estimation: Using convolutional layers to predict the change in object position based on historical observations.
 
 
 
4. Prediction and Forecasting: For long-term tracking and decision-making, the system may need to forecast the future positions of objects. This involves training models to predict where objects will be after several time steps (e.g., in the next second or two).
 
 
 
4. Model-Driven Tracking Mechanisms
 
a. Tracking-by-Detection
 
In this paradigm, object detection models (like YOLO, Faster R-CNN) detect objects in each frame, and the tracking algorithm associates these detections over time.
 
Example: You can use a CNN-based detection model followed by an RNN to track objects based on their detection history.
 
 
b. End-to-End Deep Learning Models for Tracking
 
Some models are trained to perform detection and tracking jointly. These models learn to predict both the object’s current location and its movement over time.
 
Example: Models like DeepSORT (Simple Online and Realtime Tracking with a Deep Association Metric) integrate feature extraction with data association, linking detections across frames for consistent tracking.
 
 
c. Memory-Based Models (Temporal Models)
 
Temporal models like LSTMs and transformers can store information about the object’s past states. This enables them to predict future states based on previous motion patterns.
 
Temporal Memory: In LSTMs, the hidden state serves as a memory of past inputs, which helps in predicting the next position of the object.
 
 
d. Graph-Based Models
 
Object tracking can also be performed using graph-based models like Graph Neural Networks (GNNs), where objects and their relationships (e.g., relative motion) are modeled explicitly. These can capture complex interactions between objects in dense traffic scenarios.
 
 
5. Temporal Tracking and Memory
 
Tracking inherently involves temporal processing, as we are interested in the position of an object across multiple frames. In ML-based tracking models, memory is critical to capture prior information about object positions, motion dynamics, and appearance features.
 
LSTM/RNN models explicitly handle time dependencies by maintaining an internal state (memory) that is updated at each time step based on new data.
 
Transformers use attention mechanisms to capture long-range dependencies, enabling them to learn how objects move over time without explicitly maintaining a state like LSTMs do.
 
CNN-based models may handle tracking by taking a sequence of frames as input and using the convolution layers to capture both spatial and temporal changes in the object’s position.
 
 
6. How Memory Captures Prior Information
 
In ML-based tracking, memory refers to storing information about past frames to improve tracking accuracy:
 
RNN/LSTM memory: Stores information about previous positions and movements of objects. This allows the model to make predictions about future states by taking into account the object's trajectory over several frames.
 
Transformer memory: Uses attention mechanisms to attend to relevant past frames or detections when predicting an object's movement. This is a more flexible form of memory that doesn’t rely on sequential data processing.
 
Memory Bank: In some models, a memory bank can store feature embeddings of objects (e.g., appearance, motion) from previous frames. This helps the model recall what an object looked like in case of occlusions or reappearances.
 
 
7. Synchronization and Time Stamp-Based Tracking
 
In BEV-based systems, data from multiple sensors (camera, LiDAR, radar) must be synchronized to ensure that object tracking is accurate. Typically, this is done using timestamps:
 
Each sensor provides data with a timestamp that corresponds to the exact moment it was captured.
 
The tracking system aligns the data from multiple sensors (LiDAR, camera) based on these timestamps, ensuring that the perception system has a consistent view of the environment.
 
If there is a difference in frame rates between sensors, interpolation or extrapolation is used to align the data.
 
 
Conclusion
 
Machine learning models for object tracking offer flexible and robust ways to track objects in autonomous driving scenarios. Models like LSTM, CNN, transformers, and GNNs can learn temporal patterns, predict motion, and handle complex interactions between objects. BEV-based systems take advantage of 3D spatial information from LiDAR and camera fusion to track objects in a more holistic manner. Temporal models with memory (like LSTMs) help in capturing object dynamics across time, while time stamping ensures synchronization of data across different sensors.
 
