import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(token=os.getenv("HF_TOKEN"))

image = client.text_to_image(
    "A futuristic cyberpunk cat with glowing blue eyes",
    model="black-forest-labs/FLUX.1-schnell",
)

print(type(image))

image.save("test_output.png")

print("Image saved successfully")
