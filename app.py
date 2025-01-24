# Imports
import json
from functions import create_ollama_client, email_checker

# Load the file that contains all the specifications
with open("specs.json", "r") as file:
    data = json.load(file)

# * Global Variables
APP_NAME = "Email Etiquette Enforcer"
llm = create_ollama_client("llama3")

# llm = create_ollama_client("llama3")
# wmt = data['prompts']['WMT-appropriate']
# results = email_checker("checker", "Hi. When is the deadline of the problem set?", wmt['rules'], wmt['salutations'], wmt['names'], llm)
# display(Markdown(results))