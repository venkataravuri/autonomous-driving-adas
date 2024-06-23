# :camera: Perception

> Perception refers to the processing and interpretation of sensor data to detect, identify, classify and track objects.

Perception helps car to see the world around itself, as well as recognize and classify the things that it sees.
- The car needs to see and classify traffic lights, pedestrians, road signs, walkways, parking spots, lanes, and much more.
- Not only that, it also needs to know the exact distance between itself and the objects around it.

To achieve such a high level of perception, a self-driving car must have three sensors:
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

