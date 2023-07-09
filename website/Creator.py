"""
Creator.py
-----------------
Create course with text and images using Create_Course
"""

import os
import vertexai
import requests
from PIL import Image
from io import BytesIO
import openai

openai.api_key = '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'

from vertexai.language_models import TextGenerationModel

from dotenv import load_dotenv

load_dotenv()

vertexai.init(project="ghc-015", location="us-central1")
os.getenv("GOOGLE_APPLICATION_CREDENTIALS")


def Create_Course_Social(user_input):
    prompt = """Explain social norms""".strip()

    parameters = {
        "temperature": 0.2,
        "max_output_tokens": 10,
        "top_p": 0.8,
        "top_k": 40}

    model = TextGenerationModel.from_pretrained("text-bison@001")
    response = model.predict(prompt, **parameters)
    print(response)

    url = "https://adibvafa.github.io/Portfolio/assets/images/Adibvafa.png"
    images = [url, url, url, url, url]
    print(images)

    paragraphs = [f"Paragraph1: {response.text[10:-3]})", f"Paragraph1: {response.text[10:-3]})",
                  f"Paragraph1: {response.text[10:-3]})", f"Paragraph1: {response.text[10:-3]})",
                  f"Paragraph1: {response.text[10:-3]})"]
    print(len(paragraphs))

    return paragraphs, images
