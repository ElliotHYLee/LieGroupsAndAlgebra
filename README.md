# LieGroupsAndAlgebra

This repo provides exponential and log maps for special orthogonal groups (SO3) and special Euclidian groups (SE3).

## Special Orthogonal Group (SO3)

Rotation matrix is SO3.
<br> 
<img src="https://github.com/ElliotHYLee/LieGroupsAndAlgebra/blob/master/Images/RotationMatrix.png" width="400">

Quick and intuitively, the rotation matrix is nonlinear. As R is in nonlinear space, instantaneous rotation is not dR. Rather, the instantaneous rotation is more like the information from the gyroscope in x, y, and z axes. 
<br><br>For more, refer to Chapter2. 
### Exponential Mapping 
The 3D vector needs to be mapped as a matrix. The mapping from 3D vector to the rotation matrix is exponential mapping.

skew symmetric matrix = <br> 
<img src="https://github.com/ElliotHYLee/LieGroupsAndAlgebra/blob/master/Images/skew.PNG" width="200">

### Logarithmic Mapping
The inverse mapping of exponential mapping. The log maps the rotation matrix to 3D vector.