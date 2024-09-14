import pickle as pkl
import numpy as np
from autolab_core import RigidTransform
from frankapy import FrankaArm, SensorDataMessageType
from frankapy import FrankaConstants as FC
from frankapy.proto_utils import sensor_proto2ros_msg, make_sensor_group_msg
from frankapy.proto import PosePositionSensorMessage, ShouldTerminateSensorMessage, CartesianImpedanceSensorMessage
from franka_interface_msgs.msg import SensorDataGroup
from frankapy.utils import min_jerk, min_jerk_weight
import rospy

def calculate_jacobian_RR(fa, L1=0.316, L2=0.384+0.088):
    """
    Calculate the Jacobian for a 2D RR arm.
    
    :param fa: FrankaArm instance
    :param L1: Length of the first link (default 0.3m)
    :param L2: Length of the second link (default 0.3m)
    :return: 2x2 Jacobian for planar motion
    """
    # Get current joint angles
    joints = fa.get_joints()
    theta1 = -joints[1]  # Negating to match the coordinate system
    theta2 = joints[3]


    # Calculate reduced 2x2 Jacobian for planar motion
    J_reduced = np.zeros((2, 2))
    J_reduced[0, 0] = ...
    J_reduced[0, 1] = ...
    J_reduced[1, 0] = ...
    J_reduced[1, 1] = ...

    return J_reduced

def main():
    fa = FrankaArm()
    
    # Move to initial position
    fa.reset_joints()
    initial_joints = [0.0, -0.1, 0.0, -2.1, -np.pi/2, np.pi/2, 0.0]
    print('Moving to initial position')
    fa.goto_joints(initial_joints)
    print('At initial position')

    rospy.loginfo('Generating Trajectory')
    pose_traj = pkl.load(open('franka_traj.pkl','rb'))
    T = 10
    dt = 0.01
    ts = np.arange(0, T, dt)

    rospy.loginfo('Initializing Sensor Publisher')
    pub = rospy.Publisher(FC.DEFAULT_SENSOR_PUBLISHER_TOPIC, SensorDataGroup, queue_size=10)
    rate = rospy.Rate(1 / dt)

    rospy.loginfo('Publishing pose trajectory...')
    # To ensure skill doesn't end before completing trajectory, make the buffer time much longer than needed
    fa.goto_pose(pose_traj[1], duration=T, dynamic=True, buffer_time=10,
        cartesian_impedances=[600.0, 600.0, 600.0, 50.0, 50.0, 50.0]
    )

    init_time = rospy.Time.now().to_time()
    jacobians_calc_reduced = []
    jacobians_api = []
    jacobian_differences = []

    for i in range(2, len(ts)):
        timestamp = rospy.Time.now().to_time() - init_time
        traj_gen_proto_msg = PosePositionSensorMessage(
            id=i, timestamp=timestamp,
            position=pose_traj[i].translation, quaternion=pose_traj[i].quaternion
        )
        ros_msg = make_sensor_group_msg(
            trajectory_generator_sensor_msg=sensor_proto2ros_msg(
                traj_gen_proto_msg, SensorDataMessageType.POSE_POSITION),
            )
        rospy.loginfo('Publishing: ID {}'.format(traj_gen_proto_msg.id))
        pub.publish(ros_msg)

        # Get current joint positions
        current_joints = fa.get_joints()
        
        # Calculate Jacobian using our function
        J_calc_reduced = calculate_jacobian_RR(fa)
        
        # Get Jacobian from API
        J_api_full = fa.get_jacobian(current_joints)
        J_api_reduced = J_api_full[:2, [1, 3]]  # Extract relevant part for comparison
        
        # Compare Jacobians
        difference = np.linalg.norm(J_calc_reduced - J_api_reduced)
        
        jacobians_calc_reduced.append(J_calc_reduced)
        jacobians_api.append(J_api_reduced)
        jacobian_differences.append(difference)

        rate.sleep()

    # Stop the skill
    term_proto_msg = ShouldTerminateSensorMessage(timestamp=rospy.Time.now().to_time() - init_time, should_terminate=True)
    ros_msg = make_sensor_group_msg(
        termination_handler_sensor_msg=sensor_proto2ros_msg(
            term_proto_msg, SensorDataMessageType.SHOULD_TERMINATE)
        )
    pub.publish(ros_msg)
    rospy.loginfo('Done')

    # Save the Jacobians and differences
    np.save('jacobian_differences.npy', np.array(jacobian_differences))
    
    rospy.loginfo('Jacobians and differences saved')
    rospy.loginfo(f'Average Jacobian difference: {np.mean(jacobian_differences)}')
    rospy.loginfo(f'Max Jacobian difference: {np.max(jacobian_differences)}')

if __name__ == "__main__":
    main()
