import os
from dotenv import load_dotenv
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    HarmBlockThreshold,
    HarmCategory,
)
from langchain_core.prompts import ChatPromptTemplate
from groq import Groq

load_dotenv()

def rapgenerator(word):
    client = Groq()
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": f"Write a rap on {word}"
            }
        ],
        temperature=0,
        max_tokens=8192,
        top_p=1,
        stream=True,
        stop=None,
    )

    lyrics = ""
    for chunk in completion:
        lyrics = lyrics + str(chunk.choices[0].delta.content or "")
    return lyrics