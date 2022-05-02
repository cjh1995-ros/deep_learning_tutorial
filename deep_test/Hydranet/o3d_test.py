import numpy as np
import time
import open3d as o3d
import matplotlib.pyplot as plt

pcd = o3d.io.read_point_cloud("test.pcd")
o3d.visualization.draw_geometries([pcd])