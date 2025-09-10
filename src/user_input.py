class UserInput:
    def __init__(self, user_input):
        if not user_input:
            raise ValueError("Input cannot be empty")
        if len(user_input) > 100:
            raise ValueError("Input cannot be more than 100 characters")
        self.user_input = user_input

