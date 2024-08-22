# In-Vehicle Monitoring Systems 

> In-Vehicle Monitoring Systems (IVMS) enhances vehicle safety and driver comfort by monitoring the driver, passengers, and the vehicle's interior environment.

- [IVMS Use Cases]()
- [ML Models]()
- [Hardware & Sensors]()

Below are some key ML use cases in IVMS:

|Activity|Usecases|ML Algorithms|---|
|---|---|----|---|
|<h4>Pose Estimation</h4>|Pose estimation involves detecting and tracking the body posture of the driver and passengers. Pose Estimation is crucial for detecting drowsiness, inattentiveness, and improper seating postures that could compromise safety.|ML techniques such as OpenPose or PoseNet can extract key body points and track movements in real time.|<img src="https://i.ytimg.com/vi/UZqpqNsC84Y/maxresdefault.jpg" height="100%" width="100%" />|
|<h4>Driver Drowsiness Detection</h4>|Detecting signs of drowsiness or fatigue in drivers can prevent accidents. This is often done by monitoring eye closure, head position, and other facial cues.|Techniques such as facial landmark detection and eye aspect ratio (EAR) calculation are also employed.|<img src="https://i.ytimg.com/vi/UZqpqNsC84Y/maxresdefault.jpg" height="100%" width="100%" />|
|<h4>Seat Belt Detection</h4>|Detecting whether passengers are wearing seat belts is essential for safety compliance.||<img src="" height="100%" width="100%" />|
|<h4>Gesture Operations</h4>|Gesture recognition allows drivers to control vehicle functions (e.g., adjusting the volume, accepting calls) using hand gestures, minimizing distractions.||<img src="" height="100%" width="100%" />|
|<h4>Occupancy Detection</h4>|Detecting the presence and number of occupants in the vehicle is important for various applications, including airbag deployment optimization, HVAC control, and security.|Infrared cameras combined with ML algorithms like CNNs can be used to detect and count occupants, even in low-light conditions. Trends: The use of 3D sensors and LiDAR in combination with ML models is enhancing the accuracy of occupancy detection systems.|<img src="" height="100%" width="100%" />|
|<h4></h4>|||<img src="" height="100%" width="100%" />|
|<h4></h4>|||<img src="" height="100%" width="100%" />|

    
## ML Models

ML Trends: Advanced models like attention-based networks are being used to focus on the most relevant facial features for detecting drowsiness, improving accuracy and reducing false positives.

|Year|Model|Model Type|Model Description|Model Architecture|Research Paper|Code|Benchmarks|
|---|---|---|---|---|---|---|---|
|2016|OpenPose|Pose Estimation|Multi-person detection for human pose estimation, useful for driver monitoring.|Part Affinity Fields (PAFs) and CNNs||||
|||||||||
|||||||||
|2021|Transformer Sequence Modeling||Transformer architecture applied to gesture recognition and pose estimation.|||||
|||||||||

## Hardware & Sensors

- Cameras: High-resolution RGB cameras are used for tasks like pose estimation, gesture recognition, and occupancy detection. These cameras provide real-time video feeds, which are processed by ML models to detect and track objects and behaviors.
- Infrared (IR) Cameras: Used for low-light or night-time monitoring, particularly for tasks like drowsiness detection and occupancy detection. IR cameras work by detecting infrared radiation, which is emitted by all objects with a temperature above absolute zero.
- LiDAR: LiDAR sensors use laser beams to create detailed 3D maps of the vehicle's interior, aiding in accurate occupancy detection and pose estimation. These sensors are particularly useful in low-visibility conditions.
- Ultrasonic Sensors: Used for proximity detection and occupant classification. They emit sound waves and measure the time taken for the echo to return, helping in detecting objects and their distance from the sensor.
- Radar Sensors: Radar is employed for detecting the presence and motion of occupants, as well as monitoring heart rate and respiration for drowsiness detection.

Diagrams of Sensors:

    Camera Sensor: Camera Diagram
    LiDAR Sensor: ![LiDAR Diagram](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/L
