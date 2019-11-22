from SO3 import SO3
import numpy as np

def main():
    eul = np.array([-120, -100, -95]) * np.pi/180
    print(eul)

    R = SO3.eul2rotm(eul)
    print(R)
    eul = SO3.rotm2eul(R)
    print(eul)

if __name__ =='__main__':
    main()