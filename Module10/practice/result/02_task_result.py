# На числовой прямой расположены точки A, B, C и D.
# Напишите программу, которая выведет, во сколько раз отрезок AB больше или меньше, чем отрезок CD.
# Формат входных данных:
# На вход программе подается четыре целых числа A, B, C и D.
# Расположение точек относительно друг друга на координатной прямой произвольное.
# Формат выходных данных:
# Выведите, во сколько раз отрезок AB больше, чем отрезок CD. Ответ введите с точностью до 6-ти знаков после запятой.

a = float(input("Введите координаты точек: \nа:"))
b = float(input("b:"))
c = float(input("c:"))
d = float(input("d:"))
length_ab = abs(b - a)
length_cd = abs(d - c)
if length_ab > length_cd:
    relation_times = length_ab / length_cd
    print(f"Отрезок AB больше CD  в {relation_times:.6f} раз(а)")
elif length_ab < length_cd:
    relation_times = length_cd / length_ab
    print(f"Отрезок AB меньше CD  в {relation_times:.6f} раз(а)")
else: print("Отрезки равны")
