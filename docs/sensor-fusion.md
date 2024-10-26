
Sensor fusion is the merging of data from at least two sensors. Sensor fusion along with perception enables an autonomous vehicle to develop a 3D model of the surrounding environment that feeds into the vehicle’s control unit.


Sensor Fusion is the process of fusing data coming from multiple sensors.

<img src="https://i0.wp.com/semiengineering.com/wp-content/uploads/Sensor-fusion-1.png" height="60%" width="60%" />

When one or multiple sensors fail to perform accurately, sensor fusion helps in ensuring that there are no undetected objects. For example, a camera can capture the visuals around a vehicle in ideal weather conditions.

But during dense fog or heavy rainfall, the camera won’t provide sufficient data to the system. This is where radar, and to some extent, LiDAR sensors help.

Furthermore, a radar sensor may accurately show that there is a truck in the intersection where the car is waiting at a red light.

But it may not be able to generate data from a three-dimensional point of view. This is where LiDAR is needed.

## Sensor Fusion Levels

### Low-Level Fusion (Early Fusion)

In this kind of sensor fusion method, all the data coming from all sensors is fused in a single computing unit, before we begin processing it.
For example, pixels from cameras and point clouds from LiDAR sensors are fused to understand the size and shape of the object that is detected.

### Mid-Level Fusion

In mid-level fusion, objects are first detected by the individual sensors and then the algorithm fuses the data.
Generally, a Kalman filter is used to fuse this data.

The idea is to have, let’s say, a camera and a LiDAR sensor detect an obstacle individually, and then fuse the results from both to get the best estimates of position, class and velocity of the vehicle.

### High-Level Fusion (Late Fusion)

This is similar to the mid-level method, except that we implement detection as well as tracking algorithms for each individual sensor, and then fuse the results.

There are several methods for combining LiDAR and camera data:
 
Early Fusion: Raw data from LiDAR and cameras are combined at the sensor level. For example, LiDAR point clouds are projected onto the 2D image, and both the point cloud and pixel data are fed into a neural network for joint object detection.
 
Mid-Level Fusion: LiDAR-based object detection and image-based detection are done separately, and their results are combined. For instance:
 
Use YOLO to detect objects in the 2D image (with 2D bounding boxes).
 
Use LiDAR point clouds to detect objects in 3D space (with 3D bounding boxes).
 
Fuse these results by projecting the 3D LiDAR data onto the 2D image, or by correlating detected objects in both modalities. This improves detection accuracy and helps assign depth to the objects detected by the camera.

Late Fusion: Object detections from LiDAR and camera are processed independently, and the results are combined at a decision-making stage. For example, after YOLO detects objects in the image, the system might confirm or refine those detections using LiDAR data, improving localization or classification.

## Kalman Filters

https://www.thinkautonomous.ai/blog/sensor-fusion/
https://www.thinkautonomous.ai/blog/9-types-of-sensor-fusion-algorithms/


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



#### References
- https://medium.com/@dorlecontrols/sensor-fusion-242bc70e7332
- 



multiple sensors detect the same object may seem unnecessary in ideal scenarios, but in edge cases such as poor weather, sensor fusion is required.

