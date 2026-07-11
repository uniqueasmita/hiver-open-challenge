from fastapi import FastAPI
import pandas as pd

from generator import generate_reply
from evaluator import evaluate

app = FastAPI()

dataset = pd.read_csv("data/dataset.csv")


@app.get("/")
def home():

    return {
        "message":"Hiver AI Email Suggestion System"
    }


@app.post("/generate")
def generate(email:str):

    reply = generate_reply(email)

    expected = ""

    for _, row in dataset.iterrows():

        if row["email"].lower() == email.lower():

            expected = row["response"]

            break

    if expected == "":
        expected = reply

    scores = evaluate(expected, reply)

    return {
        "incoming_email":email,
        "generated_reply":reply,
        "expected_reply":expected,
        "evaluation":scores
    }