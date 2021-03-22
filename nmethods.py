import pprint
import scipy
import scipy.linalg   # SciPy Linear Algebra Library
import numpy as np


def cholesky(A):
    L = np.zeros_like(A)
    n = len(L)
    for i in range(n):
        for j in range(i+1):
            if i==j:
                val = A[i,i] - np.sum(np.square(L[i,:i]))
                # if diagonal values are negative return zero - not throw exception
                if val<0:
                    return 0.0
                L[i,i] = np.sqrt(val)
            else:
                L[i,j] = (A[i,j] - np.sum(L[i,:j]*L[j,:j]))/L[j,j]
                
    return L