import litellm
import os
from dotenv import load_dotenv

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')
MODEL = 'gpt-5-mini'

class SystemAnalystAgent():
  def run_agent(prompt):
    response = litellm.completion(
      model=MODEL,
      messages=[
          { "role": "system", "content": """
            You are a Ruby on Rails SystemAnalystAgent.
            You take the user query and transform it into a Requirements Document.
            The document should include:
            - Backend requirements
            - Frontend requirements
            - QA test plan
            - A final summary of the scope and deliverables.""" },
          { "role": "user", "content": prompt }
      ]
    )
    return response
