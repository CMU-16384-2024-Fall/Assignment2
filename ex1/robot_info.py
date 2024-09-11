import numpy as np

def robot_info():
    robot_info = {}
    # length of the links
    robot_info['link_lengths'] = np.array([0.3280, 0.3160])  # It is your responsibility to measure the links
    # masses [kg]
    # (density of link tube is .1213 kg/m, with additional .165 kg of hardware at ends)
    robot_info['link_masses'] = robot_info['link_lengths'] * 0.1213 + np.array([.165, .165])
    robot_info['joint_masses'] = np.array([0.347, 0.3])
    robot_info['end_effector_mass'] = 0  # Nothing for the end effector for this lab!

    return robot_info

# This is the equivalent of robot_info_for_real_robot.m
def robot_info_for_real_robot():
    robot_info = {}
    # length of the links
    robot_info['link_lengths'] = np.array([0.375, 0.31])  # [0.42, 0.245]  # It is your responsibility to measure the links
    # masses [kg]
    # (density of link tube is .1213 kg/m, with additional .165 kg of hardware at ends)
    robot_info['link_masses'] = robot_info['link_lengths'] * 0.35  # + np.array([.14, .07])
    robot_info['joint_masses'] = np.array([0.342, 0.482])  # [0.342, 0.342]
    robot_info['end_effector_mass'] = 0  # Nothing for the end effector for this lab!

    return robot_info