import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

inputs = ['normals6.txt', 'normals10.txt', 'normals18.txt']
for input_name in inputs:
    data = np.genfromtxt(input_name, delimiter=',')
    print(data.shape)

    fig = plt.figure
    ax = plt.axes(projection='3d')

    num_clusters = int(np.max(data[:,3]) + 1)
    #Center data
    means = np.mean(data, axis=0)
    print(means[:3])
    data[:, :3] = data[:, :3] - means [:3]

    for i in range(num_clusters):
        points = [point[:3] for point in data if point[3] == i]
        points = np.array(points).transpose()
        if len(points) == 0:
            continue
        ax.scatter3D(points[0], points[2], points[1], s=.1)

    max_range = np.max(data)
    min_range = np.min(data)
    ax.set_xlim3d(min_range, max_range)
    ax.set_ylim3d(min_range, max_range)
    ax.set_zlim3d(min_range, max_range)
    ax.dist = 6
    ax.set_axis_off()

    ax.view_init(elev=15., azim=120)
    plt.savefig(input_name.replace('.txt', '_1.png'), bbox_inches='tight', dpi=300)
    ax.view_init(elev=15., azim=60)
    plt.savefig(input_name.replace('.txt', '_2.png'), bbox_inches='tight', dpi=300)
