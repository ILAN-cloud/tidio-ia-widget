
# Widget Chat IA + Backend (FastAPI)

Installation rapide locale :
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
export OPENAI_API_KEY="sk-..."                      # Windows: set OPENAI_API_KEY=...
uvicorn main:app --reload --port 8000
```

Test:
```bash
curl -X POST http://127.0.0.1:8000/chat       -H "Content-Type: application/json"       -d '{"client_id":"la-stella-12e","message":"Bonjour, vous ouvrez à quelle heure ?"}'
```

Déploiement (Render/Railway) :
- Déploie ce repo comme service web Python
- Commande de démarrage: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- Var d'env: `OPENAI_API_KEY`
- Note l'URL publique: ex. https://api.ton-domaine.com

Intégration front:
- Ouvre `web/index.html` et colle le bloc sur le site client.
- Change `api_base` et `client_id`.
