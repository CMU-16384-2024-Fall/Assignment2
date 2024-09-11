import sys
sys.path.append("../../ex1/solution")
import numpy as np
from jacobian_link_ends_RR import jacobian_link_ends_RR

def get_joint_torques(theta, desired_force):
    """
    Calculates the joint torques required to result in a desired force
    vector (in world coordinates).

    Args:
    theta (np.array): Joint angles
    desired_force (np.array): Desired force vector (2x1)

    Returns:
    np.array: Joint torques
    """
    # TODO: Implement joint torque calculation
    # Use the Jacobian to find the joint torques necessary for the end
    # effector to exert the given force (given the joint configuration theta).
    # Assume 'desired_force' is a 2x1 (column) vector.
    # Hint: You may find the jacobian_link_ends_RR function useful.

    # Your code here
    torque1 = 0  # Replace with your calculation
    torque2 = 0  # Replace with your calculation

    # Pack into a more readable format.
    return np.array([torque1, torque2])