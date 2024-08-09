import os
from pathlib import Path
from kitti import kitti_utils
import open3d as o3d

class KITTIDataset():
    '''Load KITT data and parse data into a usable format.'''

    def __init__(self, root_dir: str='/data/kitti', split: str = 'training'):
        '''root_dir should contain training and testing folders of KITTI dataset.'''
        self.root_dir = root_dir
        self.split_dir = os.path.join(root_dir, split)
        self.calib_dir = os.path.join(self.split_dir, 'calib')
        self.image_2_dir = os.path.join(self.split_dir, 'image_2')
        self.label_2_dir = os.path.join(self.split_dir, 'label_2')
        self.velodyne_dir = os.path.join(self.split_dir, 'velodyne')
        self.num_samples = self._count_files_in_directory(self.label_2_dir)
        self.current_sample = 1

    def __len__(self):
        return self.num_samples

    def __iter__(self):
        return self
    
    def __next__(self):
        self.current_sample += 1
        if self.current_sample < self.num_samples:
            return self
        raise StopIteration

    def _count_files_in_directory(self, directory_path):
        path = Path(directory_path)
        return sum(1 for entry in path.iterdir() if entry.is_file())

    def get_lidar(self, idx: int):
        assert(idx < self.num_samples)
        lidar_file_name = os.path.join(self.velodyne_dir, '%06d.bin'%(idx))
        return kitti_utils.load_velodyne_sensor_data(lidar_file_name)

    def get_label(self, idx: int):
        assert(idx < self.num_samples)
        label_file_name = os.path.join(self.label_2_dir, '%06d.txt'%(idx))
        return kitti_utils.read_label(label_filename=label_file_name)


    def get_lidar_pcl(self, idx: int) -> o3d.geometry.PointCloud:
        assert(idx < self.num_samples)
        lidar_file_name = os.path.join(self.velodyne_dir, '%06d.bin'%(idx))
        return kitti_utils.bin_to_pcd(bin_file=lidar_file_name)

    def get_lidar_pcl(self) -> o3d.geometry.PointCloud:
        lidar_file_name = os.path.join(self.velodyne_dir, '%06d.bin'%(self.current_sample))
        return kitti_utils.bin_to_pcd(bin_file=lidar_file_name)