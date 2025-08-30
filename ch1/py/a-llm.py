from langchain_openai.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo")

response = model.invoke("The sky is")
print(response.content)
