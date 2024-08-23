# In-Vehicle Occupants Monitoring Systems 

> In-Vehicle Occupants Monitoring System enhances vehicle safety and driver comfort by monitoring the driver, passengers, and the vehicle's interior environment.

- [In-Vehicle Occupants Monitoring Concepts]()
  - [Human Pose Estimation]()
  - [Driver Drowsiness Detection]()
  - [Seat Belt Detection]()
  - [Gesture Operations]()
  - [Occupancy Detection]() 
- [Datasets]()
  - [2D]() [3D]() 
  - [Performance Measures]()
- [ML Models]()
- [Hardware & Sensors]()

## Concepts

|Activity|Usecases|ML Algorithms|---|
|---|---|----|---|
|<h4>Human Pose Estimation</h4>|Pose estimation involves detecting and tracking the body posture of the driver and passengers. Pose Estimation is crucial for detecting drowsiness, inattentiveness, and improper seating postures that could compromise safety.|ML techniques such as OpenPose or PoseNet can extract key body points and track movements in real time.|<img src="https://i.ytimg.com/vi/UZqpqNsC84Y/maxresdefault.jpg" height="100%" width="100%" />|
|<h4>Driver Drowsiness Detection</h4>|Detecting signs of drowsiness or fatigue in drivers can prevent accidents. This is often done by monitoring eye closure, head position, and other facial cues.|Techniques such as facial landmark detection and eye aspect ratio (EAR) calculation are also employed.|<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.RIr16UO7ARQ5D8_VCVvZ1gHaEI%26pid%3DApi&f=1&ipt=aa767fe26e25db3d7104b9e95e308e4a9193b0614f872cc70114d2385f370a8f&ipo=images" height="100%" width="100%" />|
|<h4>Seat Belt Detection</h4>|Detecting whether passengers are wearing seat belts is essential for safety compliance.||<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.0-RyrIz-nyseQz8rCDSiowHaEK%26pid%3DApi&f=1&ipt=04a9f1a12558f608e4b8f26691bcabb3a09fd0bf084ebfecc1593a4c56095eb5&ipo=images" height="100%" width="100%" />|
|<h4>Gesture Operations</h4>|Gesture recognition allows drivers to control vehicle functions (e.g., adjusting the volume, accepting calls) using hand gestures, minimizing distractions.||<img src="https://how2electronics.com/wp-content/uploads/2020/01/Gesture-Recognition-and-Its-Application-in-Machine-Learning-1000x528.jpg" height="100%" width="100%" />|
|<h4>Occupancy Detection</h4>|Detecting the presence and number of occupants in the vehicle is important for various applications, including airbag deployment optimization, HVAC control, and security.|Infrared cameras combined with ML algorithms like CNNs can be used to detect and count occupants, even in low-light conditions. Trends: The use of 3D sensors and LiDAR in combination with ML models is enhancing the accuracy of occupancy detection systems.|<img src="https://www.ai-online.com/wp-content/uploads/2020/05/Xperi-Corporation-announced-that-its-in-cabin-monitoring-solution-1024x572.jpg" height="100%" width="100%" />|

### Human Pose Estimation

:star::star::star: [What is Human Pose Estimation?](https://softwaremill.com/human-pose-estimation-2023-guide/)

By knowing the orientation and overall appearance of a person, we can understand human behavior and recognize activities within images or videos.

Human pose estimation and tracking is a computer vision task that includes detecting, associating, and tracking semantic key points such as “right shoulders,” and “left knees.”

Human pose estimation aims to predict the poses of human body parts and joints in images or videos.

Human body is usually represented in three common types: skeletal model, planar model, volume model

<img src="https://viso.ai/wp-content/uploads/2021/01/human-pose-model.jpg" width="50%" height="50%" />

#### ML Models

Deep Learning based Pose Detection methods

|Year|Model|Model Category|Model Description|Model Architecture|Research Paper|Code|Benchmarks|
|---|---|---|---|---|---|---|---|
|2016|OpenPose|Pose Estimation| Bottom-up apprach |Multi-person detection for human pose estimation, useful for driver monitoring.|Part Affinity Fields (PAFs) and CNNs||[Understanding OpenPose (with code reference)— Part 1](https://medium.com/analytics-vidhya/understanding-openpose-with-code-reference-part-1-b515ba0bbc73)|
|2024|[HoT - Hourglass Tokenizer for Efficient Transformer-Based 3D Human Pose Estimation (CVPR 2024)](https://github.com/NationalGAILab/HoT)|||||||
|||||||||

### Driver Drowsiness Detection

Techniques used to identify drowsiness,

- Behavioural Parameter-Based Techniques: Measures driver’s fatigue through behavioural parameters of the driver, such as eye closure ratio, eye blinking, head position, facial expressions, and yawning.

Percentage of Eye Closures (PERCLOS) are one of the most commonly used metrics in detecting drowsiness based on eye state observation. PERCLOS is the ratio of eye closure over a period, and then on the result of PERCLOS, eyes are referred to as open or closed.
Yawning-based detection systems analyse the variations in the geometric shape of the mouth of a drowsy driver, such as the broader opening of the mouth, lip position, etc. Behavioural-based techniques use cameras and computer vision techniques to extract behavioural features.

- Vehicular Parameters-Based Techniques: Vehicular parameter-based methods try to detect driver fatigue based on vehicular features such as frequent lane-changing patterns, vehicle speed variability, steering wheel angle, steering wheel grip force, etc

- Eye Aspect Ratio (EAR)  

EAR is a widely used metric for measuring eye-opening and is commonly used in facial expression analysis, eye tracking, and driver drowsiness detection systems. EAR is calculated by measuring the ratio of the distance between the vertical landmarks of the eye (the upper and lower eyelids) to the distance between the horizontal landmarks of the eye.

<img src="https://www.ijraset.com/images/text_version_uploads/imag%201_29670.png" />

## Datasets

- Near-Infrared (IR) Images 
- Depth images (RGB-D) which provide explicit 3D information
- Multiple RGB images from different views to address occlusion challenges

<img src="https://cdn.prod.website-files.com/5d7b77b063a9066d83e1209c/62dfe3c6b83ee8a71aeadf54_IN%20TEXT%20ASSET-6.jpg" width="50%" height="50%"/>

### 2D

[MPII Human Pose Dataset](http://human-pose.mpi-inf.mpg.de/)


### 3D



HIVE (Human In VEhicles) provides RGB and NIR in-vehicle image pairs with ground-truth 2D and 3D pose and shape annotations

A synthetic dataset consists of synthesized humans with different shapes and poses in vehicels.

[Drive&Act](https://driveandact.com/): A Multi-Modal Dataset for Fine-Grained Driver Behavior Recognition in Autonomous Vehicles

dataset features twelve hours and over 9.6 million frames of people engaged in distractive activities during both, manual and automated driving. We capture color, infrared, depth and 3D body pose information from six views and densely label the videos with a hierarchical annotation scheme, resulting in 83 categories. 

### Performance Measures

[PCK - Percentage of Correct Keypoints](https://softwaremill.com/human-pose-estimation-2023-guide/)
[OKS - Object Keypoint Similarity](https://softwaremill.com/human-pose-estimation-2023-guide/)

This metric is used in the MPII dataset, where the detected joint is considered correct when the distance between the predicted location and the true location is within a certain threshold.

MPJPE
PA-MPJPE

## ML Models

Classical Human Pose Estimation solutions are based on classical Computer Vision, with a focus on parts and changes in colors and contrast. In the past few years, this area has been dominated by deep learning solutions distinguished into two branches,

- Top-down approaches: firstly performing person detection and then regressing key points within the chosen bounding box. 
- Bottom-up appraches: Estimate each body joint first and then group them to form a unique pose. Bottom-up approaches produce multiple skeletons at once, so they are often faster and more suitable for real-time solutions and also perform better in crowd scenes for multi person pose estimation.

Deep Learning based Pose Detection methods



|Year|Model|Model Category|Model Description|Model Architecture|Research Paper|Code|Benchmarks|
|---|---|---|---|---|---|---|---|
|2016|OpenPose|Pose Estimation| Bottom-up apprach |Multi-person detection for human pose estimation, useful for driver monitoring.|Part Affinity Fields (PAFs) and CNNs|||
|||||||||
|||||||||
|2021|Transformer Sequence Modeling||Transformer architecture applied to gesture recognition and pose estimation.|||||
|2024|[HoT - Hourglass Tokenizer for Efficient Transformer-Based 3D Human Pose Estimation (CVPR 2024)](https://github.com/NationalGAILab/HoT)|||||||

## Hardware & Sensors

- Cameras: High-resolution RGB cameras are used for tasks like pose estimation, gesture recognition, and occupancy detection. These cameras provide real-time video feeds, which are processed by ML models to detect and track objects and behaviors.
- Infrared (IR) Cameras: Used for low-light or night-time monitoring, particularly for tasks like drowsiness detection and occupancy detection. IR cameras work by detecting infrared radiation, which is emitted by all objects with a temperature above absolute zero.
- LiDAR: LiDAR sensors use laser beams to create detailed 3D maps of the vehicle's interior, aiding in accurate occupancy detection and pose estimation. These sensors are particularly useful in low-visibility conditions.
- Ultrasonic Sensors: Used for proximity detection and occupant classification. They emit sound waves and measure the time taken for the echo to return, helping in detecting objects and their distance from the sensor.
- Radar Sensors: Radar is employed for detecting the presence and motion of occupants, as well as monitoring heart rate and respiration for drowsiness detection.

https://electronicsmaker.com/detecting-vehicle-occupancy-with-mmwave-sensors

### Credits
- [A Systematic Review of Recent Deep Learning Approaches for 3D Human Pose Estimation](https://www.mdpi.com/2313-433X/9/12/275)
- [Driver Drowsiness Detection System using Deep Learning](https://www.ijraset.com/research-paper/driver-drowsiness-detection-system-using-deep-learning)
- [Human Pose Estimation with Deep Learning – Ultimate Overview in 2024](https://viso.ai/deep-learning/pose-estimation-ultimate-overview/)
