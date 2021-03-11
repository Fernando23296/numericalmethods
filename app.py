from flask import Flask, render_template, request
import numpy as np
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        columna = int(request.form['columna'])
        fila = int(request.form['fila'])
        identidad = np.eye(columna,fila)
        return render_template('velocidad.html', columna=columna, fila=fila, identidad = identidad)
    return render_template('index.html')


if __name__ == "__main__":

    app.run(debug=True)