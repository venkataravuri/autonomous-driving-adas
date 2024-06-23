# :ok_hand: Awesome Self-Driving Cars (AV & ADAS) :car:
A repository of autnonoums self-driving vehicles articles, dataset, software and more.

## Overview
Traditional autonomous driving technology divides autonomous driving pipeline into several different functions such as perception, localization & mapping, prediction, planning, and control. However, modern architecture encapsulates entire pipeline tasks into a single module, leveraging an end-to-end deep neural network for high integration level.

AV software development has traditionally been based on a modular approach, with separate components for object detection and tracking, trajectory prediction, and path planning and control.

End-to-end autonomous driving systems streamline this process using a unified model to take in sensor input and produce vehicle trajectories, helping avoid overcomplicated pipelines and providing a more holistic, data-driven approach to handle real-world scenarios.

end-to-end model ingests camera and lidar data, as well as the vehicle’s trajectory history, to generate a safe, optimal vehicle path for five seconds post-sensor input.

advanced driving assistance systems (ADAS), 

## :camera: Perception

> Perception refers to the processing and interpretation of sensor data to detect, identify, classify and track objects.

###  object detection or tracking 

Multi-Object Tracking

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

### Sensor Fusion

Sensor fusion is the merging of data from at least two sensors. Sensor fusion along with perception enables an autonomous vehicle to develop a 3D model of the surrounding environment that feeds into the vehicle’s control unit.

### Object-Level Fusion

Traditional _object-level fusion_ approach, perception is done separately on each sensor.

<img src="https://leddartech.com/app/uploads/2022/03/figure1.png" width="50%" height="50%" />

This is not optimal because when sensor data is not fused before the system makes a decision, it may need to do so based on contradicting inputs. For example, if an obstacle is detected by the camera but was not detected by the LiDAR or the radar, the system may hesitate as to whether the vehicle should stop.

### Raw Data Sensor Fusion

In a raw-data fusion approach, objects detected by the different sensors are first fused into a dense and precise 3D environmental RGBD model, then decisions are made based on a single model built from all the available information.

<img src="https://leddartech.com/app/uploads/2022/03/figure2.png" height="50%" width="50%" />

Fusing raw data from multiple frames and multiple measurements of a single object improves the signal-to-noise ratio (SNR), enables the system to overcome single sensor faults and allows the use of lower-cost sensors. This solution provides better detections and less false alarms, especially for small obstacles and unclassified objects.

### depth estimation

### Visual Perception

full autonomous driving requires complete, 360-degree surround camera vision.

 surround camera object tracking software currently leverages a six-camera, 360-degree surround perception setup that has no blind spots around the car. The software tracks objects in all six camera images, and associates their locations in image space with unique ID numbers as well as time-to-collision (TTC) estimates.

 feature points which are invariant to rotation and translation are detected by the Harris Corner Detector [1]. Small templates centered on the corner points are tracked by the Lucas-Kanade template tracking algorithm

 Ghost tracks due to objects moving out of the scene are the main cause of false positive braking. Removing them with low latency and without missing any object tracks is a challenging task. 

 variety of seasons, routes, times of the day, illumination conditions, highway, and urban roads.

Surround-view fisheye cameras

### RADAR Perception

### LiDAR Perception

## Prediction

## Planning

## Control

## Simulation

 testing inside the open-source NAVSIM simulator 
 

### Log-Replay Vs. Simulation

## :world_map: Mapping & Localization

## :safety_vest: Autonomous Vehicle Safety

### Regulation & Standards

#### Advance Driver Assistance System

Advanced driver assistance systems rely on front and rear cameras to perform ,
1. Automatic cruise control (ACC)
2. and lane keep assist. 

##### L2 to L3

##### High-level (L4+) Autonomous Driving 

## Datasets

https://medium.com/analytics-vidhya/15-best-open-source-autonomous-driving-datasets-34324676c8d7

## Auto Industry

## :trophy: Challenges

[Autonomous Grand Challenge 2024](https://opendrivelab.com/challenge2024/)

- [CVPR Challenge - zeron.ai Paper - End-to-End Autonomous Driving Using Vision Language Model](https://opendrivelab.com/challenge2024/technical_report/e2e_ZERON.pdf)
- [CVPR Challenge - NVIDIA Paper - Hydra-MDP: End-to-end Multimodal Planning with Multi-target Hydra-Distillation](https://opendrivelab.com/challenge2024/technical_report/e2e_ZERON.pdf](https://opendrivelab.com/challenge2024/technical_report/e2e_Team%20NVIDIA.pdf))

[Computer Vision and Pattern Recognition Conference (CVPR)](https://cvpr.thecvf.com/)

