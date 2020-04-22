from flask import Flask, render_template
app = Flask(__name__)	

# Página principal
@app.route('/')
def inicio():
    return render_template("index.html")