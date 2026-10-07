"""Flask portfolio: edit templates, static/style.css, and data/portfolio.json."""
import json
from pathlib import Path
from flask import Flask, render_template

BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__)

@app.get("/")
def home():
    with (BASE_DIR / "data" / "portfolio.json").open(encoding="utf-8") as handle:
        content = json.load(handle)
    return render_template("index.html", **content)

@app.get("/healthz")
def health():
    return {"status": "ok"}
