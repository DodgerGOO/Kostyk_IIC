import math

def calculate(num1, num2, operator):
    try:
        operations = {
            '+': num1 + num2,
            '-': num1 - num2,
            '*': num1 * num2,
            '/': num1 / num2 if num2 != 0 else None,
            '^': num1 ** num2,
            '%': num1 % num2
        }

        if operator == '/' and num2 == 0:
            raise ZeroDivisionError("Ділення на нуль!")

        result = operations.get(operator)

        if result is None:
            raise ValueError("Невідомий оператор.")

        return result
    except ZeroDivisionError as e:
        print(f"Помилка: {e}")
        return None
    except Exception as e:
        print(f"Помилка: {e}")
        return None

def special_operations(num1, operator):
    operations = {
        '√': math.sqrt(num1)
    }

    result = operations.get(operator)

    if result is None:
        raise ValueError("Невідомий оператор.")

    return result
