# Hiver AI Email Suggested Response System

## Overview

This project builds an AI-powered email response suggestion system using Google's Gemini LLM.

The system:

- Generates intelligent email replies.
- Uses a synthetic customer support email dataset.
- Evaluates generated responses using multiple NLP metrics.

---

## Dataset

The dataset contains synthetic customer support emails paired with human-written replies.

Categories include:

- Order delay
- Refund
- Password reset
- Subscription cancellation
- Billing
- Shipping
- Account issues
- Product information
- Business hours
- Technical support

The dataset was manually created to represent common customer support conversations.

---

## Response Generation

The project uses:

- Google Gemini API
- Prompt Engineering
- Dataset grounding

Incoming emails are sent to Gemini with context from the dataset to generate professional replies.

---

## Evaluation

Each generated response is evaluated using:

- Semantic Similarity
- ROUGE Score
- BLEU-style score
- Weighted Overall Score

Overall Score =
50% Semantic Similarity +
30% ROUGE +
20% BLEU

---

## Tech Stack

- Python
- FastAPI
- Google Gemini
- SentenceTransformers
- scikit-learn
- ROUGE

---

## How to Run

Install dependencies

```bash
pip install -r requirements.txt
```

Run server

```bash
uvicorn app:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

Test using any email query.

---

## AI Tools Used

- Google Gemini
- ChatGPT
- FastAPI
- SentenceTransformers

---