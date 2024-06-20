# :ok_hand: Awesome Self-Driving Cars & Autonomous Vehicles :car:
A repository of autnonoums self-driving vehicles articles, dataset, software and more.

## Overview
Traditional autonomous driving technology divides autonomous driving pipeline into several different functions such as perception, localization & mapping, prediction, planning, and control. However, modern architecture encapsulates entire pipeline tasks into a single module, leveraging an end-to-end deep neural network for high integration level.

## :camera: Perception

###  object detection or tracking 

Multi-Object Tracking

Generate the trajectories of objects and bounding box (bbox). The labels on top of a bbox (for example, [21] (0.24)) show the car ID (for example, 21), and the tracking confidence (for example, 0.24), respectively.


Generating the trajectory of an object requires identifying the same object over time even when there are abrupt changes in visual appearance or motion dynamics. 

multi-object trackers (MOT).

simple online and real-time tracker (SORT) that uses a Kalman filter for state estimation and a data association algorithm for target association based on the target bounding boxes from the detector. 

detection errors include partial or double detections and missed detections
 environmental occlusions

vehicle tracking, Pedestrian tracking

Multi-Sensor Kalman Filter



|  object tracker types | ML Models | Technology | Hardware & Devices | Papers |
| --- | --- | --- | --- | --- |
| ? | ? | ? | ? | ? |
| ? | ? | ? | ? | ? |

Sources
- [DRIVE Labs: Tracking Objects With Surround Camera Vision](https://developer.nvidia.com/blog/drive-labs-tracking-objects-with-surround-camera-vision/)

### Visual Perception

### RADAR Perception

### LiDAR Perception

## Prediction

## Planning

## Control

## Simulation

### Log-Replay Vs. Simulation

## :world_map: Mapping & Localization

## :safety_vest: Autonomous Vehicle Safety

### Regulation & Standards

#### Driver Assist System

##### L2 to L3

##### High-level (L4+) Autonomous Driving 

## Auto Industry

## :trophy: Challenges

[Autonomous Grand Challenge 2024](https://opendrivelab.com/challenge2024/)

- [CVPR Challenge - zeron.ai Paper - End-to-End Autonomous Driving Using Vision Language Model](https://opendrivelab.com/challenge2024/technical_report/e2e_ZERON.pdf)
- [CVPR Challenge - NVIDIA Paper - Hydra-MDP: End-to-end Multimodal Planning with Multi-target Hydra-Distillation](https://opendrivelab.com/challenge2024/technical_report/e2e_ZERON.pdf](https://opendrivelab.com/challenge2024/technical_report/e2e_Team%20NVIDIA.pdf))

[Computer Vision and Pattern Recognition Conference (CVPR)](https://cvpr.thecvf.com/)

