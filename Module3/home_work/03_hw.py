# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.
import random
numbers = []
n = 4
i = 0
sum = 0
while i <= n-1:
    numbers.append(random.randint(-100, 100))
    if numbers[i] % 2 == 0 and numbers[i]>0:
        sum += numbers[i]
    i += 1
print(numbers)
print("sum = ",sum)
