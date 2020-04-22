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

# Página libros: A esta página se entra con la URL /libro/codigo (siendo código un número entero). Tienes que buscar el código en el fichero libros.xml 
# y debes mostrar una página con un título "Biblioteca" y el nombre del libro y el autor. Si no existe el código debe devolver una respuesta 404.

from lxml import etree

@app.route('/libro/<codigo>',methods=["GET","POST"])
def libros(codigo):
    biblioteca = etree.parse('libros.xml')
    if codigo in biblioteca.xpath('//libro/codigo/text()'):
        autor = biblioteca.xpath('//libro[codigo="%s"]/autor/text()'%(codigo))[0]
        return render_template("libros.html", libro=nombre_libro) 
    else:
        abort(404)


app.run("0.0.0.0",8000,debug=True)