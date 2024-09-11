import sys
sys.path.append("../../ex1/solution")
import numpy as np
from robot_info import robot_info
from jacobian_link_ends_RR import jacobian_link_ends_RR
from jacobian_coms_RR import jacobian_coms_RR

def get_grav_comp_torques(theta, gravity):
    """
    Calculates the joint torques required to cancel out effects due to
    gravity.

    Args:
    theta (np.array): Joint angles
    gravity (np.array): Gravity vector (2x1)

    Returns:
    np.array: Joint torques for gravity compensation
    """
    # Get information about the robot:
    robot = robot_info()
    # Extract mass of the links, joint, and end effector [kg]
    m_link_1 = robot['link_masses'][0]
    m_link_2 = robot['link_masses'][1]
    m_joint_1 = robot['joint_masses'][0]
    m_joint_2 = robot['joint_masses'][1]
    m_end_effector = robot['end_effector_mass']

    # TODO: Implement gravity compensation
    # Use the Jacobian to calculate the joint torques to compensate for the
    # weights of the joints, links, and end effector (assuming the acceleration
    # due to gravity is given by 'gravity', and it is a 2x1 (column) vector).
    # Hint: You may find the jacobian_link_ends_RR and jacobian_coms_RR functions useful.

    # Your code here
    torque1 = 0  # Replace with your calculation
    torque2 = 0  # Replace with your calculation

    # Pack into a more readable format.
    return np.array([torque1, torque2])