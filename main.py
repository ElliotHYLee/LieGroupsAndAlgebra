from LieGA import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def KITTI():
    imgPath = 'D:/DLData/KITTI/odom/dataset/sequences/00/'
    dataPath = 'D:/DLData/KITTI/odom/dataset/poses/'
    stateData = pd.read_csv(dataPath + '00.txt', sep=' ', header=None).values
    raw = np.reshape(stateData, (stateData.shape[0], 3, 4))
    N = raw.shape[0]
    T = np.reshape(np.eye(4), (1, 4, 4))
    data = np.repeat(T, N, axis=0)
    data[:, :3, :] = raw
    return data

def main():
    data = KITTI()
    dT = np.zeros((data.shape[0]-1, 4, 4))
    dT_recon = np.zeros_like(dT)
    for i in range(1, data.shape[0]):
        T_prev = data[i - 1]
        T_curr = data[i]
        dT[i-1] = np.matmul(np.linalg.inv(T_prev), T_curr)
        w, u = SE3.get_log(dT[i - 1])
        dT_recon[i-1] = SE3.get_exp(w, u)

    pose = np.zeros((data.shape[0], 3))
    reconT = np.zeros_like(data)
    reconT[0] = np.eye(4)
    for i in range(1, data.shape[0]):
        reconT[i] = np.matmul(reconT[i-1], dT_recon[i-1])
        pose[i] = reconT[i, :3, 3]

    plt.figure()
    plt.plot(pose[:, 0], pose[:, 2], 'r')

    # plt.figure()
    # plt.plot(w[:, 0], 'b')
    # plt.plot(w[:, 1], 'g')
    # plt.plot(w[:, 2], 'r')

    plt.show()


if __name__ =='__main__':
    main()
    # T = np.reshape(np.eye(4), (1, 4, 4))
    # dd = np.repeat(T, 10, axis=0)
    # print(dd.shape)
    # print(dd[0])