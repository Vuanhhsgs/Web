db_path = 'C:/Users/Admin/Desktop/Solution_database'
import os
# List all files in the specified folder
solution_db = [f for f in os.listdir(db_path) if os.path.isfile(os.path.join(db_path, f))]

from ollama import chat
from ollama import ChatResponse
import json
output_lemma = {}
for solution_file in solution_db:
  file_path = os.path.join(db_path, solution_file)
  with open(file_path, "r", encoding="utf-8") as f:
        solution_content = f.read()
  response: ChatResponse = chat(model='llama3.1:8b', messages=[
    {
      'role': 'user',
      'content': f"""
      
      find all instances of the keywords "lemma" in the following text, then extract the content of all of the lemmas being stated in json format like below
      
      {{ "lemma1": "Content1", "lemma2": "Content2", ... }}    
      
      Text \"\"\"{solution_content}\"\"\"
      """,
    },
  ])
  output_lemma[solution_file] = response.json()
print(json.dumps(output_lemma, indent = 2))