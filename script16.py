import numpy as np
C = np.arange(24).reshape(4,-1,3)
print (C.shape, np.transpose(C).shape)
print()
print(C[0])
print ()
print(C.T[:,:,0])