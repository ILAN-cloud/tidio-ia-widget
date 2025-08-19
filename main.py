
# main.py
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI

# --- config ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("Missing OPENAI_API_KEY environment variable")
client = OpenAI(api_key=OPENAI_API_KEY)

# Exemple de prompts par client (remplace par une vraie BDD plus tard)
PROMPTS = {
    "la-stella-12e": (
        "Tu es l’assistant officiel de La Stella (pizzeria, Paris 12e). "
        "Tonalité: chaleureuse et concise. Objectif: aider à réserver/commander. "
        "Horaires: 11h30-14h30 et 18h30-22h30. Tel: 01 23 45 67 89. "
        "Offre: pizzas napolitaines, menu midi 14,90€, option sans gluten. "
        "Règles: Réponds en 3–5 phrases. Ne pas inventer; si info manquante, le dire."
    )
}

app = FastAPI(title="Caro Chat Backend", version="1.0.0")

# CORS: autorise tes domaines d'installation (remplace * en prod)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],    # ⚠️ en production, remplace par la liste des domaines
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatIn(BaseModel):
    client_id: str
    message: str
    session_id: str | None = None

@app.get("/")
def health():
    return {"ok": True}

@app.post("/chat")
def chat(inp: ChatIn):
    system_prompt = PROMPTS.get(inp.client_id, "Tu es un assistant utile et concis.")
    # Appel modèle via Chat Completions
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.3,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": inp.message},
        ],
    )
    reply = completion.choices[0].message.content
    return {"reply": reply}
