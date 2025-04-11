from fastapi import FastAPI, Request
from llm_agent import responder_pergunta
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

# Banco de Dados
def conectar_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

@app.get("/")
def root():
    return {"mensagem": "🚗 API Vintage AI Rent no ar!"}

@app.get("/carros")
def listar_carros():
    try:
        conn = conectar_db()
        cur = conn.cursor()
        cur.execute("SELECT nome, ano, disponivel FROM carros")
        carros = cur.fetchall()
        cur.close()
        conn.close()

        lista = [{"nome": nome, "ano": ano, "disponivel": disponivel} for nome, ano, disponivel in carros]
        return {"carros": lista}
    except Exception as e:
        return {"erro": str(e)}

@app.post("/perguntar")
async def perguntar(request: Request):
    dados = await request.json()
    pergunta = dados.get("pergunta", "")
    resposta = responder_pergunta(pergunta)
    return {"pergunta": pergunta, "resposta": resposta}
