
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load API key from .env
load_dotenv()

# Initialize the LangChain chat model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0
)

# Ask for exactly 5 healthy winter soup ideas
prompt = """
Suggest exactly 5 healthy soup ideas for winter.

Consider soups that are nutritious, warming, and made with wholesome
ingredients such as vegetables, lentils, beans, or lean protein.

Format requirements:
- Number the ideas from 1 to 5.
- Write exactly one line per idea.
- Include the soup name and its main healthy ingredients.
- Do not include an introduction, conclusion, or preamble.
"""

# Invoke the model
reply = llm.invoke(prompt)

# Print only the reply text
print(reply.content)
