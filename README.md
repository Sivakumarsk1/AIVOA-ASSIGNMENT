# AIVOA - AI-Powered Customer Complaint Management System

An AI-powered Customer Complaint Management System for the pharmaceutical manufacturing industry (API & FDF), built as part of the AIVOA Full Stack Developer Assessment.

## Architecture

```
┌──────────────────────────────────────────────────────────────┐
│              FRONTEND (React + Redux + Vite)                 │
│  ComplaintForm  ←→  AIAssistantPanel                         │
│  (Log Form)         (Upload, Extract, Chat)                  │
└──────────────────────┬───────────────────────────────────────┘
                       │  REST API
┌──────────────────────▼───────────────────────────────────────┐
│              BACKEND (FastAPI + Python)                       │
│  Routes → Services → LangGraph Agents → Groq LLM            │
└──────────────────────┬───────────────────────────────────────┘
                       │
┌──────────────────────▼───────────────────────────────────────┐
│              DATABASE (SQLite / PostgreSQL)                   │
└──────────────────────────────────────────────────────────────┘
```

##  Technology Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | React 18, Redux Toolkit (RTK Query), React Router, Vite |
| **Backend** | Python, FastAPI, SQLAlchemy |
| **AI Framework** | LangGraph (Agent Workflow) |
| **LLM** | Groq API - `gemma2-9b-it` model |
| **Database** | SQLite (dev) / PostgreSQL (prod) |
| **Font** | Google Inter |

## Features

### Core Features
- **Complaint Logging Form** — 4-section form matching pharmaceutical QMS standards
- **AI Document Extraction** — Upload complaint documents (PDF, DOCX, TXT, EML) or paste text
- **AI-Powered Field Population** — LLM extracts complaint details and auto-fills the form
- **AI Chat Assistant** — Conversational AI for complaint-related queries
- **CRUD Operations** — Create, read, update, delete complaints

### Bonus AI Features
-  **Complaint Completeness Checker** — Scores how complete the complaint data is (0-100%)
-  **Root Cause Recommendation** — AI suggests possible root causes based on complaint details
-  **Duplicate Complaint Detection** — Compares against existing complaints for duplicates
-  **CAPA Recommendation** — Suggests Corrective and Preventive Actions
-  **Complaint Summary** — Generates concise AI summary of the complaint
-  **AI Risk Classification** — Classifies risk level (Critical/High/Medium/Low)

##  Setup & Installation

### Prerequisites
- **Node.js** >= 18.x
- **Python** >= 3.10
- **Groq API Key** — Get one at [https://console.groq.com](https://console.groq.com)

### Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
copy .env.example .env
# Edit .env and add your GROQ_API_KEY

# Run the server
uvicorn app.main:app --reload --port 8000
```

The backend will be available at `http://localhost:8000`
API documentation at `http://localhost:8000/docs`

### Frontend Setup

```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

The frontend will be available at `http://localhost:5173`

## Project Structure

```
naukricompanyproject/
├── frontend/                    # React + Redux application
│   ├── src/
│   │   ├── app/                 # Redux store & hooks
│   │   ├── features/
│   │   │   ├── complaints/      # Complaint form & API
│   │   │   └── ai/              # AI assistant panel & API
│   │   ├── components/          # Shared UI components
│   │   ├── pages/               # Page components
│   │   └── main.jsx             # Entry point
│   └── package.json
│
├── backend/                     # FastAPI application
│   ├── app/
│   │   ├── agents/              # LangGraph workflow
│   │   │   ├── graph.py         # Agent graph definition
│   │   │   ├── nodes.py         # Agent node functions
│   │   │   └── state.py         # Agent state schema
│   │   ├── models/              # SQLAlchemy models
│   │   ├── schemas/             # Pydantic schemas
│   │   ├── routes/              # API endpoints
│   │   ├── services/            # Business logic
│   │   └── main.py              # FastAPI app
│   └── requirements.txt
│
├── sample_data/                 # Sample complaint documents
│   ├── complaint_email_1.txt    # Foreign particle complaint
│   ├── complaint_email_2.txt    # Packaging defect complaint
│   └── complaint_report.txt     # API quality complaint
│
└── README.md
```

##  LangGraph Agent Workflow

The AI extraction agent uses a multi-step LangGraph workflow:

```
START → Parse Document → Extract Fields → Classify Severity
  → Assess Risk → Check Completeness → Root Cause Analysis
  → CAPA Recommendation → Generate Summary → END
```

Each node uses the Groq `gemma2-9b-it` model with pharmaceutical-specific prompts.

##  API Endpoints

### Complaints
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/complaints` | List all complaints |
| `POST` | `/api/complaints` | Create complaint |
| `GET` | `/api/complaints/{id}` | Get complaint |
| `PUT` | `/api/complaints/{id}` | Update complaint |
| `DELETE` | `/api/complaints/{id}` | Delete complaint |

### AI
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/ai/extract` | Extract from file upload |
| `POST` | `/api/ai/extract-text` | Extract from pasted text |
| `POST` | `/api/ai/chat` | Chat with AI assistant |
| `POST` | `/api/ai/classify-risk` | AI risk classification |
| `POST` | `/api/ai/check-completeness` | Completeness scoring |
| `POST` | `/api/ai/recommend-capa` | CAPA recommendation |
| `POST` | `/api/ai/detect-duplicate` | Duplicate detection |
| `POST` | `/api/ai/summarize` | Generate summary |
| `POST` | `/api/ai/root-cause` | Root cause analysis |

##  Demo

### Sample Workflow
1. Open the application at `http://localhost:5173`
2. In the AI Assistant panel, click "Paste Complaint Text / Email"
3. Paste one of the sample complaints from `sample_data/`
4. Watch the AI extract fields and populate the form
5. Review the extracted data, severity, and priority
6. Chat with the AI assistant for clarification
7. Click "Save Complaint" to persist

##  Key Design Decisions

1. **SQLite for Development** — Zero external dependencies, easy to set up. Can switch to PostgreSQL for production.
2. **LangGraph Multi-Step Pipeline** — Each AI task (extraction, classification, CAPA, etc.) is a separate node, enabling modular testing and easy extension.
3. **RTK Query** — Automatic caching, loading states, and error handling for API calls.
4. **Groq gemma2-9b-it** — Fast inference with good structured output capabilities for pharmaceutical domain.
5. **Pharmaceutical QMS Context** — All AI prompts are crafted with pharma domain knowledge (ICH guidelines, GMP, CAPA workflows).

##  Author

Built for the AIVOA Round 1 Full Stack Developer Assessment.

---

*AI tools (Gemini, Claude) were used for code generation. All code has been reviewed, understood, and adapted to match the required workflow.*
