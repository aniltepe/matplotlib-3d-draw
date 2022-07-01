import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import math


def drawVector(vec3, color):
    zero_concat_vec3 = np.concatenate((np.array([0., 0., 0.]), vec3)).reshape(1, 6)
    v1, v2, v3, v4, v5, v6 = zip(*zero_concat_vec3)
    return ax.quiver(v1, v2, v3, v4, v5, v6, color = color)

def drawLegend():
    axis_lines = np.array(
        [[0, 0, 0, 2, 0, 0],
        [0, 0, 0, -2, 0, 0],
        [0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, -2, 0],
        [0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, -2]])
    X, Y, Z, U, V, W = zip(*axis_lines)
    ax.quiver(X, Y, Z, U, V, W)
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_proj_type('ortho')
    ax.view_init(elev = 25, azim = 35)

def rotateVectorAroundAxis(vec, axis, angle):
    return  np.add(np.add(vec * math.cos(math.radians(angle)), np.cross(axis, vec) * math.sin(math.radians(angle))), axis * np.dot(axis, vec) * (1 - math.cos(math.radians(angle))))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

vec = np.array([0., -0.707, 0.707]) 
axis = np.array([0., 0.707, 0.707])

drawVector(vec, 'red')
drawVector(axis, 'blue')

rotated = rotateVectorAroundAxis(vec, axis, 270)

drawVector(rotated, 'green')


drawLegend()
plt.show()
