# Mini API de Usuários

Projeto de exemplo em **Python** com **FastAPI** e **SQLite**, criando uma API simples de CRUD para usuários.

---

## Tecnologias

- Python
- FastAPI
- SQLite
- Pydantic

---

## Como rodar

1. Clonar o repositório:

```
git clone https://github.com/jlcambraia/users-fastapi-sqlite.git
cd mini-api
```

2. Criar ambiente virtual (opcional):

```
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows

```

3. Instalar dependências:

```
pip install -r requirements.txt
```

4. Inicializar banco de dados:

```
python database.py
```

5. Rodar API:

```
uvicorn main:app --reload
```

---

## Endpoints

| Método | Rota             | Descrição                                                      |
| ------ | ---------------- | -------------------------------------------------------------- |
| GET    | `/`              | Mensagem de boas-vindas e contagem de usuários                 |
| GET    | `/users`         | Lista todos os usuários                                        |
| POST   | `/users`         | Cria um novo usuário (JSON: `{"name": "...", "email": "..."}`) |
| GET    | `/users/{email}` | Busca usuário por email                                        |
| PUT    | `/users/{email}` | Atualiza usuário pelo email                                    |
| DELETE | `/users/{email}` | Deleta usuário pelo email                                      |

---

## Observações

- Banco SQLite usado apenas para teste rápido, não para produção.
- Emails são únicos. Tentativas de duplicação retornam erro 400.

---

## Exemplo de uso

### Criar usuário

```
curl -X POST "http://127.0.0.1:8000/users" \
-H "Content-Type: application/json" \
-d '{"name": "João", "email": "joao@example.com"}'
```

### Listar usuário

```
curl http://127.0.0.1:8000/users
```

---

## Agradecimentos

Obrigado por conferir este projeto!  
Espero que ele seja útil como referência de aprendizado em FastAPI e SQLite.  
Contribuições e feedbacks são bem-vindos!
