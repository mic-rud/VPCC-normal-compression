import numpy as np
import pptk
import os


def load_ply(filename):
    if not os.path.exists(filename):
        print("File is not existant")
        return 

    lines = []
    with open(filename, "r") as file:
        lines = file.readlines()

    headerSize = 0
    for l in lines:
        headerSize = headerSize + 1
        if l == "end_header\n":
            break

        if headerSize == 15:
            break

    header = lines[:headerSize]
    data = np.genfromtxt(filename, delimiter=' ', skip_header=headerSize) 
    print(data.shape)
    points = np.vstack((data[:,2], data[:,0], data[:,1])).transpose()
    colors = np.vstack((data[:,3], data[:,4], data[:,5])).transpose()
    return points, colors

def create_viewer(points, colors):
    v = pptk.viewer(points)
    v.attributes(colors/255)
    v.set(point_size=0.1, bg_color=[0,0,0,0], show_axis=0, show_grid=0)
    return v



filename = "./S26C03R03_rec_1051.ply"
points, colors = load_ply(filename)
v = create_viewer(points, colors)

filename = "../../../mpeg_datasets/CfP/datasets/Dynamic_Objects/People/8i/8iVFBv2/longdress/Ply/longdress_vox10_1051.ply"
points, colors = load_ply(filename)
v = create_viewer(points, colors)


