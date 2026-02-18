import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('biblioteca.db')
    conn.row_factory = sqlite3.Row # Isso permite acessar os dados pelo nome da coluna
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    # Puxa todos os livros da tabela
    livros = conn.execute('SELECT * FROM livros').fetchall()
    conn.close()
    return render_template('index.html', livros=livros)

if __name__ == '__main__':
    app.run(debug=True)