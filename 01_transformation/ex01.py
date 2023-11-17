import os.path as osp
import bk7084 as bk
from bk7084.math import *
import numpy as np


window = bk.Window()
window.set_title('BK7084 - Lab 1 - Transformation [ex00]')
window.set_size(1024, 1024)
window.set_resizable(True)

app = bk.App()

camera = app.create_camera(Vec3(-15.0, 8.0, 0.0), Vec3(0, 0, 0), 60.0)

"""
Exercise 1: Basic transformation
--------------------------------

First update your bk7084 package with pip. Type this in the terminal window:
$ conda activate compsim
$ pip install --upgrade bk7084

Make sure that you have also activated the compsim environment in Visual Studio Code (bottom left, Python 3...)

In this first exercise, you will create transformation matrices from scratch.
If you succeed, you can control a virtual car with your keyboard when you run this file:
[up, down, left, right] translate the car forward, backward, left, or right;
[X] rotate the car 45 degrees around the x-axis;
[Y] rotate the car 45 degrees around the y-axis;
[Z] rotate the car 45 degrees around the z-axis;
[S] scale the car to 90%;
[R] reset the car to its original position;
[esc] close the window (faster than clicking the close button).

Please read the accompanying PDF for an introduction and reference to complete this assignment.

Your tasks:
1. Build transformation matrices (do NOT use built-in functions):
  a. translation matrix,
  b. rotation matrices,
  c. scaling matrix.
2. Move the car to reach the red cube and blue cube.

Scroll down to complete the tasks.
Each task is denoted with "TODO: ...".
"""


def translate(x: float, y: float, z: float) -> Mat4:
    """
    Creates a translation matrix.

    Args:
        x (float): Translation along the x-axis.
        y (float): Translation along the y-axis
        z (float): Translation along the z-axis

    Returns:
        Mat4
    """
    # TODO: complete this matrix
    mat = Mat4(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]
    )
    return mat


def rotate_x(angle: float) -> Mat4:
    """
    Creates a rotation matrix around the x-axis.

    Args:
        angle (float): Rotation angle in degrees.

    Returns:
        Mat4
    """
    # TODO: complete this matrix
    # hint: you can compute cos and sin with np.cos(angle) and np.sin(angle)
    mat = Mat4(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]
    )
    return mat


def rotate_y(angle: float) -> Mat4:
    """
    Creates a rotation matrix around the y-axis.

    Args:
        angle (float): Rotation angle in degrees.

    Returns:
        Mat4
    """
    # TODO: complete this matrix
    # hint: you can compute cos and sin with np.cos(angle) and np.sin(angle)
    mat = Mat4(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]
    )
    return mat


def rotate_z(angle: float) -> Mat4:
    """
    Creates a rotation matrix around the z-axis.

    Args:
        angle (float): Rotation angle in degrees.

    Returns:
        Mat4
    """
    # TODO: complete this matrix
    # hint: you can compute cos and sin with np.cos(angle) and np.sin(angle)
    mat = Mat4(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]
    )
    return mat


def scale(x: float, y: float, z: float) -> Mat4:
    """
    Creates a scaling matrix.

    Args:
        x (float): Scaling factor along x-axis.
        y (float): Scaling factor along y-axis.
        z (float): Scaling factor along z-axis.

    Returns:
        Mat4
    """
    # TODO: complete this matrix
    mat = Mat4(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]
    )
    return mat


"""
You don't need to change the code below to finish the assignment.
"""
# Set working directory to the folder where this file is located.
cwd = osp.dirname(osp.abspath(__file__))
car = app.add_mesh(bk.Mesh.load_from(osp.join(cwd, 'assets/car.obj')))
car.set_visible(True)

# grid = Grid(origin=Vec3(0.0, -1.17, 0.0), axis_alignment=AxisAlignment.XZ, axis_marker=True)
arrow_x_mesh = bk.Mesh.load_from(osp.join(cwd, 'assets/arrow.obj'))
mtl_red = bk.Material()
mtl_red.kd = Vec3(1.0, 0.0, 0.0)
arrow_x_mesh.apply_material(mtl_red)

arrow_y_mesh = bk.Mesh.load_from(osp.join(cwd, 'assets/arrow.obj'))
mtl_green = bk.Material()
mtl_green.kd = Vec3(0.0, 1.0, 0.0)
arrow_y_mesh.apply_material(mtl_green)

arrow_z_mesh = bk.Mesh.load_from(osp.join(cwd, 'assets/arrow.obj'))
mtl_blue = bk.Material()
mtl_blue.kd = Vec3(0.0, 0.0, 1.0)
arrow_z_mesh.apply_material(mtl_blue)

arrows = [
    app.add_mesh(arrow_x_mesh),
    app.add_mesh(arrow_y_mesh),
    app.add_mesh(arrow_z_mesh)
]

# x-axis
arrows[0].set_transform(Mat4.from_translation(Vec3(7.0, 0.0, 0.0)) * Mat4.from_scale(Vec3(0.2)) * Mat4.from_rotation_z(-90.0, degrees=True))
arrows[0].set_visible(True)

# y-axis
arrows[1].set_transform(Mat4.from_translation(Vec3(0.0, 7.0, 0.0)) * Mat4.from_scale(Vec3(0.2)))
arrows[1].set_visible(True)

# z-axis
arrows[2].set_transform(Mat4.from_translation(Vec3(0.0, 0.0, 7.0)) * Mat4.from_scale(Vec3(0.2)) * Mat4.from_rotation_x(90.0, degrees=True))
arrows[2].set_visible(True)

car_transform = Mat4.identity()

@app.event
def on_update(input, dt, t):
    global car_transform

    if input.is_key_pressed(bk.KeyCode.Up):
        car_transform = car_transform * translate(0.5, 0.0, 0.0)

    if input.is_key_pressed(bk.KeyCode.Down):
        car_transform = car_transform * translate(-0.5, 0.0, 0.0)

    if input.is_key_pressed(bk.KeyCode.N):
        car_transform = car_transform * translate(0.0, 0.5, 0.0)

    if input.is_key_pressed(bk.KeyCode.M):
        car_transform = car_transform * translate(0.0, -0.5, 0.0)

    if input.is_key_pressed(bk.KeyCode.Left):
        car_transform = car_transform * translate(0.0, 0.0, -0.5)

    if input.is_key_pressed(bk.KeyCode.Right):
        car_transform = car_transform * translate(0.0, 0.0, 0.5)

    if input.is_key_pressed(bk.KeyCode.X):
        car_transform = car_transform * rotate_x(45)

    if input.is_key_pressed(bk.KeyCode.Y):
        car_transform = car_transform * rotate_y(45)

    if input.is_key_pressed(bk.KeyCode.Z):
        car_transform = car_transform * rotate_z(45)

    if input.is_key_pressed(bk.KeyCode.S):
        car.set_transform(scale(0.9, 0.9, 0.9))

    if input.is_key_pressed(bk.KeyCode.R):
        car_transform = Mat4.identity()

    car.set_transform(car_transform)


app.run(window)
