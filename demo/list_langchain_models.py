from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI as LangChainOpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def list_langchain_openai_models():
    """
    List available models through LangChain's ChatOpenAI interface
    
    LangChain doesn't provide a direct way to list all available models,
    but we can try to instantiate with a common model and then check if
    the client provides model information.
    """
    try:
        # Create a ChatOpenAI instance
        chat_model = ChatOpenAI(model="gpt-3.5-turbo")
        
        # Print information about common models for ChatOpenAI
        print("Common models available for ChatOpenAI in LangChain:")
        print("-" * 60)
        
        common_models = [
            "gpt-4",
            "gpt-4-turbo",
            "gpt-4-turbo-preview",
            "gpt-4-0125-preview",
            "gpt-4-1106-preview",
            "gpt-4-vision-preview",
            "gpt-3.5-turbo",
            "gpt-3.5-turbo-0125",
            "gpt-3.5-turbo-1106",
            "gpt-3.5-turbo-instruct"
        ]
        
        for model_name in common_models:
            try:
                # Try to create a model with each name to see if it's supported
                # We don't actually call the model to save tokens
                temp_model = ChatOpenAI(model=model_name)
                print(f"- {model_name} (Available)")
            except Exception as e:
                # If there's an error that's not connectivity-related, the model might not be available
                if "does not exist" in str(e).lower():
                    print(f"- {model_name} (Not available)")
                else:
                    print(f"- {model_name} (Status unknown: {e})")
    
        print("\nNote: The actual availability may depend on your OpenAI account access and API version.")
        print("For a comprehensive list of all models, use the OpenAI API directly.")
        
    except Exception as e:
        print(f"Error initializing ChatOpenAI: {e}")
        print("Make sure your OPENAI_API_KEY is set correctly in the .env file.")

if __name__ == "__main__":
    # List models through the LangChain interface
    list_langchain_openai_models()
    
    print("\n\nTo see all available models directly from the OpenAI API, run list_openai_models.py")