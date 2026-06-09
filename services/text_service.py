import os
import time

from dotenv import load_dotenv
from google import genai
from loguru import logger

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_text(prompt: str):

    models = ["gemini-2.0-flash", "gemini-2.0-flash-lite", "gemini-2.5-flash"]

    for model_name in models:

        try:

            logger.info(f"Trying model: {model_name}")

            response = client.models.generate_content(model=model_name, contents=prompt)

            return response.text

        except Exception as e:

            logger.warning(f"{model_name} failed: {e}")

            time.sleep(2)

    return "All Gemini models are currently busy. Please try again."
