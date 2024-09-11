import numpy as np
from robot_info import robot_info

def forward_kinematics_RR(theta):
    """
    forward_kinematics_RR

    Returns the forward kinematics for an RR robot given
    the joint angle positions [rad].

    The function returns N 3x3 frames, where N is the
    number of links.

    Each homogeneous transform describes the relationship from
    the base frame to start of the corresponding link.

    Hints
    - 'theta' is a vector. Individual angles can be selected
       using indices, e.g., theta1 = theta[0]
    """

    # Get information about the robot:
    robot = robot_info()
    # Extract length of the links
    l1, l2 = robot['link_lengths']

    # Ensure theta is a 1D array
    theta = np.squeeze(theta)

    # --------------- BEGIN STUDENT SECTION ----------------------------------
    # Define the transforms for all the frames below (replace each 'np.eye(3)'
    # with the corresponding matrix).  You can define helper variables, and
    # feel free to express your answers as products of matrices.

    H_1_0 = np.eye(3)
    H_2_0 = np.eye(3)

    # --------------- END STUDENT SECTION ------------------------------------

    # Pack into a more readable format. DO NOT CHANGE!
    frames = np.stack((H_1_0, H_2_0), axis=2)
    return frames