import numpy as np

class SO3():
    @staticmethod
    def eul2rotm(eul, type='zyx'):
        rads = np.reshape(eul, (3,))
        x, y, z = rads
        Rx = np.array([[1, 0, 0],
                       [0, np.cos(x), -np.sin(x)],
                       [0, np.sin(x), np.cos(x)]])
        Ry = np.array([[np.cos(y), 0, np.sin(y)],
                       [0, 1, 0],
                       [-np.sin(y), 0, np.cos(y)]])
        Rz = np.array([[np.cos(z), -np.sin(z), 0],
                       [np.sin(z), np.cos(z), 0],
                       [0, 0, 1]])
        if type == 'zyx':
            R = np.matmul(np.matmul(Rz, Ry), Rx)
        else:
            R = np.eye(3)
        return R

    @staticmethod
    def rotm2eul(R, type='zyx'):
        if type == 'zyx':
            sy = np.sqrt(R[0, 0] * R[0, 0] + R[1, 0] * R[1, 0])
            singular = sy < 1e-6
            if not singular:
                x = np.arctan2(R[2, 1], R[2, 2])
                y = np.arctan2(-R[2, 0], sy)
                z = np.arctan2(R[1, 0], R[0, 0])
            else:
                x = np.arctan2(-R[1, 2], R[1, 1])
                y = np.arctan2(-R[2, 0], sy)
                z = 0
            result = np.array([x, y, z])
        else:
            result = np.array([0, 0, 0])
        return result

    @staticmethod
    def get_exp(dthdt, type='zyx'):
        pass

    @staticmethod
    def get_log(R, type='zyx'):
        pass

