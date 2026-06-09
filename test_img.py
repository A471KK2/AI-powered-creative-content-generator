# test_image.py

from services.image_service import generate_image

img = generate_image("A futuristic cyberpunk cat with blue neon eyes")

print(type(img))

if img:
    img.show()
