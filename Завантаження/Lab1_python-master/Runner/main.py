from Functions.calculations import calculate, special_operations
from Functions.memory_functions import get_from_memory, save_to_memory
from Settings.AppSettings import DECIMALS
import init


def main():
    while True:
        num1 = input("Введіть перше число (або 'm' для використання пам'яті): ")
        if num1.lower() == 'm' and get_from_memory() is not None:
            num1 = get_from_memory()
            print(f"Використано з пам'яті: {num1}")
        else:
            num1 = float(num1)

        operator = input("Введіть оператор (+, -, *, /, ^, %, √): ")
        if operator not in ['+', '-', '*', '/', '^', '%', '√']:
            print("Невірний оператор. Спробуйте ще раз.")
            continue

        if operator == '√':
            result = special_operations(num1, operator)
        else:
            num2 = input("Введіть друге число (або 'm' для використання пам'яті): ")
            if num2.lower() == 'm' and get_from_memory() is not None:
                num2 = get_from_memory()
                print(f"Використано з пам'яті: {num2}")
            else:
                num2 = float(num2)

            result = calculate(num1, num2, operator)

        if result is not None:
            print(f"Результат: {round(result, DECIMALS)}")
            save_to_memory(result)
            init.history.append(f"{num1} {operator} {num2 if operator != '√' else ''} = {result}")

        repeat = input("Бажаєте виконати ще одне обчислення? (так/ні): ").lower()
        if repeat != 'так':
            break

if __name__ == "__main__":
    main()
