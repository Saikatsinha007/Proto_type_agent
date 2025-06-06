from openai import OpenAI
from utils import log_action
import os


def log_action(agent, action, payload):
    print(f"[{agent}] {action} -> {payload}")

class CatalogAgent:
    def __init__(self, api_key: str, base_url: str, fallback: bool = True):
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.fallback = fallback
        self.labels = ["bug", "feature", "question"]
        self.confidence_threshold = 0.7

     
        self.bug_keywords = ["bug", "error", "fail", "exception", "traceback", "crash"]
        self.feature_keywords = ["feature", "add", "enhance", "improve", "extend", "implement"]
        self.question_keywords = ["how", "why", "what", "can", "should", "help"]

    def classify(self, query: str) -> str:
        label = None
        query = query.strip()

        try:
            
            system_prompt = "You are a smart software query classifier. Classify the query as one of: bug, feature, or question. Return only the label (e.g., 'bug')."
            user_prompt = f"Query: {query}"

            response = self.client.chat.completions.create(
                model="gemini-2.0-flash",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
            )

            label = response.choices[0].message.content.strip().lower()
            if label in self.labels:
                log_action("CatalogAgent", "LLM classification", {"query": query, "label": label})
                return label

        except Exception as e:
            log_action("CatalogAgent", "LLM call failed", {"error": str(e)})

      
        if self.fallback:
            query_lower = query.lower()
            if any(kw in query_lower for kw in self.bug_keywords):
                return "bug"
            elif any(kw in query_lower for kw in self.feature_keywords):
                return "feature"
            elif any(kw in query_lower.split() for kw in self.question_keywords):
                return "question"

        return "unknown"
