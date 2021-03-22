import numpy as np 
# Resolucion por cholesky para solucion por minimosn cuadrados, solucion aproximada
#para cuando A es invertible
#cholesky
def cholesky_pro(A,b):
    #primero.- transpuesta de A
    A_t = np.transpose(A)
    paso_2_1 = np.dot(A_t,A)
    #print(paso_2_1)
    paso_2_2 = np.dot(A_t,b)
    #print(paso_2_2)
    chol = np.linalg.cholesky(paso_2_1)
    #tringular superior, L
    #print(chol)
    #triangular inferior L_t
    chol_t = np.transpose(chol)
    #print(chol_t)
    #print("CHOLESKY")
    #print(chol, chol_t)
    #print("Comprobamos cholesky")
    #print(paso_2_1,np.dot(chol, chol_t))
    #l*y1,y2 = At_b
    y = np.linalg.solve(chol, paso_2_2)
    #valores de y
    #print(y)

    x = np.linalg.solve(chol_t,y)
    #valores de x
    #print(x)
    return paso_2_1,paso_2_2, chol, chol_t, y,  x
'''
A = [[1,-6],[1,-2],[1,1],[1,7]]
b = [[-1],[2],[1],[6]]

#primero.- transpuesta de A
A_t = np.transpose(A)
paso_2_1 = np.dot(A_t,A)
print(paso_2_1)
paso_2_2 = np.dot(A_t,b)
print(paso_2_2)
chol = np.linalg.cholesky(paso_2_1)
#tringular superior, L
print(chol)
#triangular inferior L_t
chol_t = np.transpose(chol)
print(chol_t)
print("CHOLESKY")
print(chol, chol_t)
print("Comprobamos cholesky")
print(paso_2_1,np.dot(chol, chol_t))
#l*y1,y2 = At_b
y = np.linalg.solve(chol, paso_2_2)
#valores de y
print(y)

x = np.linalg.solve(chol_t,y)
#valores de x
print(x)
'''

