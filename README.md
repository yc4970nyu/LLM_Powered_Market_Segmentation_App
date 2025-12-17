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


