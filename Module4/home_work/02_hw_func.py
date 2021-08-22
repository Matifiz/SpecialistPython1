# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def min_length (a, b, c):
    length = [distance(*a, *b), distance(*b, *c), distance(*a, *c)]
    name = ['AB', 'BC', 'AC']
    segments = {}
    for names, val in zip(name, length):
        segments[names] = val
    min_segm = segments['AB']
    for names, val in segments.items():
          if segments[names] <= min_segm:
             min_segm = segments[names]
             min_name = names
    return print(f"Самый короткий отрезок: {min_name} = {min_segm:.2f}")


print(min_length((0,0),(2,2),(2,-2)))

# TODO: your code here
#print("Самый короткий отрезок:", ...)  # Выводим название отрезка, например “АС”.
