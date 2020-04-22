from flask import Flask, render_template
app = Flask(__name__)	

# Página principal
@app.route('/')
def inicio():
    return render_template("index.html")

# Página potencia:
@app.route('/potencia/<int:base>/<exp>',methods=["GET","POST"])
def potencia(base,exp):
    exp=int(exp)
#Si el exponente es positivo, el resultado es la potencia.
    if exp > 0:
        resultado = base**exp
#Si el exponente es 0, el resultado es 1.
    elif exp==0:
        resultado = 1
#Si el exponente es negativo, el resultado es 1/potencia con el exponente positivo.
    elif exp < 0:
        exp = abs(exp)
        resultado = float(1/(base**exp))
    else:
        abort(404)
    return render_template("potencia.html",base=base,exponente=exp,resultado=resultado)



#Página cuenta letras: Se accede con la URL /cuenta/palabra/letra (siendo palabra y letra dos cadenas cualquiera). Si la letra no es una cadena con un carácter se devuelve un error 404. 
# Se muestra una página donde hay un título "Cuanta letras", y muestra el siguiente mensaje "En la palabra ********* aparece *** veces el carácter ***".

@app.route('/cuenta/<cadena>/<caracter>',methods=["GET","POST"])
def contar(cadena,caracter):
    if len(caracter) != 1:
        abort(404)
    else:
        veces = cadena.count(caracter)
    return render_template("cuentaletras.html",palabra=cadena,veces=veces,letra=caracter) 



app.run("0.0.0.0",8000,debug=True)