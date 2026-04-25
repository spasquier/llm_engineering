# --- Imports ---
import os
import openai
from dotenv import load_dotenv

# Initialize environment
load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')
if api_key and api_key.startswith('sk-proj-') and len(api_key)>10:
    print("API key looks good so far")
else:
    print("There might be a problem with your API key? Please visit the troubleshooting notebook!")

# --- Configuration ---
client = openai.OpenAI()
MODEL = "gpt-4.1-nano"

# --- Agent Definitions ---
def call_agent(role, system_prompt, user_prompt):
    """Generic wrapper for OpenAI completions."""
    print(f"Calling {role} Agent...")
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2
    )
    return response.choices[0].message.content

class RailsAgents:
    @staticmethod
    def planning_agent(user_request):
        system = (
            "You are a Project Planner. Break down the user's Ruby on Rails request into "
            "specific tasks for a Backend Engineer (API/Models), a Frontend Engineer (UI/Views), "
            "and a QA Tester (RSpec). Output the plan clearly."
        )
        return call_agent("Planner", system, user_request)

    @staticmethod
    def backend_agent(plan):
        system = (
            "You are a Backend Engineer. Generate the Ruby on Rails models, controllers, and "
            "routes for the REST API. Return only the code and the file paths in a structured way."
        )
        return call_agent("Backend", system, f"Follow this plan: {plan}")

    @staticmethod
    def frontend_agent(plan):
        system = (
            "You are a Frontend Engineer. Generate the Rails Views (ERB), Stimulus controllers, "
            "or CSS. Return only the code and the file paths in a structured way."
        )
        return call_agent("Frontend", system, f"Follow this plan: {plan}")

    @staticmethod
    def qa_agent(plan):
        system = (
            "You are a QA Tester. Generate RSpec tests for the features described in the plan. "
            "Return only the code and the file pathsin a structured way."
        )
        return call_agent("QA", system, f"Follow this plan: {plan}")
