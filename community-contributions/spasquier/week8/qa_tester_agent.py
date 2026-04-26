import litellm
import os
from dotenv import load_dotenv

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')
MODEL = 'gpt-5-mini'

class QaTesterAgent():
  def run_agent(prompt):
    response = litellm.completion(
      model=MODEL,
      messages=[
          { "role": "system", "content": """
            You are a Ruby on Rails QATesterAgent.
            You receive a requirements document from the System Analyst Agent.
            Generate test cases and QA verification steps for the Rails application.
            Include both automated test ideas and manual test scenarios.""" },
          { "role": "user", "content": prompt }
      ]
    )
    return response
