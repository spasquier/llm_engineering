import litellm
import os
from dotenv import load_dotenv

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')
MODEL = 'gpt-5-mini'

class BackendDeveloperAgent():
  def run_agent(prompt):
    response = litellm.completion(
      model=MODEL,
      messages=[
          { "role": "system", "content": """
            You are a Ruby on Rails BackendDeveloperAgent.
            You receive a requirements document from the System Analyst Agent.
            Generate Rails backend code, including models, controllers, and routes, that satisfy the requirements.
            Keep the output focused on backend implementation details only.""" },
          { "role": "user", "content": prompt }
      ]
    )
    return response
