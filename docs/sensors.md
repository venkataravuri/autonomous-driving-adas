# Sensors

- [LiDAR](#introduction)
    - [Data Format - Point Clouds]()
    - [Calibration]()
    - [Hardware]()
- [Camera]()
    - [Data Format]()
    - [Calibration]()
    - [Hardware]()
- [RADAR]()
    - [Doppler Effect]()
    - [Calibration]()
    - [Data Format]()
    - [Hardware]()
- [Open Datasets]()


# Camera Sensor


Multiple camera sensors are typically positioned to cover different angles around the ego vehicle (front, rear, and sides), providing a near 360-degree view in the 2D space.

Each camera covers a specific Field of View (FoV)

- Camera 1 covers the front (120° FoV).
- Camera 2 covers the rear (120° FoV).
- Four other cameras cover the left, right, front-left, and front-right regions, respectively, with smaller FoVs.


### Calibration

Intrinsic Parameters: These describe the camera’s focal length and principal point, defining how the 3D world is projected onto the 2D image plane.
 
Extrinsic Parameters: These describe the camera’s position and orientation relative to the ego vehicle.

<img align="right" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRexJXGGhK719BgaGSQI5BouU79zlI-NWCOlql5wlISgRugJOwWsFUU1bUw7HBjD1j52u8" width="30%" height="30%" />

# LiDAR - Light Detection and Ranging

LiDAR device functions by emitting laser (light) pulses and measuring the duration it takes for these pulses to return after bouncing off of things. This time delay, known as the “time of flight”, is used to calculate precise distances, allowing for the creation of detailed three-dimensional maps of the environment.

- LiDAR sensor readings are given in a set of 3D coordinates called a Point Cloud (PCL), which gives accurate depth information of each point’s surroundings and intensity levels. 
- LiDAR sensors capture millions of data points per second, creating dense point clouds that represent the vehicle's surroundings in rich 3D scenes of environment.
- Point clouds are rich in spatial information, they lack semantic context.
- Point clouds represent the world in 3D. The LiDAR sensor gets the exact (X,Y,Z) position of every impact point.
- LiDARs don’t work well in bad weather conditions. In cases of fog, the lasers can hit it and muddle the scene. Similar to rain drops or dirt.

> RADARs measure the world by sending radio waves, and SONARs sending sound waves, LiDAR do it using light waves.


# LiDAR

The LiDAR sensor provides a 360-degree view by outputting a 3D point cloud of the surroundings. Assume the LiDAR outputs 100,000 points per frame, each point with 3D coordinates  relative to the vehicle's reference frame. The LiDAR also provides intensity information per point, which indicates how strong the reflection was.

### LiDAR Data Formats

| Data Format | Dataset | Details |
|---|---|---|
|bin|KITTI|?|
|LAS |KITTI|?|
XYZ & ASCII
PLY

## LiDAR Hardware

- [OUSTER](https://ouster.com/) formerly Velodyne

#### How LiDARs estimate Velocity?

LiDAR estimate velocity as difference between two consecutive measurements. RADARs, on the other hand, can estimate the velocity using Doppler effect.

#### How LiDARs point clouds can be stored efficiently?

- Point cloud data is stored in formats like LAS, LAZ, or PLY, with metadata like color or intensity values.
- Data is structured using techniques like octrees or k-d trees. These structures enable faster data access and manipulation.
- Data compression is applied to reduce storage needs while maintaining accuracy.
  
- [Storing Point Clouds in PostgreSQL](https://oslandia.com/wp-content/uploads/2018/05/Lemoine-Oslandia-Pointcloud.pdf)

#### LiDAR Point Cloud Visualization Tools

## RADAR

Radar stands for Radio Detection And Ranging.

### Physics of Radar

Radar radio frequency (RF) generator emits electromagnetic waves and its receiver picks up, filters and processes the waves rebounded from the metal surfaces or other reflecting materials. The distance to the objects is measured by multiplying speed of the radio wave (speed of light~300,000 km/s) by half of the propagation time (transmission time + receiving time).

#### What are applications of radar?
Some applications of radar are in adaptive cruise control (ACC), predictive emergency braking (PEBS) and blind-spot monitoring (BSM) systems.

non-line-of-sight (NLOS) detection — detecting objects and agents that are hidden (“occluded”).

 Tesla Autopilot has some ability to do this on the highway, for example when an occluded vehicle two or three cars ahead hits the brakes suddenly.

#### What are different types of radar?

There are different types of radars based on the range and beam angle. In the past the main types were short-range radars (SRR) in the ~24 GHz frequency band and long-range radars (LRR) in the ~76 GHz frequency band. But the applications are merging and some radars cover both ranges known as mid-range radars (MRR) in the 76 to 81 GHz. Eventually MRRs are expected to dominate the market supplemented by a LRR. Short-range radars typically have a range of 20–50 meters and a beam angle of up to 160 degrees. Long-range radars have ranges of 250 m and beam angles of up to 30 degrees. Mid-range radars have ranges of 100–150m and a beam angle in between.

#### What is doppler effect?
Radar can also measure the relative speed of all the detected objects using the doppler shift of the reflected electromagnetic wave as well as the transverse offset with an angle estimation.

 Doppler effect, where a moving target produces a shift in frequency in the EM wave being reflected from the object.

Radar works by emitting a radio frequency signal and measuring the time it takes for the received signal to bounce back after it hits an object. By measuring the frequency difference which is created through time delay and doppler effect, radar can determine the distance and speed of the object.

#### What are strengths of radar over other sensors?
- They’re able to see through objects unlike lidar.
- They work normally in bad weather (rain, snow, dust) unlike lidar.
- They work well in fog and low light night time situations unlike cameras.
- Some newer versions have resolutions and object recognition capabilities comparable to lidar.

#### References
- https://medium.com/@BabakShah/radar-in-self-driving-cars-5a31951164e2
- https://www.linkedin.com/pulse/auto-annotating-labeling-lidar-data-self-driving-vehicles-bertini/
- https://www.thinkautonomous.ai/blog/voxel-vs-points/
- https://www.thinkautonomous.ai/blog/types-of-lidar/
- https://www.thinkautonomous.ai/blog/how-lidar-detection-works/


#### For autonomous driving, what are different camera sensors from MobileEye? What data can be streamed from these sensors? Which format it streams data? What are the specs of camera sensors? What is focal length?

Mobileye, a leader in advanced driver-assistance systems (ADAS) and autonomous driving technology, develops a variety of camera sensors that are crucial for enabling autonomous vehicles to perceive their surroundings. These camera sensors are part of Mobileye’s EyeQ system-on-chip (SoC) solutions, which process the visual data to perform tasks like object detection, lane detection, traffic sign recognition, and more. While the exact model numbers and specific cameras Mobileye integrates can vary by generation and automotive partner, here are the general aspects of Mobileye's camera systems:
 
1. Mobileye Camera Sensors for Autonomous Driving
 
Mobileye typically deploys multi-camera setups that are forward, rearward, and side-facing, in both monocular and stereo configurations. These sensors are embedded into the vehicle for robust 360-degree perception.
 
Types of Camera Setups:
 
Monocular Camera: Single cameras used for recognizing lanes, traffic signs, vehicles, pedestrians, and other road users.
 
Stereo Camera: Dual cameras used for depth perception (e.g., measuring the distance to an object using disparity between the two cameras’ views).
 
 
2. Data Streamed from Mobileye Camera Sensors
 
The data streamed from Mobileye’s camera sensors typically includes:
 
RGB Image Data: Raw image frames captured by the cameras, representing the visual environment. These can be processed to detect objects, lanes, traffic signs, etc.
 
Depth Information: If using stereo cameras, disparity maps or depth maps are calculated based on the difference between the two camera views.
 
Semantic Information: The camera data can be processed by the onboard Mobileye EyeQ chip to extract information like detected objects (cars, pedestrians, cyclists), lane markings, traffic signs, free space, and road geometry.
 
Meta-data: This can include the camera’s position, orientation, and timestamp data to synchronize with other sensor streams (LiDAR, radar).
 
 
3. Data Formats
 
Raw Image Data: Typically, the image data from Mobileye cameras can be streamed in YUV or RGB formats. Depending on the processing pipeline, data can also be converted into compressed formats like JPEG or video streams in formats like H.264 for transmission or storage.
 
Processed Data: After processing on Mobileye's EyeQ chip, data like object detection bounding boxes, lane positions, and classification results (e.g., car, pedestrian) are output as structured data (bounding boxes, labels, etc.) in real-time.
 
CAN Bus / Ethernet: Processed sensor information can be sent via CAN (Controller Area Network) or Ethernet to the vehicle’s main system.
 
 
4. Specifications of Mobileye Camera Sensors
 
The specific camera specs of Mobileye sensors can vary, especially with the EyeQ generation and the vehicle manufacturer it is integrated into. However, general specifications include:
 
Common Specifications:
 
Resolution: Typically around 1280 x 960 pixels for a monocular camera, but this can vary depending on the camera's purpose (e.g., high-resolution front cameras vs. lower-resolution side cameras).
 
Field of View (FoV): Cameras typically have wide fields of view, ranging from 40 degrees to 120 degrees, depending on their purpose (e.g., narrow FoV for long-range detection, wide FoV for lane and side detection).
 
Frame Rate: Cameras capture images at 30 to 60 frames per second (FPS), allowing real-time analysis and decision-making for tasks like lane-keeping and object avoidance.
 
Operating Range: Cameras can detect objects at distances up to 200 meters for long-range cameras and 50-100 meters for side or rear cameras, depending on the resolution and type.
 
 
Focal Length:
 
Focal Length: Focal length refers to the distance between the lens and the image sensor. For Mobileye cameras, the focal length may vary depending on whether the camera is designed for long-range detection (requiring a larger focal length) or short-range detection (requiring a smaller focal length). In Mobileye cameras, typical focal lengths range from 2.5 mm to 6 mm, with longer focal lengths used for high-resolution, far-field object detection.
 
 
5. Capabilities and Features of Mobileye Camera Sensors
 
Object Detection: Cars, trucks, motorcycles, pedestrians, cyclists, and even smaller objects like animals or debris can be detected.
 
Lane Detection: Mobileye cameras are highly efficient at detecting lane markings, including broken lanes, road boundaries, lane curvature, and upcoming lane merges or splits.
 
Traffic Sign Recognition: The cameras are capable of recognizing traffic signs and signals (e.g., stop signs, speed limits) in real-time.
 
Free-Space Estimation: Cameras estimate drivable space (free space) in front of the vehicle, which is essential for path planning in autonomous systems.
 
Vision-Based Localization: Cameras can detect road landmarks and environmental cues to assist in localizing the vehicle on a high-definition map.
 
 
6. Integration and Processing: Mobileye EyeQ Chip
 
Mobileye cameras are tightly integrated with the Mobileye EyeQ series SoC, which handles the real-time processing of image data. The EyeQ chip uses highly efficient computer vision and AI algorithms to:
 
Process high-definition image data.
 
Perform tasks like object detection, lane marking detection, and free space estimation.
 
Output processed and fused sensor data in real-time.
 
 
Mobileye’s fusion of vision and deep learning techniques allows the camera data to contribute to crucial ADAS tasks like collision avoidance, automatic emergency braking, and lane-keeping assistance.
 
7. Conclusion: Mobileye Cameras in Autonomous Driving
 
Mobileye’s camera sensors play a pivotal role in autonomous driving perception systems by providing high-resolution images and semantic understanding of the driving environment. The data streamed from these sensors, typically in YUV or RGB formats, is processed using Mobileye’s powerful EyeQ chips to produce actionable insights for autonomous vehicles, including detecting objects, road lanes, and traffic signs. The exact camera specifications, such as focal length, resolution, and field of view, are fine-tuned for specific use cases, whether for long-range or short-range detection in ADAS or fully autonomous vehicles.
 

#### What is structure of YUV? How it can be compared to RGB? How RGB or YUV compressed into JPEG? what is structure of JPEG? How often mobileeye camera sensor sends data to central board over CAN? If it is H.264 format,  how often it sends?

1. Structure of YUV vs. RGB
 
YUV Color Space
 
YUV is a color encoding system that separates an image into luminance (Y) and chrominance (U and V) components:
 
Y (Luminance): Represents the brightness of the pixel. This is similar to grayscale information.
 
U (Chrominance blue): Represents the difference between the blue color channel and the brightness.
 
V (Chrominance red): Represents the difference between the red color channel and the brightness.
 
 
YUV color space is often used in video and image compression formats because human vision is more sensitive to changes in brightness than color. By separating these components, the chrominance channels (U and V) can be subsampled, reducing bandwidth without much perceptual loss in quality.
 
RGB Color Space
 
RGB represents images using three color channels:
 
R (Red)
 
G (Green)
 
B (Blue)
 
 
Each channel holds information about the intensity of that color. RGB is commonly used in displays because it directly maps to how screens generate color by combining red, green, and blue light.
 
YUV vs. RGB Comparison
 
YUV separates brightness (Y) from color (U and V), allowing for subsampling of the chrominance components. This results in better compression while maintaining visual quality.
 
RGB directly represents the color in three channels but requires more bandwidth since it does not allow for easy subsampling.
 
 
YUV Subsampling Formats
 
4:4:4: No subsampling, U and V have the same resolution as Y.
 
4:2:2: U and V are halved in horizontal resolution, reducing bandwidth.
 
4:2:0: U and V are halved in both horizontal and vertical resolution.
 
 
2. Compression of RGB/YUV to JPEG
 
JPEG Compression Process
 
JPEG compression is a widely used method to reduce the size of images, both in RGB and YUV formats. The process involves several stages:
 
1. Color Space Conversion:
 
If the image is in RGB format, it is first converted to YUV (usually YCbCr, a digital version of YUV) because YUV allows for more efficient compression.
 
 
 
2. Subsampling (in YUV format):
 
The U and V chrominance channels are often subsampled (e.g., 4:2:0) since the human eye is less sensitive to color detail compared to brightness. This reduces the size of the color information by reducing resolution in these channels.
 
 
 
3. Block Splitting:
 
The image is divided into 8x8 blocks of pixels in the YUV channels.
 
 
 
4. Discrete Cosine Transform (DCT):
 
Each 8x8 block undergoes a DCT transformation, which converts the spatial domain data into the frequency domain. This helps separate the image into low-frequency and high-frequency components.
 
 
 
5. Quantization:
 
The DCT coefficients are then quantized (reduced precision) based on a quantization matrix. Lower precision is given to higher frequencies because the human eye is less sensitive to fine details (high frequencies).
 
 
 
6. Entropy Encoding:
 
The quantized data is then entropy encoded using techniques like Huffman coding or Arithmetic coding to further compress the image.
 
 
 
7. JPEG File Structure:
 
The final JPEG file contains a header (with metadata and quantization tables), followed by the compressed image data.
 
 
 
 
3. JPEG File Structure
 
A typical JPEG file is structured as follows:
 
SOI (Start of Image): Marks the beginning of the image.
 
APP0 (JFIF Header): Contains metadata like resolution, aspect ratio, etc.
 
Quantization Tables: Tables used during quantization, which are stored in the file for decompression.
 
Huffman Tables: Used for entropy encoding.
 
Start of Frame (SOF): Indicates the image size and number of components (Y, U, V or R, G, B).
 
Compressed Data: Entropy encoded DCT coefficients.
 
End of Image (EOI): Marks the end of the image.
 
 
4. Mobileye Camera Sensor Data Transmission
 
Over CAN Bus
 
The CAN (Controller Area Network) bus is typically used in automotive systems to transfer data between sensors and control units, including camera data. The CAN bus is a relatively low-bandwidth protocol (typically 1 Mbps in traditional CAN, though CAN FD supports higher speeds up to 5 Mbps). Because of this limitation, the camera does not stream full video over CAN. Instead, processed data such as:
 
Object detection results (bounding boxes, classifications).
 
Lane detection information.
 
Traffic sign recognition results.
 
Free space estimation.
 
 
The frequency at which data is transmitted over CAN from a Mobileye sensor is typically 30 to 60 Hz (i.e., once per frame or more). However, this can vary based on the vehicle configuration, processing load, and specific task.
 
Over Ethernet (for H.264 video stream)
 
In some systems, especially for full video streaming, data may be sent over a high-speed Ethernet connection, particularly when compressing video using H.264 format. H.264 (also known as AVC) is a widely used video compression standard that efficiently compresses video data while maintaining high quality.
 
Data Rate: When streaming video over Ethernet using H.264, the bitrate depends on the resolution, frame rate, and compression settings. Typically, H.264 streams can range from 500 kbps to several Mbps depending on the configuration.
 
Frame Rate: Typically, 30-60 frames per second (FPS), depending on the system setup and application.
 
 
Since Ethernet provides much higher bandwidth than CAN, Mobileye camera sensors may stream full-frame video data at 30 FPS or higher, depending on the application needs. The H.264 format allows this video to be compressed effectively, reducing the bandwidth needed while maintaining the necessary detail for perception tasks.
 
5. Focal Length of Mobileye Camera Sensors
 
The focal length of a camera lens is the distance between the lens and the image sensor when the subject is in focus. It determines the field of view (FoV) of the camera. For example:
 
A short focal length (e.g., 2.5 mm) results in a wide FoV.
 
A long focal length (e.g., 6 mm) provides a narrower FoV, which is better for focusing on distant objects.
 
 
In Mobileye systems:
 
Forward-facing cameras tend to have a longer focal length to detect objects at greater distances (e.g., vehicles, pedestrians).
 
Side and rear cameras often have a wider FoV to cover more area around the vehicle, useful for tasks like lane keeping and cross-traffic detection.
 
 
Summary:
 
YUV and RGB are different color spaces; YUV separates brightness from color, enabling better compression.
 
Both YUV and RGB data can be compressed into JPEG using color space conversion, subsampling, DCT, quantization, and entropy encoding.
 
Mobileye camera sensors send processed data (like object detection results) over CAN bus at 30-60 Hz, and for full video streams, they may use H.264 compression over Ethernet.
 
H.264 streams can vary in bitrate depending on resolution and compression settings but generally allow for efficient video transmission.
