# Hiver AI Email Suggested Response System

## Overview

This project is an AI-powered email reply suggestion system built as part of the Hiver Open Challenge.

The application generates professional responses for incoming customer support emails using Google's Gemini LLM. It is grounded with a synthetic customer support dataset and evaluates the quality of every generated response using multiple NLP evaluation metrics.

## Features

- AI-powered email response generation using Google Gemini
- Synthetic customer support email dataset
- FastAPI backend
- Simple HTML web interface
- Automatic response evaluation
- JSON API for integration
- End-to-end runnable project

---

## Dataset

The project uses a manually created synthetic dataset of customer support emails and their corresponding responses.

The dataset covers common customer support scenarios, including:

- Order delays
- Refund requests
- Password reset
- Billing issues
- Subscription cancellation
- Shipping questions
- Business hours
- Account access
- Product information
- Technical support

The dataset was intentionally designed to represent realistic customer support conversations while remaining simple, consistent, and suitable for evaluating AI-generated responses.

---

## Response Generation

The system uses Google's Gemini LLM to generate responses.

### Workflow

1. User enters an incoming email.
2. The system searches the dataset for a similar support example.
3. Relevant context is provided to Gemini through prompt engineering.
4. Gemini generates a professional customer support reply.
5. The generated reply is evaluated against the expected response from the dataset.

This approach combines dataset grounding with a Large Language Model instead of using a traditional machine learning classifier.

---

## Evaluation Method

Each generated response is evaluated using multiple NLP metrics.

### Metrics Used

- **Semantic Similarity** (Sentence Transformers)
- **BLEU Score**
- **ROUGE Score**

### Overall Score

The overall quality score is calculated as:

```
Overall Score =
50% Semantic Similarity
+ 30% ROUGE
+ 20% BLEU
```

These metrics provide both semantic and lexical evaluation instead of relying on exact text matching.

---

## Tech Stack

- Python
- FastAPI
- HTML / JavaScript
- Google Gemini API
- Sentence Transformers
- scikit-learn
- ROUGE
- Pandas

---

## Project Structure

```
hiver-open-challenge/
│
├── app.py
├── generator.py
├── evaluator.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── data/
    └── dataset.csv
```

---

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Project

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Open the application in your browser:

```
http://127.0.0.1:8000
```

The application provides a simple web interface where users can:

- Enter an email
- Generate an AI response
- View evaluation metrics
- See the overall quality score

---

## API Endpoint

### Generate Reply

**POST**

```
/generate
```

Example:

```
POST /generate?email=I forgot my password.
```

The API returns:

- Generated Reply
- Expected Reply
- Semantic Similarity
- BLEU Score
- ROUGE Score
- Overall Score

---

## AI Tools Used

This project was developed using:

- Google Gemini API
- ChatGPT (for development assistance)
- FastAPI
- Sentence Transformers

---

## Future Improvements

- Retrieval-Augmented Generation (RAG)
- Larger real-world support email dataset
- Conversation history support
- Email intent classification
- Response tone customization
- User authentication
- Dashboard for evaluation analytics