# Tidio IA Widget

Petit projet de démonstration : un backend **FastAPI** qui se connecte à l’API OpenAI, 
et un widget de chat simple en **HTML/JS** à intégrer sur n’importe quel site.

## 🚀 Fonctionnalités
- API `/chat` pour discuter avec l’IA (modèle OpenAI `gpt-4o-mini`)
- Prompts personnalisés par client (ex: pizzeria La Stella)
- Widget de chat léger à coller dans un site web

## 📦 Installation locale
```bash
git clone https://github.com/ILAN-cloud/tidio-ia-widget.git
cd tidio-ia-widget
pip install -r requirements.txt
export OPENAI_API_KEY="sk-..."   # (Windows: set OPENAI_API_KEY=...)
uvicorn main:app --reload --port 8000
