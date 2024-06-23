> Perception refers to the processing and interpretation of sensor data to detect, identify, classify and track objects.

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
