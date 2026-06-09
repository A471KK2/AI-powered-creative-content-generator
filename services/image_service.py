# import requests
# from tenacity import retry, stop_after_attempt, wait_fixed
# from loguru import logger
# import os
# from dotenv import load_dotenv

# load_dotenv()

# API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"

# headers = {
#     "Authorization": f"Bearer {API_KEY}"
# }

# @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
# def generate_image(prompt: str):
#     try:
#         logger.info(f"Generating image for prompt: {prompt}")

#         response = requests.post(
#             API_URL,
#             headers=headers,
#             json={"inputs": prompt},
#             timeout=30
#         )

#         if response.status_code == 200:
#             return response.content  # raw image bytes
#         else:
#             logger.error(f"API Error: {response.status_code} - {response.text}")
#             return None

#     except Exception as e:
#         logger.exception(f"Exception occurred: {e}")
#         return None


# import requests
# from tenacity import retry, stop_after_attempt, wait_exponential
# from loguru import logger
# import os
# from dotenv import load_dotenv

# load_dotenv()

# API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-2"

# headers = {
#     "Authorization": f"Bearer {API_KEY}"
# }

# @retry(stop=stop_after_attempt(5), wait=wait_exponential(min=2, max=10))
# def generate_image(prompt: str):
#     try:
#         logger.info(f"Generating image for prompt: {prompt}")

#         response = requests.post(
#             API_URL,
#             headers=headers,
#             json={"inputs": prompt},
#             timeout=60
#         )

#         if response.status_code == 200:
#             return response.content

#         else:
#             logger.error(f"API Error: {response.status_code} - {response.text}")
#             return None

#     except Exception as e:
#         logger.exception(f"Exception: {e}")
#         return None


# import requests
# from tenacity import retry, stop_after_attempt, wait_exponential
# from loguru import logger
# import os
# from dotenv import load_dotenv

# load_dotenv()

# API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"

# headers = {
#     "Authorization": f"Bearer {API_KEY}"
# }

# @retry(stop=stop_after_attempt(5), wait=wait_exponential(min=2, max=10))
# def generate_image(prompt: str):
#     try:
#         logger.info(f"Generating image for prompt: {prompt}")

#         response = requests.post(
#             API_URL,
#             headers=headers,
#             json={"inputs": prompt},
#             timeout=60
#         )

#         if response.status_code == 200:
#             return response.content

#         elif response.status_code == 503:
#             logger.warning("Model loading, retrying...")
#             raise Exception("Model loading")

#         else:
#             logger.error(f"API Error: {response.status_code} - {response.text}")
#             return None

#     except Exception as e:
#         logger.exception(f"Exception: {e}")
#         return None

###############################################################################################################

# import requests
# from tenacity import retry, stop_after_attempt, wait_exponential
# from loguru import logger
# import os
# from dotenv import load_dotenv
# from requests.exceptions import ReadTimeout

# # Load env variables
# load_dotenv()

# API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"

# headers = {
#     "Authorization": f"Bearer {API_KEY}"
# }

# @retry(stop=stop_after_attempt(3), wait=wait_exponential(min=3, max=15))
# def generate_image(prompt: str):
#     try:
#         logger.info(f"Generating image for prompt: {prompt}")

#         response = requests.post(
#             API_URL,
#             headers=headers,
#             json={"inputs": prompt},
#             timeout=90
#         )

#         if response.status_code == 200:
#             return response.content

#         elif response.status_code == 503:
#             logger.warning("Model loading... retrying")
#             raise Exception("Model loading")

#         else:
#             logger.error(f"API Error: {response.status_code} - {response.text}")
#             return None

#     except ReadTimeout:
#         logger.error("Timeout: HuggingFace is busy")
#         return None

#     except Exception as e:
#         logger.exception(f"Exception: {e}")
#         return None


##########################################################################################################

import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from loguru import logger
from tenacity import retry, stop_after_attempt, wait_exponential

load_dotenv()

client = InferenceClient(token=os.getenv("HF_TOKEN"))


@retry(stop=stop_after_attempt(3), wait=wait_exponential(min=2, max=10))
def generate_image(prompt: str):

    try:

        logger.info(f"Generating image: {prompt}")

        image = client.text_to_image(prompt, model="black-forest-labs/FLUX.1-schnell")

        return image

    except Exception as e:

        logger.exception(f"Image generation failed: {e}")

        return None
