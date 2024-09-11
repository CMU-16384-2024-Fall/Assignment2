import numpy as np
from robot_info import robot_info

def jacobian_coms_RR(theta):
    """
    jacobian_coms_RR

    Returns a vector of Jacobian matrices, corresponding
    to points at the center of mass of each link, given the
    joint angle positions [rad]. The Jacobians computed here
    are relative to R^2 only (i.e., no theta term).

    The function returns N 2xN matrices, where N is the
    number of links (and also the number of joints).

    Each matrix describes the differential relationship between
    a vector of joint angle velocities and the (x,y) motion of the
    corresponding point.

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
    # Define the Jacobians for the frames below.  Feel free to define helper
    # variables.
    J_1 = np.zeros((2, 2))
    J_2 = np.zeros((2, 2))
    # --------------- END STUDENT SECTION ------------------------------------

    # Pack into a more readable format. DO NOT CHANGE!
    jacobians = np.stack((J_1, J_2), axis=2)
    return jacobians