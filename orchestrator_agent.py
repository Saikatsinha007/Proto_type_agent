from catalog_agent import CatalogAgent
from developer_agent import DeveloperAgent
from utils import log_action

class OrchestratorAgent:
    def __init__(self, api_key: str, base_url: str):
        self.catalog_agent = CatalogAgent(api_key, base_url)
        self.developer_agent = DeveloperAgent(api_key, base_url)
        # In future, add AnswerAgent or DocumentationAgent

    def handle_query(self, query: str) -> str:
        query_type = self.catalog_agent.classify(query)
        log_action("OrchestratorAgent", "Classified query", {"query": query, "type": query_type})

        if query_type in ["bug", "feature"]:
            return self.developer_agent.handle(query, query_type)
        elif query_type == "question":
            return "ℹ️ AnswerAgent would handle this (not implemented yet)."
        else:
            return "❓ Could not classify query."
