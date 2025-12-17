# LLM-Powered Market Segmentation App

A production-oriented web application that uses Large Language Models (LLMs) to convert unstructured customer text (reviews, survey responses, interview notes, call transcripts, etc.) into **market segments**, **persona-style summaries**, and **actionable marketing recommendations**.

This project is designed to be practical: fast setup, clear outputs, and safe handling of secrets (API keys).

---

## Table of Contents

- [Why this app](#why-this-app)
- [Key features](#key-features)
- [Demo](#demo)
- [Tech stack](#tech-stack)
- [Project structure](#project-structure)
- [Quickstart](#quickstart)
- [Configuration](#configuration)
- [Running the app](#running-the-app)
- [API (if FastAPI is included)](#api-if-fastapi-is-included)
- [Output format](#output-format)
- [Security](#security)
- [Troubleshooting](#troubleshooting)
- [Development workflow](#development-workflow)
- [Deployment notes](#deployment-notes)
- [How to update README and push](#how-to-update-readme-and-push)
- [License](#license)

---

## Why this app

Qualitative feedback is high-value but hard to use at scale. This app helps teams quickly:
- summarize raw feedback,
- identify distinct segments,
- articulate segment needs and motivations,
- and generate concrete messaging and next steps.

---

## Key Features

- **Text → Segments**: Generate market segments from unstructured text with consistent fields
- **Personas**: Persona-style summaries for each segment (traits, needs, pain points)
- **Actionable insights**: Messaging angles, positioning suggestions, and recommended actions
- **Interactive UI**: Streamlit UI for fast iteration, re-runs, and prompt tuning
- **Extensible prompting**: Prompt templates and parsing can be adapted per industry/domain
- **Safe by default**: Secrets are never committed; uses `config.env.example` as a template

---

## Demo

> Optional: add screenshots once you have them.

- UI screenshot: `docs/ui.png`
- Example output JSON: `docs/sample_output.json`

---

## Tech Stack

- **Python**
- **LangChain** (LLM orchestration)
- **Streamlit** (web UI)
- **FastAPI** (backend API, optional depending on repo)
- (Optional) **Uvicorn** for serving FastAPI

---

## Project Structure

> Your filenames may differ slightly. Adjust the commands below to match your repo.

```text
LLM_Powered_Market_Segmentation_App/
├── app.py or streamlit_app.py         # Streamlit entry file
├── api/                               # FastAPI app (optional)
│   └── main.py
├── src/                               # core logic: prompting, parsing, utils
├── requirements.txt
├── config.env.example                 # safe template (committed)
├── config.env                         # local secrets (NOT committed)
└── README.md




Quickstart
1) Clone the repository
git clone https://github.com/yc4970nyu/LLM_Powered_Market_Segmentation_App.git
cd LLM_Powered_Market_Segmentation_App

2) Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

3) Install dependencies
pip install -r requirements.txt

4) Create your local secrets file (DO NOT COMMIT)
cp config.env.example config.env


Edit config.env and set:

OPENAI_API_KEY=YOUR_KEY_HERE


✅ config.env must stay local-only and should be in .gitignore.

Configuration
Environment variables

This repo uses environment variables to configure the LLM client and runtime behavior.

Required

OPENAI_API_KEY

Recommended (optional)

OPENAI_MODEL (example: gpt-4o-mini)

TEMPERATURE (example: 0.2)

MAX_TOKENS (example: 1200)

Example config.env.example
OPENAI_API_KEY=YOUR_KEY_HERE
OPENAI_MODEL=gpt-4o-mini
TEMPERATURE=0.2
MAX_TOKENS=1200

Make sure secrets are ignored

Your .gitignore should include at least:

config.env
.env
.env.*
__pycache__/
*.pyc
.DS_Store

Running the App
Option A — Run Streamlit UI (most common)

Identify your Streamlit entry file (app.py or streamlit_app.py).

streamlit run app.py


If the entry is different:

streamlit run streamlit_app.py


Streamlit will print a local URL (usually http://localhost:8501).

Option B — Run FastAPI backend (if included)

If you have api/main.py:

uvicorn api.main:app --reload --port 8000


Open API docs:

Swagger: http://localhost:8000/docs

API (if FastAPI is included)

If your repo does not include FastAPI endpoints, you can delete this section.

Example endpoints (typical)

POST /segment — generate segments/personas from raw text input

POST /refine — refine previous segments with new constraints or feedback

GET /health — health check

Example request
{
  "text": "I love how fast delivery is, but the packaging is always damaged...",
  "num_segments": 4,
  "style": "marketing",
  "output_format": "json"
}

Example response (high-level)
{
  "segments": [
    {
      "name": "Speed-First Shoppers",
      "summary": "Prioritize delivery speed and convenience.",
      "needs": ["fast shipping", "reliable tracking"],
      "pain_points": ["packaging quality", "damaged items"],
      "messaging": ["Fast delivery you can count on", "Secure packaging upgrades"],
      "recommended_actions": ["Improve packaging QA", "Offer delivery guarantees"]
    }
  ],
  "metadata": {
    "model": "gpt-4o-mini",
    "temperature": 0.2
  }
}
