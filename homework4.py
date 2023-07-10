#  Работа с переменными
#  1. Переменной var_int присвойте значение 10, var_float - значение 8.4, var_str - "No"
var_int = 10
var_float = 8.4
var_str = "No"
#  2. Измените значение, хранимое в переменной var_int, увеличив его в 3.5 раза, результат свяжите с переменной big_int
big_int = var_int * 3.5
#  3. Измените значение, хранимое в переменной var_float, уменьшив его на единицу,результат свяжите с той же переменной
var_float -= 1
#  4. Разделите var_int на var_float, а затем big_int на var_float. Результат данных выражений не привязывайте ни к каким переменным
var_int / var_float
big_int / var_float
#  5. Измените значение переменной var_str на "NoNoYesYesYes". При формировании нового значения используйте операции конкатенации (+) и повторения строки (*)
var_str += "NoYesYesYes"
#  6. Выведите значения всех переменных
print("var_int =", var_int)
print("var_float =", var_float)
print("var_str =", var_str)
print("big_int =", big_int)

#  Строки
#  1. Свяжите переменную с любой строкой, состоящей не менее чем из 8 символов.
#  Извлеките из строки первый символ, затем последний, третий с начала и третий с
#  конца. Измерьте длину вашей строки.
x_string = "qwertyui"
first_character = x_string[0]
last_character = x_string[-1]
third_char_from_start = x_string[2]
third_char_from_end = x_string[-3]
x_string_length = len(x_string)
print(first_character)
print(last_character)
print(third_char_from_start)
print(third_char_from_end)
print(x_string_length)
#  2. Присвойте произвольную строку длиной 10-15 символов переменной и извлеките из нее следующие срезы

#  3. Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name” вставьте ваше имя.
string = "my name is name"
new_string_with_replace = string.replace("name", "python", 1)
print(new_string_with_replace)
#  4. Есть строка: test_tring = "Hello world!", необходимо
test_string = "Hello world!"
#  напечатать на каком месте находится буква w
index_of_w = test_string.index('w')
print("Индекс буквы 'w':", index_of_w)
#  кол-во букв l
count_of_one = test_string.count('l')
print("Количество букв 'l':", count_of_one)
#  проверить начинается ли строка с подстроки: “Hello”
starts_with_hello = test_string.startswith("Hello")
print("Начинается ли строка с 'Hello':", starts_with_hello)
#  проверить заканчивается ли строка подстрокой: “qwe”
ends_with_qwe = test_string.endswith("qwe")
print("Заканчивается ли строка на 'qwe':", ends_with_qwe)
#  Lists
#  1. Создайте два любых списка и свяжите их с переменными.
list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d", "e"]
#  2. Извлеките из первого списка второй элемент.
second_element = list1[1]
print(second_element)
#  3. Измените во втором списке последний элемент. Выведите список на экран.
list2[-1] = "z"
print(list2)
#  4. Соедините оба списка в один, присвоив результат новой переменной. Выведите получившийся список на экран. 
link_lists = list1 + list2
print(link_lists)
#  5. Снимите" срез из соединенного списка так, чтобы туда попали некоторые части
sliced_list = link_lists[2:7]
print(sliced_list)
#  6. Добавьте в список два новых элемента и снова выведите его
link_lists.append("newlist1")
link_lists.append("newlist2")
print(link_lists)  # Выводит: [1, 2, 3, 4, 5, "a", "b", "c", "d", "z", "new1", "new2"]
#  7. Даны списки: 
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
#  Нужно вернуть список, который состоит из элементов, общих для этих двух
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
link_elements = list(set(a) & set(b))
print(link_elements)
#  8. Есть список: [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3] оставить в нем только уникальные
list_original = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
unique_values = list(set(list_original))
print(unique_values)
#  Логические операции:
#  1. Присвойте двум переменным любые числовые значения.
x = 5
y = 10
#  2. Составьте четыре сложных логических выражения с помощью оператора and, два из
#  которых должны давать истину, а два других - ложь.
expression1 = (x > 0) and (y < 20)
expression2 = (x > 0) and (y > 20)
expression3 = (x < 0) and (y < 20)
expression4 = (x < 0) and (y > 20)
#  3. Аналогично выполните п. 2, но уже используя оператор or.
expression5 = (x > 0) or (y < 20)
expression6 = (x > 0) or (y > 20)
expression7 = (x < 0) or (y < 20)
expression8 = (x < 0) or (y > 20)
#  4. Попробуйте использовать в сложных логических выражениях работу с переменными
#  строкового типа.
name1 = "Alice"
name2 = "Bob"
expression9 = (name1 == "Alice") and (name2 == "Bob")
expression10 = (name1 == "Alice") and (name2 == "Gys")
expression11 = (name1 != "Alice") or (name2 == "Bob")
expression12 = (name1 != "Alice") or (name2 != "Gys")
#  Словари:
#  1. Создайте словарь, связав его с переменной school, и наполните его данными,
#  которые бы отражали количество учащихся в десяти разных классах (например, 1а, 1б,
#  2б, 6а, 7в и т.д.).
school = {
    "1а": 25,
    "1б": 28,
    "2б": 30,
    "6а": 24,
    "7в": 27,
    "8б": 26,
    "9а": 29,
    "10б": 31,
    "11а": 23,
    "11б": 22
}
#  2. Узнайте сколько человек в каком-нибудь классе.
print(school["1а"])
#  3. Представьте, что в школе произошли изменения, внесите их в словарь:
#  ◦ в трех классах изменилось количество учащихся;
school["1a"]=30
school["2б"]=32
school["6a"]=30
#  ◦ в школе появилось два новых класса;
school["9б"] = 27
school["10а"] = 26
#  ◦ в школе расформировали один из классов.
del school["11б"]
#  4. Выведите содержимое словаря на экран.
print(school)
#  Преобразование типов
#  1.
#  Перевести строку в массив
#  "Robin Singh" => ["Robin”, “Singh"]
#  "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]
string1 = "Robin Singh"
print(string1.split())
string2 = "I love arrays they are my favorite"
new_string = string2.split()
print(new_string)
#  2.
#  Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
#  Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
names = ['Ivan', 'Ivanou']
city = 'Minsk'
country = 'Belarus'
text = f"Привет, {names[0]} {names[1]}! Добро пожаловать в {city} {country}"
print(text)
#  3.
#  Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него
#  строку => "I love arrays they are my favorite"
my_list = ["I", "love", "arrays", "they", "are", "my", "favorite"]
result_string = " ".join(my_list)
print(result_string)
#  4.
#  Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
#  удалите элемент из списка под индексом 6
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_value = "new"
my_list.insert(2, new_value)
del my_list[6]
print(my_list)
#  5.
#  Есть 2 словаря
#  a = { 'a': 1, 'b': 2, 'c': 3}
#  b = { 'c': 3, 'd': 4,'e': 5}
a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}
ab = {}
for key in set(a.keys()) | set(b.keys()):
    ab[key] = [a.get(key), b.get(key)]
print(ab)
#  Условия
#  1. Дано целое число. Если оно является положительным, то прибавить к нему 1; в
#  противном случае не изменять его. Вывести полученное число.
number = int(input("Введите целое число: "))

if number > 0:
    number += 1

print("Результат:", number)

#  2. Даны три целых числа. Найти количество положительных чисел в исходном наборе.
a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
c = int(input("Введите третье целое число: "))

count = 0

if a > 0:
    count += 1

if b > 0:
    count += 1

if c > 0:
    count += 1

print("Количество положительных чисел:", count)
#  3. Дан номер года (положительное целое число). Определить количество дней в
#  этом году, учитывая, что обычный год насчитывает 365 дней, а високосный — 366
#  дней. Високосным считается год, делящийся на 4, за исключением тех годов, которые
#  делятся на 100 и не делятся на 400 (например, годы 300, 1300 и 1900 не являются
#  високосными, а 1200 и 2000 являются).
year = int(input("Введите номер года: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    days = 366
else:
    days = 365

print("Количество дней в году:", days)
#  4. Дано целое число в диапазоне 1–7. Вывести строку — название дня недели,
#  соответствующее данному числу (1 — «понедельник», 2 — «втор- ник» и т. д.).
day_number = int(input("Введите число от 1 до 7: "))
if day_number == 1:
    day_name = "понедельник"
elif day_number == 2:
    day_name = "вторник"
elif day_number == 3:
    day_name = "среда"
elif day_number == 4:
    day_name = "четверг"
elif day_number == 5:
    day_name = "пятница"
elif day_number == 6:
    day_name = "суббота"
elif day_number == 7:
    day_name = "воскресенье"
else:
    day_name = "некорректное число"

print("Название дня недели:", day_name)
#  5. Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 —
#  миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер. Дан номер едини- цы массы (целое
#  число в диапазоне 1–5) и масса тела в этих единицах (вещественное число). Найти
#  массу тела в килограммах.unit_number = int(input("Введите номер единицы массы (1-5): "))
unit_number = int(input("Введите номер единицы массы (1-5): "))
weight = float(input("Введите массу тела: "))
if unit_number == 1:
    weight_kg = weight
elif unit_number == 2:
    weight_kg = weight / 1000000
elif unit_number == 3:
    weight_kg = weight / 1000
elif unit_number == 4:
    weight_kg = weight * 1000
elif unit_number == 5:
    weight_kg = weight * 100
print("Масса тела в килограммах:", weight_kg)
#  Цикл while
#  1.Дано число N. Найти произведение всех чисел от 0 до N.
def find_product(N):
    product = 1
    i = 1
    while i <= N:
        product *= i
        i += 1
    return product
N = 5  # Заданное число
result = find_product(N)
print("Произведение чисел от 0 до", N, ":", result)
#  2.Поле засеяли цветами двух сортов на площади S1 и S2. Каждый год
#  площадь цветов первого сорта увеличивается вдвое, а площадь второго сорта
#  увеличивается втрое. Через сколько лет площадь первых сортов будет
#  составлять меньше 10% от площади вторых сортов.
def find_years(S1, S2):
    years = 0
    while S1 >= S2 * 0.1:
        S1 *= 2
        S2 *= 3
        years += 1
    return years
S1 = 1  # Площадь цветов первого сорта (начальное значение)
S2 = 1  # Площадь цветов второго сорта (начальное значение)
result = find_years(S1, S2)
print("Количество лет:", result)
#  3.Дано целое число N (>0). Используя операции деления нацело и взятия
#  остатка от деления, найти количество и сумму его цифр.
def count_digits_sum(N):
    count = 0
    digit_sum = 0
    while N > 0:
        digit = N % 10
        count += 1
        digit_sum += digit
        N //= 10
    return count, digit_sum
N = 12345  # Заданное целое число
count, digit_sum = count_digits_sum(N)
print("Количество цифр:", count)
print("Сумма цифр:", digit_sum)
#  4. Деду M лет, а внуку N лет. Через сколько лет дед станет вдвое старше
#  внука. И сколько при этом лет будет деду и внуку
def check_years(M, N):
    years = 0
    while M < 2 * N:
        M += 1
        N += 1
        years += 1
    return years, M, N
M = 50  # Возраст дедушки
N = 25  # Возраст внука
years, M, N = check_years(M, N)
print("Количество лет:", years)
print("Возраст дедушки:", M)
print("Возраст внука:", N)