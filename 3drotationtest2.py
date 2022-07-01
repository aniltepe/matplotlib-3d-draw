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
    ax.view_init(elev = 130, azim = -130)

def rotateVectorAroundAxis(vec, axis, angle):
    axis /= np.linalg.norm(axis)
    return  np.add(np.add(vec * math.cos(math.radians(angle)), np.cross(axis, vec) * math.sin(math.radians(angle))), axis * np.dot(axis, vec) * (1 - math.cos(math.radians(angle))))

def yaw(front, right, up, angle):
    front = rotateVectorAroundAxis(front, up, angle)
    right = rotateVectorAroundAxis(right, up, angle)
    return front, right, up

def pitch(front, right, up, angle):
    up = rotateVectorAroundAxis(up, right, angle)
    front = rotateVectorAroundAxis(front, right, angle)
    return front, right, up

def roll(front, right, up, angle):
    right = rotateVectorAroundAxis(right, front, angle)
    up = rotateVectorAroundAxis(up, front, angle)
    return front, right, up


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

front = np.array([0., 0., -1.])
right = np.array([1., 0., 0.])
up = np.array([0., 1., 0.])


front, right, up = yaw(front, right, up, 30)
drawVector(front, 'red')
drawVector(right, 'green')
drawVector(up, 'blue')
front, right, up = pitch(front, right, up, 30)
# front, right, up = roll(front, right, up, 30)

drawVector(front, 'cyan')
drawVector(right, 'magenta')
drawVector(up, 'yellow')

drawLegend()
plt.show()
