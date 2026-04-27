import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')
MODEL = 'gpt-5-mini'
openai = OpenAI()

class FrontendDeveloperAgent():
  def run_agent(self, prompt):
    response = openai.chat.completions.create(model=MODEL, messages=[
          { "role": "system", "content": """
            You are a Ruby on Rails FrontendDeveloperAgent.
            You receive a requirements document from the System Analyst Agent.
            Generate Rails frontend code, including views, layouts, and assets, that satisfy the requirements.
            Keep the output focused on frontend implementation details only.""" },
          { "role": "user", "content": prompt }
      ]
    )
    return response.choices[0].message.content
