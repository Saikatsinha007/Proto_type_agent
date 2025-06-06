from orchestrator_agent import OrchestratorAgent

API_KEY = "AIzaSyDshoHIAfzoWuPDqX9bvKtuhHotJsdaw2o"
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

agent = OrchestratorAgent(api_key=API_KEY, base_url=BASE_URL)

queries = [
    "The signup page crashes with a traceback error.",
    "Please add dark mode to the dashboard.",
    "How can I reset my password?"
]

for q in queries:
    print(f"📝 Query: {q}")
    response = agent.handle_query(q)
    print(f"✅ Response:\n{response}\n{'-'*60}")
