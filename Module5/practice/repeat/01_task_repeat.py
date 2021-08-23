# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

import random


def gen_list(size, of, to):
    digit_list = []
    for _ in range(size):
        random_numb = random.randint(of, to)
        digit_list.append(random_numb)
    return (digit_list)


print(gen_list(5, 1, 10))

