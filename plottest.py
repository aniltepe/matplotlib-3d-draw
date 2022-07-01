import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import math


def drawVector(vec3, color):
    zero_concat_vec3 = np.concatenate((np.array([0., 0., 0.]), vec3)).reshape(1, 6)
    v1, v2, v3, v4, v5, v6 = zip(*zero_concat_vec3)
    return ax.quiver(v1, v2, v3, v4, v5, v6, color = color)

def drawShadows(vec3):
    xaxis_x = np.linspace(0, 0, 2)
    xaxis_y = np.linspace(0, vec3[1], 2)
    xaxis_z = np.linspace(0, vec3[2], 2)
    ax.plot3D(xaxis_x, xaxis_y, xaxis_z, ':k')
    xaxis_y_x = np.linspace(0, 0, 2)
    xaxis_y_y = np.linspace(vec3[1], vec3[1], 2)
    xaxis_y_z = np.linspace(0, vec3[2], 2)
    ax.plot3D(xaxis_y_x, xaxis_y_y, xaxis_y_z, ':k')
    xaxis_z_x = np.linspace(0, 0, 2)
    xaxis_z_y = np.linspace(0, vec3[1], 2)
    xaxis_z_z = np.linspace(vec3[2], vec3[2], 2)
    ax.plot3D(xaxis_z_x, xaxis_z_y, xaxis_z_z, ':k')
    xaxis_x_x = np.linspace(0, vec3[0], 2)
    xaxis_x_y = np.linspace(vec3[1], vec3[1], 2)
    xaxis_x_z = np.linspace(vec3[2], vec3[2], 2)
    ax.plot3D(xaxis_x_x, xaxis_x_y, xaxis_x_z, ':k')


    yaxis_x = np.linspace(0, vec3[0], 2)
    yaxis_y = np.linspace(0, 0, 2)
    yaxis_z = np.linspace(0, vec3[2], 2)
    ax.plot3D(yaxis_x, yaxis_y, yaxis_z, ':k')
    yaxis_x_x = np.linspace(vec3[0], vec3[0], 2)
    yaxis_x_y = np.linspace(0, 0, 2)
    yaxis_x_z = np.linspace(0, vec3[2], 2)
    ax.plot3D(yaxis_x_x, yaxis_x_y, yaxis_x_z, ':k')
    yaxis_z_x = np.linspace(0, vec3[0], 2)
    yaxis_z_y = np.linspace(0, 0, 2)
    yaxis_z_z = np.linspace(vec3[2], vec3[2], 2)
    ax.plot3D(yaxis_z_x, yaxis_z_y, yaxis_z_z, ':k')
    yaxis_y_x = np.linspace(vec3[0], vec3[0], 2)
    yaxis_y_y = np.linspace(0, vec3[1], 2)
    yaxis_y_z = np.linspace(vec3[2], vec3[2], 2)
    ax.plot3D(yaxis_y_x, yaxis_y_y, yaxis_y_z, ':k')


    zaxis_x = np.linspace(0, vec3[0], 2)
    zaxis_y = np.linspace(0, vec3[1], 2)
    zaxis_z = np.linspace(0, 0, 2)
    ax.plot3D(zaxis_x, zaxis_y, zaxis_z, ':k')
    zaxis_x_x = np.linspace(vec3[0], vec3[0], 2)
    zaxis_x_y = np.linspace(0, vec3[1], 2)
    zaxis_x_z = np.linspace(0, 0, 2)
    ax.plot3D(zaxis_x_x, zaxis_x_y, zaxis_x_z, ':k')
    zaxis_y_x = np.linspace(0, vec3[0], 2)
    zaxis_y_y = np.linspace(vec3[1], vec3[1], 2)
    zaxis_y_z = np.linspace(0, 0, 2)
    ax.plot3D(zaxis_y_x, zaxis_y_y, zaxis_y_z, ':k')
    zaxis_z_x = np.linspace(vec3[0], vec3[0], 2)
    zaxis_z_y = np.linspace(vec3[1], vec3[1], 2)
    zaxis_z_z = np.linspace(0, vec3[2], 2)
    ax.plot3D(zaxis_z_x, zaxis_z_y, zaxis_z_z, ':k')

def drawLegend():
    axis_lines = np.array(
        [[0, 0, 0, 10, 0, 0],
        [0, 0, 0, -10, 0, 0],
        [0, 0, 0, 0, 10, 0],
        [0, 0, 0, 0, -10, 0],
        [0, 0, 0, 0, 0, 10],
        [0, 0, 0, 0, 0, -10]])
    X, Y, Z, U, V, W = zip(*axis_lines)
    ax.quiver(X, Y, Z, U, V, W)
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_zlim([-5, 5])
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_proj_type('ortho')
    ax.view_init(elev = 130, azim = -130)

def calculateRotatedVec(vec3, yaw, pitch, roll):
    rotated = vec3

    # z-axis - yaw
    rotated = np.array([rotated[0] * math.cos(math.radians(roll)) - rotated[1] * math.sin(math.radians(roll)),
        rotated[0] * math.sin(math.radians(roll)) + rotated[1] * math.cos(math.radians(roll)), rotated[2]])

    # y-axis - pitch
    rotated = np.array([rotated[0] * math.cos(math.radians(yaw)) + rotated[2] * math.sin(math.radians(yaw)),
        rotated[1], -1 * rotated[0] * math.sin(math.radians(yaw)) + rotated[2] * math.cos(math.radians(yaw))])
    
    # x-axis - roll
    rotated = np.array([rotated[0], rotated[1] * math.cos(math.radians(pitch)) - rotated[2] * math.sin(math.radians(pitch)),
        rotated[1] * math.sin(math.radians(pitch)) + rotated[2] * math.cos(math.radians(pitch))])

    
    return rotated

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

cameraCenter = np.array([0., 0., 0.])
cameraPos = np.array([0., 0., 5.]) 
cameraUp = np.array([0., 5., 0.])

yaw = 0
pitch = 20
roll = 40

cameraLook = cameraCenter - cameraPos
look = calculateRotatedVec(cameraLook, yaw, pitch, roll)
drawVector(look, 'black')
up = calculateRotatedVec(cameraUp, yaw, pitch, roll)
drawVector(up, 'black')

arrowcount = 20
for i in range(1, arrowcount):
    stepdegree = 360 / arrowcount
    yaw = i * stepdegree
    look = calculateRotatedVec(look, yaw, 0, 0)
    drawVector(look, 'red')
# for i in range(1, arrowcount):
#     stepdegree = 360 / arrowcount
#     pitch = i * stepdegree
#     look = calculateRotatedVec(cameraLook, yaw, pitch, roll)
#     drawVector(look, 'green')
# for i in range(1, arrowcount):
#     stepdegree = 360 / arrowcount
#     roll = i * stepdegree
#     up = calculateRotatedVec(cameraUp, yaw, pitch, roll)
#     drawVector(up, 'blue')

drawLegend()

plt.show()
