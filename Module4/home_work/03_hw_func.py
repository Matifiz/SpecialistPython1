# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
  
def circle_inside(o1 ,o2, r1, r2):
    delta = distance(*o1,*o2)
    return r1 >= r2+delta

print(circle_inside((0,1),(0,0),2,1))
