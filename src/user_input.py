class UserInput:
    """
    The input of the user. Prompts are capped at 100 characters.
    """
    def __init__(self, user_input):
        if not user_input:
            raise ValueError("Input cannot be empty")
        if len(user_input) > 100:
            raise ValueError("Input cannot be more than 100 characters")
        self.user_input = user_input

    def __call__(self):
        return self.user_input