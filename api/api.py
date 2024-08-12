from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
from langchain_community.llms import Ollama
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

# Initialize the Ollama LLM with the desired model
llm = Ollama(model="llama2")

# Define a prompt template for generating a poem
prompt = ChatPromptTemplate.from_template("Write me a python code about {topic}")

# Add a route to the FastAPI app for generating poems using the Ollama model
add_routes(
    app,
    prompt | llm,  # Combine the prompt template with the LLM
    path="/poem"  # Define the API endpoint path
)

# Main entry point to run the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
