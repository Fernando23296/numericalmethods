from flask import Flask, render_template, request
from jacobi import jacobi
from cholesky import cholesky_pro
from scipy.linalg import solve
import scipy.linalg
import numpy as np
app = Flask(__name__)


#A = np.array([[4.0, -2.0, 1.0], [1.0, -3.0, 2.0], [-1.0, 2.0, 6.0]])
b = [[-1],[2],[1],[6]]



@app.route('/', methods=['GET','POST'])
def index():
    global columna
    global fila
    if request.method=='POST':
        columna = int(request.form['columna'])
        fila = int(request.form['fila'])
        identidad = np.eye(columna,fila)
        return render_template('matrix.html', columna=columna, fila=fila, identidad = identidad)
    return render_template('index.html')

@app.route('/matrix', methods=['GET','POST'])
def matrix():
    if request.method=='POST':
        valores = []

        for c in range (0,fila):
            for f in range (0,columna):
                name = 'fila'+str(c)+'columna'+str(f)
                val = int(request.form[name])
                valores.append(val)
        
        matrix = np.reshape(valores, (fila, columna))
        '''
        matrix_array = np.array(matrix)
        b = [1.0, 2.0, 3.0]
        x = [1.0, 1.0, 1.0]
        n = 25
        x = jacobi(matrix_array, b, x, n)
        solucion = solve(matrix_array, b)
        '''
        L2 = cholesky_pro(matrix,b)
        '''
        f0c0 = int(request.form['fila0columna0'])
        f0c1 = int(request.form['fila0columna1'])
        f1c0 = int(request.form['fila1columna0'])
        f1c1 = int(request.form['fila1columna1'])
        '''

    return render_template('suma.html', suma = L2  )
if __name__ == "__main__":

    app.run(debug=True)