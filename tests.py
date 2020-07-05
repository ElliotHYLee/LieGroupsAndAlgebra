import unittest
import numpy as np
from LieGA import *

EPSILON = np.eye(3)*10**-5

class LieGATest(unittest.TestCase):
    def test_eul2rotm(self):
        eul = np.array([-30, 15, -15])*np.pi/180.0
        R = SO3.eul2rotm(eul)
        ans = np.array([[ 0.9330127, 0.09914387, 0.34591587,],
                         [-0.25, 0.87000995, 0.42495021],
                         [-0.25881905, -0.48296291, 0.8365163 ]])
        diff = np.abs(R-ans)
        self.assertLess(diff.tolist(), EPSILON.tolist())

        eul = np.array([180, 90, -90]) * np.pi / 180.0
        R = SO3.eul2rotm(eul)
        ans = np.array([[0, -1, 0],
                        [0, 0, 1],
                        [-1, 0, 0]])
        diff = np.abs(R - ans)
        self.assertLess(diff.tolist(), EPSILON.tolist())

    def test_rotm2eul(self):
        R = np.array([[0.9330127, 0.09914387, 0.34591587, ],
                        [-0.25, 0.87000995, 0.42495021],
                        [-0.25881905, -0.48296291, 0.8365163]])
        eul = SO3.rotm2eul(R)

        ans = np.array([-30, 15, -15]) * np.pi / 180.0
        diff = np.abs(eul - ans)
        self.assertLess(diff.tolist(), (np.ones(3)*10**-5).tolist())

        R = np.array([[0, -1, 0],
                        [-1, 0, 0],
                        [0, 0, -1]])
        eul = SO3.rotm2eul(R)
        ans = np.array([180, 0, -90]) * np.pi / 180.0
        diff = np.abs(eul - ans)
        self.assertLess(diff.tolist(), (np.ones(3) * 10 ** -5).tolist())

    def test_get_exp(self):
        w = np.array([10, -20 , 30])*np.pi/180.0
        dR = SO3.get_exp(w)
#        print(dR)