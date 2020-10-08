import numpy as np
from collections import namedtuple
from dataclasses import dataclass

@dataclass
class Point:
    "Class for storing points"
    x: float
    y: float
def generate_trajectory(robot_model, actuation_sequence):
    kinematic_trajectory = []
    for action in actuation_sequence:
        kinematic_trajectory.append(robot_model.kinematic_move(action))
    return kinematic_trajectory



class Rigid5Bar():
    def __init__(self, length1=40, length2=66, servo_distance=70):

        self.l1 = length1
        self.l2 = length2
        self.l3 = length2
        self.l4 = length1
        self.servo_distance = servo_distance
        self.p1 = Point(0, 0)
        self.p2 = Point(0, 0)
        self.p3 = Point(0, 0)
        self.p4 = Point(0, 0)
        self.p5 = Point(-self.servo_distance, 0)

    def kinematic_move(self, action):

        theta1 = action[0]
        theta5 = action[1]
        a1 = self.l1
        a2 = self.l2
        a3 = self.l3
        a4 = self.l4
        a5 = self.servo_distance

        self.p2.x = a1*np.cos(theta1)
        self.p2.y = a1*np.sin(theta1)
        self.p4.x = a4*np.cos(theta5)-a5
        self.p4.y = a4*np.sin(theta5)

        p4 = np.array([self.p4.x, self.p4.y])
        p2 = np.array([self.p2.x, self.p2.y])

        dist_p2_ph = (a2**2 - a3**2 + np.linalg.norm(p4-p2)**2)\
               /(2*np.linalg.norm(p4-p2))

        ph = p2 + (dist_p2_ph/np.linalg.norm(p2-p4))*(p4-p2)
        dist_p3_ph = np.sqrt(a2**2-dist_p2_ph**2)
        xh = ph[0]
        yh = ph[1]

        self.p3.x = xh + dist_p3_ph/np.linalg.norm(p2-p4) * (self.p4.y -
                                   self.p2.y)

        self.p3.y = yh - dist_p3_ph/np.linalg.norm(p2-p4) *\
        (self.p4.x-self.p2.x)

    def __str__(self):

        string =\
        f"{self.p1.__str__()}\n{self.p2.__str__()}\n{self.p3.__str__()}\n{self.p4.__str__()}\n{self.p5.__str__()}"
        return string


robot = Rigid5Bar()
robot.kinematic_move([np.pi/4, 3*np.pi/4])
print(robot)













