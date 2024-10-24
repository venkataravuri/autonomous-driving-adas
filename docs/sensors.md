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


<img align="right" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRexJXGGhK719BgaGSQI5BouU79zlI-NWCOlql5wlISgRugJOwWsFUU1bUw7HBjD1j52u8" width="30%" height="30%" />

# LiDAR - Light Detection and Ranging

LiDAR device functions by emitting laser (light) pulses and measuring the duration it takes for these pulses to return after bouncing off of things. This time delay, known as the “time of flight”, is used to calculate precise distances, allowing for the creation of detailed three-dimensional maps of the environment.

- LiDAR sensor readings are given in a set of 3D coordinates called a Point Cloud (PCL), which gives accurate depth information of each point’s surroundings and intensity levels. 
- LiDAR sensors capture millions of data points per second, creating dense point clouds that represent the vehicle's surroundings in rich 3D scenes of environment.
- Point clouds are rich in spatial information, they lack semantic context.
- Point clouds represent the world in 3D. The LiDAR sensor gets the exact (X,Y,Z) position of every impact point.
- LiDARs don’t work well in bad weather conditions. In cases of fog, the lasers can hit it and muddle the scene. Similar to rain drops or dirt.

> RADARs measure the world by sending radio waves, and SONARs sending sound waves, LiDAR do it using light waves.


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