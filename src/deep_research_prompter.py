import google.generativeai as genai
from src.user_input import UserInput


class DeepResearchPrompter:
    """
    Uses Gemini API to perform deep research based on user input.
    """
    def __init__(self, user_input: UserInput, api_key: str):
        self.user_input = user_input
        genai.configure(api_key=api_key)
        # Using a model that is good for this kind of task.
        # Enabling the search tool for deep research.
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-pro-latest",
            tools=["google_search_retrieval"],
        )

    def query_deep_research_api(self):
        """
        Queries the Gemini API with the user input to perform deep research.
        """
        response = self.model.generate_content(self.user_input())
        return response.text
