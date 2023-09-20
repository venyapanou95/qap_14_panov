# 1 Напишите декоратор, который проверял бы тип параметров
# функции, конвертировал их если надо и складывал:
def typed(type):
    def decorator(func):
        def wrapper(*args):
            converted_args = []
            for i, arg in enumerate(args):
                if type == 'int':
                    converted_args.append(int(arg))
                elif type == 'str':
                    converted_args.append(str(arg))
                else:
                    raise ValueError('Unsupported type')

            return func(*converted_args)
        return wrapper
    return decorator

@typed(type='str')
def add_two_symbols(a, b):
    return a + b

@typed(type='int')
def add_three_symbols(a, b, c):
    return a + b + c

# Примеры использования
print(add_two_symbols("3", 5))  # Вывод: "35"
print(add_two_symbols(5, 5))     # Вывод: "55"
print(add_two_symbols('a', 'b'))  # Вывод: "ab"

print(add_three_symbols(5, 6, 7))     # Вывод: 18
print(add_three_symbols("3", 5, 0))    # Вывод: 8
print(add_three_symbols(0.1, 0.2, 0.4)) # Вывод: 0.7000000000000001
