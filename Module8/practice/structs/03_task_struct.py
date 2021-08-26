# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов
import random
numbers = []
n = 10
for _ in range (10):
    numbers.append(random.randint(-20, 20))
print(numbers)

larger_ten = [el for el in numbers if el >= 10]
sum_positive = sum([el for el in numbers if el >0])
positive = [el for el in numbers if el >0]
mean_positive = sum(positive) / len(positive)
print(larger_ten)
print(sum_positive)
