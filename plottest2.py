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

def rotateX(vec3, angle):
    return np.array([vec3[0], vec3[1] * math.cos(math.radians(angle)) - vec3[2] * math.sin(math.radians(angle)),
        vec3[1] * math.sin(math.radians(angle)) + vec3[2] * math.cos(math.radians(angle))])

def rotateY(vec3, angle):
    return np.array([vec3[0] * math.cos(math.radians(angle)) + vec3[2] * math.sin(math.radians(angle)),
        vec3[1], -1 * vec3[0] * math.sin(math.radians(angle)) + vec3[2] * math.cos(math.radians(angle))])

def rotateZ(vec3, angle):
    return np.array([vec3[0] * math.cos(math.radians(angle)) - vec3[1] * math.sin(math.radians(angle)),
        vec3[0] * math.sin(math.radians(angle)) + vec3[1] * math.cos(math.radians(angle)), vec3[2]])

def yaw(vec3, angle):
    return rotateZ(vec3, angle)
def pitch(vec3, angle):
    return rotateY(vec3, angle) 
def roll(vec3, angle):
    return rotateX(vec3, angle)

def rotate(vec3, yaw, pitch, roll):
    return rotateZ(rotateY(rotateX(vec3, roll), pitch), yaw)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

absoluteFront = np.array([-1., 0., 0.]) 
absoluteUp = np.array([0., 0., 1.])
absoluteRight = np.array([0., 1., 0.])

cameraPos = np.array([0., 0., 1.])
cameraFront = np.array([-1., 0., 0.]) 
cameraUp = np.array([0., 0., 1.])
cameraRight = np.array([0., 1., 0.])

# drawVector(cameraFront, 'red')
# drawVector(cameraUp, 'green')
# drawVector(cameraRight, 'blue')

# yaw = 0
# pitch = 20
# roll = 40

# cameraFront = roll(cameraFront, 20)
# cameraUp = roll(cameraUp, 20)
# cameraRight = roll(cameraRight, 20)

cameraFront = rotate(cameraFront, 45, 0, 25)
cameraUp = rotate(cameraUp, 45, 0, 25)
cameraRight = rotate(cameraRight, 45, 0, 25)

drawVector(cameraFront, 'red')
drawVector(cameraUp, 'green')
drawVector(cameraRight, 'blue')

# cameraFront = pitch(cameraFront, 45)
# cameraUp = pitch(cameraUp, 45)
# cameraRight = pitch(cameraRight, 45)

# drawVector(cameraFront, 'red')
# drawVector(cameraUp, 'green')
# drawVector(cameraRight, 'blue')

# cameraFront = yaw(cameraFront, 90)
# cameraUp = yaw(cameraUp, 90)
# cameraRight = yaw(cameraRight, 90)

# drawVector(cameraFront, 'cyan')
# drawVector(cameraUp, 'magenta')
# drawVector(cameraRight, 'yellow')




# drawVector(cameraFront, 'red')
# drawVector(cameraUp, 'green')
# drawVector(cameraLeft, 'blue')
# rotated = rotateZ(cameraFront, 90)
# drawVector(rotated, 'red')
# rotated = rotateY(cameraFront, 90)
# drawVector(rotated, 'green')
# rotated = rotateX(cameraFront, 90)
# drawVector(rotated, 'blue')
# rotated = rotateX(cameraFront, 90)
# drawVector(rotated, 'blue')

arrowcount = 100

# for i in range(arrowcount):
#     stepdegree = 360 / arrowcount
#     cameraFront = yaw(cameraFront, stepdegree)
#     drawVector(cameraFront, 'red')

# for i in range(arrowcount):
#     stepdegree = 360 / arrowcount
#     cameraFront = pitch(cameraFront, stepdegree)
#     cameraUp = pitch(cameraUp, stepdegree)
#     cameraRight = pitch(cameraRight, stepdegree)
#     drawVector(cameraFront, 'magenta')

# for i in range(arrowcount):
#     stepdegree = 360 / arrowcount
#     cameraUp = roll(cameraUp, stepdegree)
#     drawVector(cameraUp, 'green')

drawLegend()

plt.show()
