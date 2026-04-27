import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')
MODEL = 'gpt-5-mini'
openai = OpenAI()

class BackendDeveloperAgent():
  def run_agent(self, prompt):
    response = openai.chat.completions.create(model=MODEL, messages=[
          { "role": "system", "content": """
            You are a Ruby on Rails BackendDeveloperAgent.
            You receive a requirements document from the System Analyst Agent.
            Generate Rails backend code, including models, controllers, and routes, that satisfy the requirements.
            Keep the output focused on backend implementation details only.""" },
          { "role": "user", "content": prompt }
      ]
    )
    return response.choices[0].message.content
