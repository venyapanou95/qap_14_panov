# 1 Напишите генератор который принимает список
def positive_numbers(numbers):
    return [num for num in numbers if num > 0]

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
positive_nums = positive_numbers(numbers)
print(positive_nums)  # Вывод: [34.6, 44.9, 68.3, 44.6, 12.7]

# 2 Необходимо составить список чисел которые
def word_lengths(sentence):
    words = sentence.split()
    lengths = []
    for word in words:
        if word.lower() != "the":
            lengths.append(len(word))
    return lengths

sentence = "the quick brown fox jumps over the lazy dog"
lengths = word_lengths(sentence)
print(lengths)  # Вывод: [5, 5, 3, 5, 4, 4, 3]

