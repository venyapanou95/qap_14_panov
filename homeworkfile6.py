#  1. Дан файл целых чисел, содержащий не менее четырех элементов.
#  Вывести первый, второй, предпоследний и последний элементы данного
#  файла. Если чисел меньше 3 выводить ошибку
def read_file(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

def print_specific_elements(numbers):
    if len(numbers) < 4:
        print("Ошибка: В файле должно быть не менее четырех элементов.")
    else:
        print("Первый элемент:", numbers[0])
        print("Второй элемент:", numbers[1])
        print("Предпоследний элемент:", numbers[-2])
        print("Последний элемент:", numbers[-1])

if __name__ == "__main__":
    filename = "имяфайла.txt"
    numbers = read_file(filename)
    print_specific_elements(numbers)
#  2. Дан файл целых чисел. Создать два новых файла, первый из которых
#  содержит четные числа из исходного файла, а второй — нечетные (в том
#  же порядке). Если четные или нечетные числа в исходном файле
#  отсутствуют, то соответствующий результирующий файл оставить пустым.
def read_file(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

def write_to_file(filename, numbers):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(str(number) + '\n')

def separate_even_odd_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return even_numbers, odd_numbers

if __name__ == "__main__":
    filename = "имяфайла2.txt"
    numbers = read_file(filename)
    even_numbers, odd_numbers = separate_even_odd_numbers(numbers)

    if even_numbers:
        write_to_file("четные_числа.txt", even_numbers)
    else:
        print("В исходном файле отсутствуют четные числа. Созданный файл с четными числами будет пустым.")

    if odd_numbers:
        write_to_file("нечетные_числа.txt", odd_numbers)
    else:
        print("В исходном файле отсутствуют нечетные числа. Созданный файл с нечетными числами будет пустым.")
#  Дан файл вещественных чисел. Заменить в нем все элементы на их квадраты.
def read_file(filename):
    with open(filename, 'r') as file:
        numbers = [float(line.strip()) for line in file]
    return numbers

def write_to_file(filename, numbers):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(str(number**2) + '\n')

if __name__ == "__main__":
    filename = "имяфайла3.txt"
    numbers = read_file(filename)
    squared_numbers = [num**2 for num in numbers]
    write_to_file(filename, squared_numbers)
#  4. Даны два файла произвольного типа. Поменять местами их содержимое. Файлы должны быть бинарного типа

def swap_binary_files(file1, file2):
    with open(file1, 'rb') as f1:
        data1 = f1.read()

    with open(file2, 'rb') as f2:
        data2 = f2.read()

    with open(file1, 'wb') as f1:
        f1.write(data2)

    with open(file2, 'wb') as f2:
        f2.write(data1)

if __name__ == "__main__":
    file1 = "file1.bin"  # Замените "file1.bin" на имя первого бинарного файла
    file2 = "file2.bin"  # Замените "file2.bin" на имя второго бинарного файла

    swap_binary_files(file1, file2)
