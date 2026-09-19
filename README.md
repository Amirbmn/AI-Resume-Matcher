# AI Resume–Job Matcher

An NLP-based application that analyzes a resume against a job description and estimates how well they match.

The project combines traditional NLP techniques with semantic similarity to identify matching skills, missing skills, relevant resume content, and other important compatibility factors.

## Features

* Upload a resume in **PDF or TXT** format
* Extract and process resume text using **spaCy**
* Detect technical skills from the resume and job description
* Identify:

  * Matching skills
  * Missing skills
* Calculate:

  * Skill match score
  * Keyword similarity
  * Semantic similarity
  * Experience match
  * Education match
  * Role match
  * Overall match score
* Find resume passages that are most relevant to the job
* Generate recommendations based on missing skills
* Interactive interface built with **Streamlit**

## Tech Stack

* **Python**
* **Streamlit** — web interface
* **PyMuPDF** — PDF text extraction
* **spaCy** — NLP and entity processing
* **scikit-learn** — TF-IDF and cosine similarity
* **Sentence Transformers** — semantic similarity
* **Regex + JSON** — skill and experience extraction

## How It Works

```text
Resume + Job Description
          ↓
     Text Extraction
          ↓
      NLP Processing
          ↓
     Skill Extraction
          ↓
   ┌──────────────────────┐
   │ Resume–Job Matching  │
   └──────────────────────┘
          ↓
  ┌───────┼────────┬──────────┐
  ↓       ↓        ↓          ↓
Skills  Keywords  Semantic  Experience
  │       │        │          │
  └───────┴────────┴──────────┘
              ↓
        Overall Match Score
              ↓
   Recommendations + Relevant
        Resume Passages
```

## Project Structure

```text
ai-matcher-nlp/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── skills.json
└── src/
    ├── extractor.py
    ├── nlp.py
    ├── skills.py
    ├── similarity.py
    └── matcher.py
```

## Installation

Clone the repository and create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install the spaCy English model:

```bash
python -m spacy download en_core_web_sm
```

## Run the Application

```bash
streamlit run app.py
```

Then open the local Streamlit URL in your browser.

## Matching Score

The overall score is calculated from several components:

| Component           | Weight |
| ------------------- | -----: |
| Skill Match         |    30% |
| Semantic Similarity |    25% |
| Keyword Similarity  |    15% |
| Experience Match    |    15% |
| Education Match     |    10% |
| Role Match          |     5% |

These weights are currently heuristic and can be improved through further testing.

