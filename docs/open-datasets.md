
### KITTI Dataset

KITTI is a popular computer vision dataset designed for autonomous driving research. It contains a diverse set of challenges for researchers, including object detection, tracking, and scene understanding. The dataset is derived from the autonomous driving platform developed by the Karlsruhe Institute of Technology and the Toyota Technological Institute at Chicago.

The KITTI dataset includes a collection of different sensors and modalities, such as stereo cameras, LiDAR, and GPS/INS sensors, which provides a comprehensive view of the environment around the vehicle. The data was collected over several days in the urban areas of Karlsruhe and nearby towns in Germany. The dataset includes more than 200,000 stereo images and their corresponding point clouds, as well as data from the GPS/INS sensors, which provide accurate location and pose information.

KITTI dataset is a widely used computer vision dataset for training and evaluating algorithms for tasks like object detection, 3D object tracking, and scene understanding. 

- [Explain label file of kitti dataset](https://medium.com/@abdulhaq.ah/explain-label-file-of-kitti-dataset-738528de36f4)
- [KITTI calibration file explained P0–3, R0_rect, Tr_velo_to_cam, and Tr_imu_to_velo](https://medium.com/@abdulhaq.ah/kitti-calibration-file-explained-p0-3-r0-rect-tr-velo-to-cam-and-tr-imu-to-velo-fb47b3f254e6)

[Exploring KITTI Dataset: Visual Odometry for autonomous vehicles](https://medium.com/@jaimin-k/exploring-kitti-visual-ododmetry-dataset-8ac588246cdc)

### LiDAR Data Annotation & Labeling

LiDAR point cloud data requires annotation and labeling to be used for training autonomous vehicles.
- Object Detection: Annotators identify and label objects within the point cloud, including cars, pedestrians, cyclists, and other relevant objects.
- Semantic Segmentation: Assigning a label to each point in the cloud, creating a pixel-wise segmentation of objects and their boundaries.
- Instance Segmentation: Separating individual instances of the same object class, such as distinguishing between different vehicles.
- 3D Bounding Boxes: Defining 3D bounding boxes around objects, including their dimensions, orientation, and location in 3D space.
- Lane and Road Markings: Annotating the road layout, lane markings, and other navigational information.

### Annotaiton Tools

- MOSAIK Suite from MicroVision