from Functions.calculations import calculate, special_operations
from Functions.memory_functions import save_to_memory, get_from_memory


class Calculator:
    def __init__(self):
        self.history = []
        self.memory = None

    def perform_calculation(self, num1, num2, operator):
        result = calculate(num1, num2, operator)
        if result is not None:
            self.history.append(f"{num1} {operator} {num2} = {result}")
            save_to_memory(result)
        return result

    def special_operation(self, num1, operator):
        result = special_operations(num1, operator)
        if result is not None:
            self.history.append(f"{operator}{num1} = {result}")
            save_to_memory(result)
        return result

    def get_history(self):
        return self.history
