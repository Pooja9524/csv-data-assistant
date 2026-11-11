import os
from dotenv import load_dotenv
from groq import Groq

# Read the settings from the .env file
load_dotenv()

MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")


def chat(system, user):
    # Create the connection using the key from .env
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    # Send the instructions (system) and the request (user) to the model
    response = client.chat.completions.create(
        model=MODEL,
        temperature=0,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    )

    # Return only the reply text
    return response.choices[0].message.content.strip()