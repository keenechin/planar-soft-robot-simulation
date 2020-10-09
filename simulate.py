import numpy as np
from dataclasses import dataclass
import matplotlib.pyplot as plt
import json

@dataclass
class Point:
    "Class for storing points"
    x: float
    y: float


@dataclass
class RigidParams:
    "Parameter set for rigid 5-bar"
    l1: float
    l2: float
    l3: float
    l4: float
    servo_dist: float

@dataclass
class RigidState:
    p1: Point
    p2: Point
    p3: Point
    p4: Point
    p5: Point

def generate_trajectory(robot_model, actuation_sequence):
    kinematic_trajectory = []
    for action in actuation_sequence:
        kinematic_trajectory.append(robot_model.kinematic_move(action))
    return kinematic_trajectory


class Rigid5Bar():
    def __init__(self,  params = RigidParams(40, 66, 66, 40, 70)):

        self.l1 = params.l1
        self.l2 = params.l2
        self.l3 = params.l3
        self.l4 = params.l4
        self.servo_distance = params.servo_dist
        self.state = RigidState(Point(0,0), Point(0,0), Point(0,0), Point(0,0),
                                Point(-self.servo_distance,0))

    def kinematic_move(self, action):

        theta1 = action[0]
        theta5 = action[1]
        a1 = self.l1
        a2 = self.l2
        a3 = self.l3
        a4 = self.l4
        a5 = self.servo_distance

        self.state.p2.x = a1*np.cos(theta1)
        self.state.p2.y = a1*np.sin(theta1)
        self.state.p4.x = a4*np.cos(theta5)-a5
        self.state.p4.y = a4*np.sin(theta5)

        p4 = np.array([self.state.p4.x, self.state.p4.y])
        p2 = np.array([self.state.p2.x, self.state.p2.y])

        dist_p2_ph = (a2**2 - a3**2 + np.linalg.norm(p4-p2)**2)\
               /(2*np.linalg.norm(p4-p2))

        ph = p2 + (dist_p2_ph/np.linalg.norm(p2-p4))*(p4-p2)
        operand = a2**2-dist_p2_ph**2
        if operand < 0:
            raise ArithmeticError
        dist_p3_ph = np.sqrt(operand)
        xh = ph[0]
        yh = ph[1]

        self.state.p3.x = xh + dist_p3_ph/np.linalg.norm(p2-p4) * (self.state.p4.y -
                                   self.state.p2.y)

        self.state.p3.y = yh - dist_p3_ph/np.linalg.norm(p2-p4) *\
        (self.state.p4.x-self.state.p2.x)

    def __str__(self):
        string = self.state.__str__()
        return string



if __name__ == "__main__":
    robot = Rigid5Bar(params = RigidParams(30,30,30,30,70))
    resolution = 180
    actuationSet  =  np.linspace(0, 2*np.pi, num=resolution)
    o = "\u03B8"
    validity = np.zeros((resolution,resolution))

    for i,theta1 in enumerate(actuationSet):
        for j,theta2 in enumerate(actuationSet):
            try:
                robot.kinematic_move([theta1, theta2])
                #print(robot)
                validity[i][j] = 1
            except ArithmeticError:
                pass
                #print(f"Invalid config: ({o}1: {theta1}, {o}2: {theta2})")

    plt.imshow(validity, cmap='hot')
    plt.xlabel(f"{o}1")
    plt.ylabel(f"{o}2")
    plt.title("Is a valid angle pair?")
    plt.show()
