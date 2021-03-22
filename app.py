from flask import Flask, render_template, request
from jacobi import jacobi
from cholesky import cholesky_pro
from scipy.linalg import solve
import scipy.linalg
import numpy as np
app = Flask(__name__)


#A = np.array([[4.0, -2.0, 1.0], [1.0, -3.0, 2.0], [-1.0, 2.0, 6.0]])
#b = [[-1],[2],[1],[6]]



@app.route('/', methods=['GET','POST'])
def index():
    global columna
    global fila
    global filab
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
        valoresb = []
        for c in range (0,fila):
            for f in range (0,columna):
                name = 'fila'+str(c)+'columna'+str(f)
                val = int(request.form[name])
                valores.append(val)
        
        for cb in range(0, fila):
            name = 'filab'+str(cb)
            valb = int(request.form[name])
            valoresb.append(valb)

        matrix = np.reshape(valores, (fila, columna))
        #bb = np.reshape(valores, (fila,1))
        '''
        matrix_array = np.array(matrix)
        b = [1.0, 2.0, 3.0]
        x = [1.0, 1.0, 1.0]
        n = 25
        x = jacobi(matrix_array, b, x, n)
        solucion = solve(matrix_array, b)
        '''
        #
        valoresb = np.array(valoresb)
        b =valoresb.reshape(-1,1)

        resultado = cholesky_pro(matrix,b)
        '''
        f0c0 = int(request.form['fila0columna0'])
        f0c1 = int(request.form['fila0columna1'])
        f1c0 = int(request.form['fila1columna0'])
        f1c1 = int(request.form['fila1columna1'])
        '''

    return render_template('resultado.html', resultado = resultado  )
if __name__ == "__main__":

    app.run(debug=True)