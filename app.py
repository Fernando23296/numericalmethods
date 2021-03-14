from flask import Flask, render_template, request
import numpy as np
app = Flask(__name__)

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

        f0c0 = int(request.form['fila0columna0'])
        f0c1 = int(request.form['fila0columna1'])
        f1c0 = int(request.form['fila1columna0'])
        f1c1 = int(request.form['fila1columna1'])
        suma = f0c0+f0c1+f1c0+f1c1
    return render_template('suma.html', suma = suma, columna2=columna2, fila2=fila2  )
if __name__ == "__main__":

    app.run(debug=True)