import sqlite3


def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """
    )
    conn.commit()
    conn.close()


# Inicializar banco
if __name__ == "__main__":
    init_db()
    print("Banco criado com sucesso!")
