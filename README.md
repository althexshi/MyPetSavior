# PetSavior 🐾 — Connecting Shelters to People

<small>PetSavior helps people discover adoptable pets by aggregating listings from participating shelters and making them searchable, filterable, and easy to share.</small>

<img width="2188" height="1721" alt="ASOC" src="https://github.com/user-attachments/assets/35e130dc-e746-41ec-878c-098fd9d1ece0" />


---


## Table of Contents
- <small>[Features](#features)</small>

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


---


## Architecture
<small>PetSavior runs as a single ASGI app with Python-powered UI:</small>

1. <small>**`api/` (FastAPI)** — JSON endpoints for pets, shelters, and health checks.</small>  
2. <small>**`ui/` (NiceGUI)** — Python-based pages/components (no HTML templates needed).</small>  
3. <small>**`database/`** — DB schema, migrations, and data access layer (SQLAlchemy).</small>  
4. <small>**`scraping/`** — pluggable scrapers that fetch and normalize shelter listings.</small>  

**Data flow (high level):**

```text
Shelter Websites 
     │
     ▼
  scraping/
     │
     ▼
  database/
     │
     ▼
  backend/
     │
     ▼
  frontend/
```


---


## Project Structure

```bash
PetSavior/
├── backend/         # API server (routers, services, models, config)
├── frontend/        # Templates/static files or client app for the UI
├── database/        # DB schema, migrations, ORM models
├── scraping/        # Individual scrapers + normalization
│
├── requirements.txt # Python dependencies
├── test_main.http   # Handy HTTP requests for local API testing
└── README.md        # Project documentation
```


---


## Tech Stack
- <small>**Language:** Python 3.10+</small>
- <small>**Backend/UI:** NiceGUI (Python-based UI) + FastAPI (ASGI)</small>
- <small>**Server:** Uvicorn/Gunicorn</small>
- <small>**DB/ORM:** SQLAlchemy (SQLite locally; Postgres-ready for production)</small>
- <small>**Scraping:** requests, beautifulsoup4 (pluggable per-shelter adapters)</small>
- <small>**Deploy:** Render </small>




---


## Team
- <small>Dmitriy Gamolya</small>  
- <small>Brandon Hu</small>  
- <small>Jianqi (Alex) Shi</small>  
- <small>Andy Martin-Valencia</small>






