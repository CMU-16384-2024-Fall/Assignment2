import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
import pickle
from robot_info import robot_info
from forward_kinematics_RR import forward_kinematics_RR
from jacobian_link_ends_RR import jacobian_link_ends_RR
from jacobian_coms_RR import jacobian_coms_RR

def sample_path():
    # Load a subset of the sample data so that the plot is less cluttered.
    log = loadmat('sample_ground_truth.mat')
    theta = log['theta'][2400:3200, :]
    theta_dot = log['theta_dot'][2400:3200, :]

    n = len(theta)
    x = np.zeros((n, 4))
    y = np.zeros((n, 4))
    x_dot = np.zeros((n, 4))
    y_dot = np.zeros((n, 4))

    robot = robot_info()
    l1, l2 = robot['link_lengths']

    # --------------- BEGIN STUDENT SECTION ----------------------------------
    # Fill in x/y positions and velocities for each point, using the forward
    # kinematics and Jacobian functions you have written.

    for i in range(n):
        th = theta[i, :]
        th_dot = theta_dot[i, :]

        # Fill in center of mass of link 1 position/velocity:
        x[i, 0] = 0
        y[i, 0] = 0
        x_dot[i, 0] = 0
        y_dot[i, 0] = 0

        # Fill in distal end of link 1 position/velocity:
        x[i, 1] = 0
        y[i, 1] = 0
        x_dot[i, 1] = 0
        y_dot[i, 1] = 0

        # Fill in center of mass of link 2 position/velocity:
        x[i, 2] = 0
        y[i, 2] = 0
        x_dot[i, 2] = 0
        y_dot[i, 2] = 0

        # Fill in distal end of link 2 position/velocity:
        x[i, 3] = 0
        y[i, 3] = 0
        x_dot[i, 3] = 0
        y_dot[i, 3] = 0

    # --------------- END STUDENT SECTION ------------------------------------

    # Save the results to a pickle file
    results = {
        'COM_Link_1': {
            'x': x[:, 0],
            'y': y[:, 0],
            'x_dot': x_dot[:, 0],
            'y_dot': y_dot[:, 0]
        },
        'End_Link_1': {
            'x': x[:, 1],
            'y': y[:, 1],
            'x_dot': x_dot[:, 1],
            'y_dot': y_dot[:, 1]
        },
        'COM_Link_2': {
            'x': x[:, 2],
            'y': y[:, 2],
            'x_dot': x_dot[:, 2],
            'y_dot': y_dot[:, 2]
        },
        'End_Link_2': {
            'x': x[:, 3],
            'y': y[:, 3],
            'x_dot': x_dot[:, 3],
            'y_dot': y_dot[:, 3]
        }
    }
    with open('results.pkl', 'wb') as f:
        pickle.dump(results, f)

    subsample_resolution = 25
    x_sub = x[::subsample_resolution, :]
    y_sub = y[::subsample_resolution, :]
    x_dot_sub = x_dot[::subsample_resolution, :]
    y_dot_sub = y_dot[::subsample_resolution, :]

    plt.figure(figsize=(10, 10))
    colors = ['#FFB3B3', '#FF0000', '#808080', '#000000']
    labels = ['COM Link 1', 'End Link 1', 'COM Link 2', 'End Link 2']
    
    for i in range(4):
        plt.plot(x[:, i], y[:, i], color=colors[i], label=labels[i], alpha=0.5)
        
        scale = 0.1
        plt.quiver(x_sub[:, i], y_sub[:, i],
                   x_dot_sub[:, i], y_dot_sub[:, i],
                   scale=scale, color=colors[i], width=0.003)

    plt.title('Plot of link positions and velocities over a sample run.')
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.axis('equal')
    plt.legend()
    
    margin = 0.1
    plt.xlim([np.min(x) - margin, np.max(x) + margin])
    plt.ylim([np.min(y) - margin, np.max(y) + margin])
    
    plt.grid(True)
    plt.savefig('path.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    sample_path()