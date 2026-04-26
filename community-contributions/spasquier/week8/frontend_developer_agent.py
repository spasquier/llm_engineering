import litellm
import os
from dotenv import load_dotenv

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')
MODEL = 'gpt-5-mini'

class FrontendDeveloperAgent():
  def run_agent(prompt):
    response = litellm.completion(
      model=MODEL,
      messages=[
          { "role": "system", "content": """
            You are a Ruby on Rails FrontendDeveloperAgent.
            You receive a requirements document from the System Analyst Agent.
            Generate Rails frontend code, including views, layouts, and assets, that satisfy the requirements.
            Keep the output focused on frontend implementation details only.""" },
          { "role": "user", "content": prompt }
      ]
    )
    return response
