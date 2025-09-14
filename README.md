# PetSavior 🐾 — Connecting Shelters to People

<small>PetSavior helps people discover adoptable pets by aggregating listings from participating shelters and making them searchable, filterable, and easy to share.</small>


---


## Table of Contents
- <small>[Features](#features)</small>

- <small>[Live Demo](#live-demo)</small>

- <small>[Architecture](#architecture)</small>

- <small>[Project Structure](#project-structure)</small>

- <small>[Tech Stack](#tech-stack)</small>

- <small>[Team](#team)</small>


---


## Features
- <small>🔎 **Smart search & filters** — find pets by species, breed, age, size, and location.</small>
- <small>🏠 **Shelter aggregation** — pulls listings from participating shelters into a single, consistent format.</small>
- <small>🖼️ **Clean, shareable profiles** — readable pet cards with images and contact info.</small>
- <small>⚡ **Fast API** — lightweight Python backend, ready for production hardening.</small>
- <small>🧹 **Resilient scraping** — modular scrapers normalized to a common schema.</small>
- <small>📦 **One-file config** — simple `.env` to run locally or in the cloud.</small>


---


## Live Demo
- <small>**Web:** https://petsavior.onrender.com</small>


---


## Architecture
<small>PetSavior is split into four modules:</small>

1. <small>**`backend/`** — REST API for searching pets, health checks, and serving frontend pages/assets.</small>
2. <small>**`frontend/`** — UI templates/assets that render search, listings, and pet detail pages.</small>
3. <small>**`database/`** — DB schema, migrations, and data access layer (ORM).</small>
4. <small>**`scraping/`** — pluggable scrapers that fetch and normalize shelter listings.</small>

<small>**Data flow (high level):**  
Shelter Websites ──► scraping/ ──► database/ ──► backend/ ──► frontend/</small>


---


## Project Structure
PetSavior/
├─ backend/ # API server (routers, services, models, config)
├─ frontend/ # Templates/static or client app for the UI
├─ database/ # DB schema, migrations, ORM models
├─ scraping/ # Individual scrapers + normalization
├─ requirements.txt # Python dependencies
├─ test_main.http # Handy HTTP requests for local API testing
└─ README.md


---


## Tech Stack
- <small>**Language:** Python 3.10+</small>
- <small>**Backend:** FastAPI (ASGI), Uvicorn/Gunicorn</small>
- <small>**DB/ORM:** SQLAlchemy (SQLite locally; Postgres-ready for production)</small>
- <small>**Scraping:** requests, beautifulsoup4 (pluggable per-shelter adapters)</small>
- <small>**Deploy:** Render</small>


---


## Team
- <small>Dmitriy Gamolya</small>  
- <small>Brandon Hu</small>  
- <small>Jianqi (Alex) Shi</small>  
- <small>Andy Martin-Valencia</small>








