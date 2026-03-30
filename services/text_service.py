# import requests
# from tenacity import retry, stop_after_attempt, wait_fixed
# from loguru import logger

# BASE_URL = "https://text.pollinations.ai/prompt/"

# @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
# def generate_text(prompt: str) -> str:
#     try:
#         url = BASE_URL + prompt
        
#         logger.info(f"Generating text for prompt: {prompt}")
        
#         response = requests.get(url, timeout=10)

#         if response.status_code == 200:
#             return response.text.strip()
#         else:
#             logger.error(f"API Error: {response.status_code}")
#             return "Error: Failed to generate text."

#     except Exception as e:
#         logger.exception(f"Exception occurred: {e}")
#         return "Error: Something went wrong."


import requests
from tenacity import retry, stop_after_attempt, wait_exponential
from loguru import logger
import urllib.parse

BASE_URL = "https://text.pollinations.ai/prompt/"

@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=2, max=10))
def generate_text(prompt: str) -> str:
    try:
        encoded_prompt = urllib.parse.quote(prompt.strip())
        url = BASE_URL + encoded_prompt

        logger.info(f"Generating text for prompt: {prompt}")

        response = requests.get(url, timeout=20)

        if response.status_code == 200:
            return response.text.strip()

        elif response.status_code == 429:
            logger.warning("Rate limit hit. Retrying...")
            raise Exception("Rate limit")

        else:
            logger.error(f"API Error: {response.status_code}")
            return "Error: Failed to generate text."

    except Exception as e:
        logger.exception(f"Exception: {e}")
        raise