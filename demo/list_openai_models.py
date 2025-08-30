from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(
    # This will use the OPENAI_API_KEY environment variable from your .env file
)

try:
    # Retrieve all available models
    models = client.models.list()

    print("Available OpenAI Models:")
    print("-" * 50)

    # Filter for only GPT models if you want
    gpt_models = [model for model in models.data if "gpt" in model.id.lower()]
    
    # Print all models
    print("\nAll Models:")
    for model in models.data:
        print(f"- {model.id}")

    # Print GPT models specifically
    print("\nGPT Models (for use with ChatOpenAI):")
    for model in gpt_models:
        print(f"- {model.id}")

except Exception as e:
    print(f"Error retrieving models: {e}")