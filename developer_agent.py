from openai import OpenAI
from utils import log_action

def log_action(agent, action, payload):
    print(f"[{agent}] {action} -> {payload}")

class DeveloperAgent:
    def __init__(self, api_key: str, base_url: str):
        self.client = OpenAI(api_key=api_key, base_url=base_url)

    def handle(self, query: str, query_type: str) -> str:
        log_action("DeveloperAgent", "Received", {"type": query_type, "query": query})

        if query_type not in ["bug", "feature"]:
            return "❌ Unsupported query type."

        # Prompt LLM for simulated fix or feature
        prompt = f"""
You are a senior software developer. A user reported this {query_type}:

\"\"\"{query}\"\"\"

Write a simulated fix or feature response as if you're submitting a patch summary.
"""

        try:
            response = self.client.chat.completions.create(
                model="gemini-2.0-flash",
                messages=[
                    {"role": "system", "content": "You are a helpful software engineer."},
                    {"role": "user", "content": prompt}
                ]
            )

            fix = response.choices[0].message.content
            log_action("DeveloperAgent", "Generated response", {"summary": fix})
            return fix

        except Exception as e:
            log_action("DeveloperAgent", "LLM Error", {"error": str(e)})
            return "⚠️ Failed to generate fix."
