import sqlite3

def inserir_dados():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    # Inserindo 3 livros de teste
    livros = [
        ('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 'Infantil'),
        ('Dom Casmurro', 'Machado de Assis', 'Clássico'),
        ('A Menina que Roubava Livros', 'Markus Zusak', 'Drama')
    ]
    
    cursor.executemany('INSERT INTO livros (titulo, autor, categoria) VALUES (?, ?, ?)', livros)
    
    conn.commit()
    conn.close()
    print("📚 3 Livros inseridos com sucesso!")

if __name__ == '__main__':
    inserir_dados()