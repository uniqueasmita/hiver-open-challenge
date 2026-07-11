import google.generativeai as genai
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


model = genai.GenerativeModel("gemini-flash-latest")

df = pd.read_csv("data/dataset.csv")

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(df["email"])


def generate_reply(user_email):

    query = vectorizer.transform([user_email])

    similarities = cosine_similarity(query, X)[0]

    top = similarities.argsort()[-3:][::-1]

    context = ""

    for i in top:
        context += f"""
Customer Email:
{df.iloc[i]['email']}

Reply:
{df.iloc[i]['response']}

"""

    prompt = f"""
You are a customer support assistant.

Use these previous examples:

{context}

Now write a professional reply for:

{user_email}

Only return the email reply.
"""

    response = model.generate_content(prompt)

    return response.text