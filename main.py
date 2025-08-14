from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from typing import List

app = FastAPI(title="Mini API de Usuários")


class User(BaseModel):
    name: str
    email: str


def get_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.get("/")
def hello_visitor():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    conn.close()
    return {"message": f"Olá! Nós temos {count} usuários no banco de dados."}


@app.get("/users", response_model=List[User])
def list_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, email FROM users")
    users = cursor.fetchall()
    conn.close()
    return [dict(user) for user in users]


@app.post("/users")
def create_user(user: User):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)", (user.name, user.email)
        )
        conn.commit()
        return {
            "message": "Usuário criado com sucesso!",
            "user": {"name": user.name, "email": user.email},
        }
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Email já existe")
    finally:
        conn.close()


@app.get("/users/{email}")
def get_user(email: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, email FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    if user:
        return dict(user)
    else:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")


@app.put("/users/{email}")
def update_user(email: str, user: User):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET name = ?, email = ? WHERE email = ?",
        (user.name, user.email, email),
    )
    conn.commit()
    updated = cursor.rowcount
    conn.close()
    if updated:
        return {"message": "Usuário atualizado com sucesso"}
    else:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")


@app.delete("/users/{email}")
def delete_user(email: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE email = ?", (email,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    if deleted:
        return {"message": "Usuário deletado com sucesso"}
    else:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
