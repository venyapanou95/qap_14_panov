#  1.2 Определить переменные всех типов и выведете их на экран
integer_x = 5
float_x = 5.15
string_x = "Hello World"
boolean_x = True
#  Вывод значений переменных 
print(integer_x)
print(float_x)
print(string_x)
print(boolean_x)
#  1.3 Вычисление и вывод значений всех выражений
print("x =", 17 / 2 * 3 + 2)
print("x =", 2 + 17 / 2 * 3)
print("x =", 19 % 4 + 15 / 2 * 3)
print("x =", (15 + 6) - 10 * 4)
print("x =", 17 / 2 % 2 * 3**3)
#  1.4 Создать три переменные, содержащие возраст трех ближайших соседей, найти сумму и вывести ее на экран.
a1_age = 20
b2_age = 65
b3_age = 30
#  Найти сумму
sum_age = a1_age + b2_age + b3_age
#  Создание среднего 
average_age = sum_age / 3
#  Вывод суммы
print(sum_age)
print(average_age)
#  1. Привести к целому типу -1.6, 2.99
x = int(-1.6)
y = int(2.99)
print(x)
print(y)
#  2. Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
x = "www.my_site.com#about"
updated_x = x.replace("#", "/")
print(updated_x)
#  3. Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’
x = "stroka"
y = "ing"
print(x + y)
#  4. В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
x = "Ivanou Ivan"
word = x.split()
reversed_word = " ".join(reversed(word))
print(reversed_word)
#  5. Напишите программу которая удаляет пробел в начале, в конце строки
x = " Space space "
print(x) 
remove_space = x.strip()
print(remove_space)
#  6. Создайте словарь, связав его с переменной school, и наполните его данными которые бы отражали количество учащихся в десяти разных классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).
school = {"1A":10,"1B":11,"2B":122}
print(school)
#  7. Создайте список и извлеките из него списка второй элемент.
venya_list = [20, 30, 40]
element_2 = venya_list[1]
print(element_2)
#  8. Вывести входит ли строка1 в строку2 (пример: employ и employment )
x1 = "employ"
x2 = "employment"
if x1 in x2:
    print("x1 is included in x2")
else:
    print("x1 is not included in x2")   
#  9. Вывести нужные символы
x = "My name is Agent Smith"
print(x[1]) #y
print(x[3]+x[6]+x[9]+x[12]+x[15]) #nesgt



err = {
    'length': 'Длина пароля равна 8 символам',
    'upper': 'Отсутствуют заглавные буквы',
    'lower': 'Нет строчных букв в пароле',
    'digits': 'Нет цифр в пароле',
    }

password = "Q#wertyyyyy12312313"
err = {
    "digits": "Нет цифр в пароле",
    'length': 'Длина пароля равна 8 символам',
    'upper': 'Отсутствуют заглавные буквы',
    'lower': 'Нет строчных букв в пароле',
}

if any(char.isdigit() for char in password):
    print("Пароль содержит цифры")
else:
    print(err["digits"])

