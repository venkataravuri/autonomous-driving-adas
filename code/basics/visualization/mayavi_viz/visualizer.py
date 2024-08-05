
from mayavi import mlab
from ..kitti_dataset import KITTIDataset
import logging

logger = logging.getLogger(__name__)

def draw_lidar(pc, pc_label, color=None, fig=None, bgcolor=(0,0,0), pts_scale=1, pts_mode='point', pts_color=None):
    ''' Draw lidar points
    Args:
        pc: numpy array (n,3) of XYZ
        color: numpy array (n) of intensity or whatever
        fig: mayavi figure handler, if None create new one otherwise will use it
    Returns:
        fig: created or used fig
    '''
    
    if fig is None: fig = mlab.figure(figure=None, bgcolor=bgcolor, fgcolor=None, engine=None, size=(1600, 1000))
    
    color_list = [(1, 1, 125/255),
                (0, 1, 1),
                (0.5, 0.5, 0.5),
                (1, 0, 0), 
                (0, 1, 125/255),
                (0, 0, 1),
                (0, 125/255, 1),
                (125/255, 1, 0),
                (0, 1, 0)]

    mlab.points3d(pc[:,0], pc[:,1], pc[:,2],  color=color_list[1], mode=pts_mode, colormap = 'gnuplot', scale_factor=pts_scale, figure=fig) 

    lidar_label = pc_label 

    for idx in range(len(lidar_label)):
        color=(0,0,1)
        line_width=1
        bbox = lidar_label[idx]

        b = convert_bbox_to_corners(bbox)#
        # print('189: the size of b is: ', b.shape)
        # min_x, min_y, min_z, max_x, max_y, max_z, length_x, length_y, length_z
        
        for k in range(0,4):
            #http://docs.enthought.com/mayavi/mayavi/auto/mlab_helper_functions.html
            i,j=k,(k+1)%4#below
            mlab.plot3d([b[i,0], b[j,0]], [b[i,1], b[j,1]], [b[i,2], b[j,2]], color=color, tube_radius=None, line_width=line_width)#, figure=fig)

            i,j=k+4,(k+1)%4 + 4#above
            mlab.plot3d([b[i,0], b[j,0]], [b[i,1], b[j,1]], [b[i,2], b[j,2]], color=color, tube_radius=None, line_width=line_width)#, figure=fig)

            i,j=k,k+4
            mlab.plot3d([b[i,0], b[j,0]], [b[i,1], b[j,1]], [b[i,2], b[j,2]], color=color, tube_radius=None, line_width=line_width)#, figure=fig)



    middle_idx = 3000#00#pc.shape[0] / 2#
    mlab.view(azimuth=270, elevation=0, focalpoint=[ pc[middle_idx,0], pc[middle_idx,1], pc[middle_idx,2]], distance=10.0, figure=fig)

    return fig

def convert_bbox_to_corners(bbox):
    # min_x, min_y, min_z, max_x, max_y, max_z, length_x, length_y, length_z
    l = bbox.l# bbox(8)#[8]
    h = bbox.h#bbox[9]
    w = bbox.w#bbo
    center = bbox.t#[data[11],data[12],data[13]]
    # 3d bounding box corners 根据中心点和长宽高，把 8个顶点的坐标求出来
    x_corners = [l/2,l/2,-l/2,-l/2,l/2,l/2,-l/2,-l/2];
    y_corners = [h/2,h/2,h/2,h/2,-h/2,-h/2,-h/2,-h/2];
    z_corners = [w/2,-w/2,-w/2,w/2,w/2,-w/2,-w/2,w/2];
    
    # rotate and translate 3d bounding box
    corners_3d = np.vstack([x_corners,y_corners,z_corners])#沿着竖直方向将矩阵堆叠起来
    #print corners_3d.shape
    # print('226: the size of corner 3d is: ', corners_3d.shape)
    corners_3d[0,:] = corners_3d[0,:] + center[0]
    corners_3d[1,:] = corners_3d[1,:] + center[1]
    corners_3d[2,:] = corners_3d[2,:] + center[2]
    return np.transpose(corners_3d)


def show_lidar(point_cloud_velo, point_cloud_label, img_fov=False):
    ''' Show all LiDAR points.
        Draw 3d box in LiDAR point cloud (in velo coord system) '''

    fig = mlab.figure(figure=None, bgcolor=(1,1,1), fgcolor=None, engine=None, size=(1000, 500))

    draw_lidar(point_cloud_velo, point_cloud_label, fig=fig)

    mlab.show(1)


def dataset_viz():
    dataset = KITTIDataset()

    idx : int = 7480

    point_cloud = dataset.get_lidar(idx)[:,0:7]
    pint_cloud_label = dataset.get_label(idx)[:,0]

if __name__ == '__main__':
    dataset_viz()