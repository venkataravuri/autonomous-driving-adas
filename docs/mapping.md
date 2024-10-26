# Mapping & Localization

In the realm of autonomous driving, mapping is vital for navigation and situational awareness.

**Mapping** involves creating a representation of the environment, which can include static objects like  road boundaries, lane delimiters, centerlines, direction of travel and crosswalks, buildings and dynamic objects such as pedestrians and other vehicles.It is a process of predicting map elements for a given set of surround view images and lidar point clouds.

**Localization** is the process of determining the vehicle's position within that map. This is essential for navigation, obstacle avoidance, and path planning.

## Map Categores

The main types of maps utilized include,
- Topological maps
- High-definition (HD) maps
- and Mapless autonomous driving.

## Topological Maps
Topological maps represent the environment based on the connectivity and relationships between various locations (e.g., intersections, routes) rather than precise geometrical details. They emphasize the paths and routes available, making them useful for navigation tasks that require understanding of how different areas are connected.

Topological maps includes attributes like road topology, lane topology (number of lanes), building footprints, street segments, direction of travel, parking lots. They are useful to know how to get from point A to point B.

Data used to assemble these maps are produced from cameras mounted on dashboards (can be crowdsourced), aerial imagery from satelites, planes and drones.

#### What are different approaches to assemble toplogical maps?

- Segmentation followed by Heuristics - Usually done through Road pixel binary semantic segmentation on aerial imagery followed by heuristic to get the road network. It is subjected to challenges such as partial occlusion or an unexpected angle in areal imagery.
- Engergy based
- Neural Network

## High-Definition (HD) Maps
HD maps are highly detailed representations of the environment, essential for advanced autonomous driving systems. They provide centimeter-level accuracy and include intricate details about road geometry, traffic signs, lane markings, and other critical features.

High-definition (HD) maps offer an intricate and precise depiction of the road, encompassing lane markings, traffic signs, and other critical features.

HD Maps contain both geometric structure information as well as semantics.

<img src="https://geospatialmedia.s3.amazonaws.com/wp-content/uploads/2016/04/here-1.jpg" height="50%" width="50%" />

Types of HD Maps,

- **Offline HD Maps**:
 - Created using extensive data collection methods such as LiDAR, cameras, and GPS.
 - Typically updated periodically based on new data or changes in the environment.
 - Used for detailed planning and simulation.

- **Online HD Maps**:
 - Updated in real-time or near-real-time using sensor data from vehicles.
 - Allow for dynamic changes in the environment to be reflected immediately.
 - Essential for applications requiring immediate responsiveness to changing conditions.

#### What are different HD map layers?

HD Map is organized into layers. 

<img src="https://geospatialmedia.s3.amazonaws.com/wp-content/uploads/2019/01/HD-Maps-Layers-20190107.png" height="30%" width="30%" />

| Layer | Mappying Information | ? |
| --- | --- | --- |
| 1 | Topological Representation | Topology captures how roads, lanes, intersections, and other features are connected |
| 2 | Geometric Representation | Geometric features include the shapes and positions of roads, lanes, sidewalks, buildings, and terrain. These features are typically represented using a vector data structure, which describes simplified geometric shapes such as points, lines, curves, circles, and polygon. |
| 3 | Semantic Representation | Semantic representation includes various traffic 2D and 3D objects such as lane boundaries, intersections, crosswalks, parking spots, stop signs, traffic lights, road speed limits, lane information, and road classification |
| 4 | Dynamic elements |  Dynamic elements like pedestrians, obstacles, and vehicles need to be updated for the HD map to be always precise and accurate. The dynamic element layer of HD maps captures and represents these time-varying aspects of the environment, which are essential for safe and efficient path planning and decision-making. |
| 5 | Feature-Based Map Layers | HD maps rely heavily on advanced feature-based map layers for accurate localization and navigation. These layers use various techniques to identify and match features in the environment to ensure precise vehicle positioning. |

### What are different HD Maps formats?

|Dataset| Format | Description File | Format Representations |
| --- | --- | --- | --- |
|Argoverse 2, nuScenes, CommonRoad| Lanelet2 | HD map format for autonomous driving XML, OSM | Points |
|KITTI Dataset| OpenDRIVE | Standard for logical description of road networks | XML Geometric primitives |
| Waymo Open Dataset| Custom proprietary| Detailed HD maps from Waymo's autonomous vehicles.||

## Lanelet2 HDMap Format

Lanelet2 maps are organized into three main layers:
- **Physical Layer**:
  - Contains observable elements such as lane boundaries, road markings, and traffic signs.
  - Represents the real-world features that can be detected by sensors.
- **Relational Layer**:
  - Defines the relationships between physical elements (e.g., which lanes connect to which intersections).
  - Includes regulatory elements that represent traffic rules like stop signs and traffic lights.
- **Topological Layer**:
  - Combines elements from the relational layer into a network of drivable areas.
  - This layer helps in understanding navigable paths and potential interactions between different road users.

<details>
<summary>Lanelet 2 sample</summary>
 
```xml
 <laneletMap>
    <lanelets>
        <lanelet id="1">
            <lineString>
                <point x="1.0" y="1.0"/>
                <point x="1.0" y="5.0"/>
            </lineString>
            <regulatoryElement>
                <trafficLight id="tl1" state="green"/>
            </regulatoryElement>
        </lanelet>
        <lanelet id="2">
            <lineString>
                <point x="1.0" y="5.0"/>
                <point x="5.0" y="5.0"/>
            </lineString>
        </lanelet>
    </lanelets>
    <regulatoryElements>
        <trafficLight id="tl1" position="1.0, 5.0" state="green"/>
    </regulatoryElements>
</laneletMap>
```

</details>

### OpenDRIV HDMap Format

OpenDRIVE files typically have the .xodr extension and are organized into several key components:

- **Header**: Contains metadata about the road network, including version information and timestamps.
- **Roads**: Defines individual roads, including their geometry and attributes.
- **Lanes**: Specifies lane details such as width, type, and markings.
- **Junctions**: Describes how roads connect to each other.
- **Objects**: Includes static features like traffic signs and signals.

<details>
<summary>OpenDRIVE Sample</summary>
 
```xml
<OpenDRIVE xmlns="http://www.opendrive.org/schema/1.6">
    <header>
        <revision>1.6</revision>
        <name>Sample Road Network</name>
        <date>2024-10-26T12:00:00</date>
    </header>
    <road id="1" length="1000" junction="-1">
        <line>
            <start x="0" y="0" z="0"/>
            <end x="1000" y="0" z="0"/>
        </line>
        <lanes>
            <lane id="1" type="driving" level="0">
                <width>
                    <laneWidth sOffset="0" a="3.5"/>
                </width>
                <roadMark>
                    <type>solid</type>
                    <color>white</color>
                </roadMark>
            </lane>
            <lane id="2" type="driving" level="0">
                <width>
                    <laneWidth sOffset="0" a="3.5"/>
                </width>
                <roadMark>
                    <type>dashed</type>
                    <color>yellow</color>
                </roadMark>
            </lane>
        </lanes>
    </road>
    <junction id="1">
        <connection incomingRoadId="1" outgoingRoadId="2"/>
    </junction>
</OpenDRIVE>
```

</details>

### HD Map Generation ML Models

- [HDMapNet: An Online HD Map Construction and Evaluation Framework](https://arxiv.org/pdf/2107.06307)
- [MapTRv2: An End-to-End Framework for Online Vectorized HD Map Construction](https://arxiv.org/pdf/2308.05736)
-  PoseNet and VLocNet++, are some of the frameworks that use point data to estimate the 3D position and orientation. These estimated 3D positions and orientations can be used to derive scene semantics, as seen in the image below.


## Mapless Autonomous Driving
Mapless autonomous driving refers to systems that navigate without relying on pre-defined maps. Instead, these systems utilize real-time sensor data to understand their environment and make decisions.

Characteristics:
- Can adapt to completely new environments without prior knowledge.
- Often employs techniques like SLAM (Simultaneous Localization and Mapping) to build a map on-the-fly while localizing itself.

Mapless autonomous driving leverages a combination of cameras and sensors to create a dynamic perception map of the vehicle’s surroundings without relying on pre-loaded HD maps.

Companies like Imagry, Deeproute, Tesla was the frontrunner among OEMs adopting Mapless AD for its lineup using FSD, other OEMs such as Xpeng, Huawei AITO, GAC Aion and Li Auto have also adopted Mapless.

Map-based AD systems depend on detailed pre-loaded HD maps, which are regularly updated to ensure accuracy and reliability. Major players like Google, HERE, and TomTom provide these comprehensive maps, which enhance navigation and route guidance. 

[MapVision: CVPR 2024 Autonomous Grand Challenge Mapless Driving Tech Report](https://arxiv.org/pdf/2406.10125v1)


## Localization

Localization module tells the car where you are in the 3D space, and what’s actually around you.

Localization algorithms in self-driving cars calculate the position and orientation of the vehicle as it navigates – a science known as Visual Odometry (VO).

VO works by matching key points in consecutive video frames. With each frame, the key points are used as the input to a mapping algorithm. The mapping algorithm, such as Simultaneous localization and mapping (SLAM), computes the position and orientation of each object nearby with respect to the previous frame and helps to classify roads, pedestrians, and other objects around.

### References

- [A Comprehensive Survey on High-Definition Map Generation and Maintenance](https://www.mdpi.com/2220-9964/13/7/232)
