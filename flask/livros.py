# app.py
from flask import Flask, render_template
from models import Livro

app = Flask(__name__)

# Lista de livros
livros = []

@app.route(livros)
def listar_livros()
    return render_template(lista_livros.html, livros=livros)
