import unittest
from src.deep_research_prompter import DeepResearchPrompter
from src.user_input import UserInput


class TestDeepResearchPrompter(unittest.TestCase):
    def test_query_deep_research_api(self):
        with open("google_api_key.txt") as f:
            api_key = f.read().strip()
        user_input = UserInput("What are the latest advancements in AI?")
        prompter = DeepResearchPrompter(user_input, api_key)
        response = prompter.query_deep_research_api()
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)
