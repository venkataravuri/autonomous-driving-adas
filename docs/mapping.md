# Mapping & Localization

## Mapping

Given a surround view of images, optionally accompanied by lidar point clouds, the end to end map generation task aims to predict map elements directly. Map elements include road boundaries, lane delimiters, centerlines, and crosswalks.

### HD Maps

High-definition (HD) maps offer an intricate and precise depiction of the road, encompassing lane markings, traffic signs, and other critical features. 

### Algorithms

- [HDMapNet: An Online HD Map Construction and Evaluation Framework](https://arxiv.org/pdf/2107.06307)
- [MapTRv2: An End-to-End Framework for Online Vectorized HD Map Construction](https://arxiv.org/pdf/2308.05736)

 PoseNet and VLocNet++, are some of the frameworks that use point data to estimate the 3D position and orientation. These estimated 3D positions and orientations can be used to derive scene semantics, as seen in the image below. 

## Localization

Localization algorithms in self-driving cars calculate the position and orientation of the vehicle as it navigates – a science known as Visual Odometry (VO).

VO works by matching key points in consecutive video frames. With each frame, the key points are used as the input to a mapping algorithm. The mapping algorithm, such as Simultaneous localization and mapping (SLAM), computes the position and orientation of each object nearby with respect to the previous frame and helps to classify roads, pedestrians, and other objects around.

