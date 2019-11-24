import numpy as np
import warnings

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
    def get_exp(w, type='zyx'):
        w = np.reshape(w, (3))
        th = np.sqrt(np.dot(w, w))
        wx = SO3.get_skew(w)
        dR = np.eye(3) if th == 0 else np.eye(3) + np.sin(th) / th * wx + (1 - np.cos(th)) / th ** 2 * np.matmul(wx, wx)
        return dR

    @staticmethod
    def get_log(R, type='zyx'):
        with warnings.catch_warnings():
            warnings.filterwarnings('error')
            try:
                th = np.arccos((np.trace(R) - 1)/2)
            except:
                R = np.round(R, 6)
                th = np.arccos((np.trace(R) - 1)/2)
        skew = np.zeros((3,3)) if th == 0 else th/(2*np.sin(th))*(R - R.T)
        return skew

    @ staticmethod
    def get_skew(w):
        w = np.reshape(w, (3))
        x, y, z = w
        wx = np.array([[0, -z, y],
                       [z, 0, -x ],
                       [-y, x, 0]])
        return wx

    @ staticmethod
    def get_w(wx):
        w = np.array([-wx[1,2], wx[0,2], -wx[0,1]])
        return w

class SE3():
    @ staticmethod
    def get_V(w):
        th = np.sqrt(np.dot(w, w))
        skew = SO3.get_skew(w)
        V = np.eye(3) if th == 0 else np.eye(3) + (1-np.cos(th))/th**2*skew +(th-np.sin(th))/th**3*np.matmul(skew, skew)
        return V

    @staticmethod
    def get_Rt(T):
        return T[:3, :3], T[:3, 3]

    @staticmethod
    def get_exp(w, u):
        R = SO3.get_exp(w)
        V = SE3.get_V(w)
        t = np.matmul(V, u)
        T = np.eye(4)
        T[:3, :3] = R
        T[:3, 3] = t
        return T

    @staticmethod
    def get_log(T):
        R, t = SE3.get_Rt(T)
        skew = SO3.get_log(R)
        w = SO3.get_w(skew)
        V = SE3.get_V(w)
        u = np.matmul(np.linalg.inv(V), t)
        return w, u

if __name__ == '__main__':
    eul = np.array([10, 20, 30])*np.pi/180
    # R = Lie_SO3.eul2rotm(eul)
    # skew = Lie_SO3.get_log(R)
    # w = Lie.get_w(skew)
    # wx = Lie.get_skew(w)
    # R = Lie_SO3.get_exp(w)
    # print(Lie_SO3.rotm2eul(R)*180/np.pi)
    T = np.eye(4)
    T[:3, :3] = SO3.eul2rotm(eul)
    T[:3, 3] = np.array([1, 2, 3])
    print(T)
    w, u = SE3.get_log(T)
    T_recon = SE3.get_exp(w, u)
    print(np.round(T - T_recon, 2))

