import numpy as np
A = np.array([[1,2,3,0],[1,3,1,3],[1,6,4,5],[2,3,1,0]])
print("Matrix:\n",A)
print("Excluding first row\n",A[1:,:])
print("Excluding last column\n",A[:,:-1])
print("1st and 2nd column in 2nd and 3rd row\n",A[1:3,:2])
print("2nd and 3rd element of 1st row\n",A[:1,1:3])

