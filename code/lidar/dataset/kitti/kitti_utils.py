from typing import List
import numpy as np
import logging
import open3d as o3d
import struct

logger = logging.getLogger(__name__)

class Object3d():
    def __init__(self, label_line: str):
        data = label_line.split(' ')
        data[1:] = [float(x) for x in data[1:]]

        # extract label, truncation, occlusion
        self.type = data[0] # Cloud be 'car', 'pedestrian', ...
        self.truncation = data[1] # truncated pixel ratio [0..1]
        self.occlusion = int(data[2]) # 0=visible, 1=partly occluded, 2=fully occluded, 3=unknown
        self.alpha = data[3] # object observation angle [-pi..pi]

        # extract 2d bounding box in 0-based coordinates
        self.xmin = data[4] # left
        self.ymin = data[5] # top
        self.xmax = data[6] # right
        self.ymax = data[7] # bottom
        self.box2d = np.array([self.xmin,self.ymin,self.xmax,self.ymax])

        # extract 3d bounding box information
        self.h = data[8] # box height
        self.w = data[9] # box width
        self.l = data[10] # box length (in meters)
        self.t = (data[11],data[12],data[13]) # location (x,y,z) in camera coord.
        self.ry = data[14] # yaw angle (around Y-axis in camera coordinates) [-pi..pi]

    def __str__(self):
        return f"""Type: {self.type}, truncation: {self.truncation}, occlusion: {self.occlusion}, alpha: {self.alpha} \n \
            2d bbox (x0,y0,x1,y1): ({self.xmin}, {self.ymin}, {self.xmax}, {self.ymax}) \n \
            3d bbox h,w,l: ({self.h}, {self.w}, {self.l}) \n \
            3d bbox location, ry: ({self.t[0]},{self.t[1]},{self.t[2]},{self.ry})"""

    def __repr__(self):
        return self.__str__()

def load_velodyne_sensor_data(velodyne_sensor_data_filename: str):
    # read raw data from binary
    scan = np.fromfile(velodyne_sensor_data_filename, dtype=np.float32)
    # Reshape the array into a ?x4 matrix, automatically calculating the first dimension
    points = scan.reshape(-1, 4)[:, 0:3] # Lidar xyz (front, left, up)
    logger.debug(f"Points shape: {points.shape}")
    return points

def read_label(label_filename: str) -> List[Object3d] :
    lines = [line.rstrip() for line in open(label_filename)]
    return [Object3d(line) for line in lines]



def bin_to_pcd(bin_file: str) -> o3d.geometry.PointCloud:
    size_float: int = 4
    list_pcd = []
    with open(bin_file, "rb") as f:
        byte = f.read(size_float * 4)
        while byte:
            x, y, z, intensity = struct.unpack("ffff", byte)
            list_pcd.append([x, y, z])
            byte = f.read(size_float * 4)

    np_pcd = np.asarray(list_pcd)
    pcd = o3d.geometry.PointCloud()
    v3d = o3d.utility.Vector3dVector
    pcd.points = v3d(np_pcd)

    return pcd