import numpy as np
from numpy.linalg import norm, inv
from numpy import transpose
from readonly.bearNecessities import *

def build_reflection_matrix(bearBasis):  
    
    B = np.array(bearBasis, dtype=np.float64)  
    verySmallNumber = 1e-14  
    
    for i in range(B.shape[1]):
        for j in range(i):
            B[:, i] -= (B[:, i] @ B[:, j]) * B[:, j]
        
        if norm(B[:, i]) > verySmallNumber:
            B[:, i] /= norm(B[:, i])
        else:
            B[:, i] = np.zeros_like(B[:, i])
    
    E = B
    
    TE = np.array([[1, 0],
                   [0, -1]]) 
    
    T = E @ TE @ inv(E)
    
    return T

bearBasis = np.array([[1, -1], [1.5, 2]])
T = build_reflection_matrix(bearBasis)
print("Transformation Matrix T:\n", T)