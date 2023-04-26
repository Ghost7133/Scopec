import math
def firstGroupTest(a,b,c):
        if(a>0 and b>0 and c>0) and (a !=0 and b  != 0 and c != 0):
            if a+b>c and a+c>b and b+a>c and b+c>a and c+a>b and c+b>a:   
                if a == b == c:
                    return("Треугольник является равносторонним")
                elif a == b or b == c or a == c:
                    return("Треугольник является равнобедренным")
                else:
                    return("Треугольник является разносторонним")
            else:
                return("Сумма двух из чисел больше третьего")
        else:
            return("Одно из чисел <= 0")

    
def secondGroupTest(a,b,c):
    if (a <= 0 or b <= 0 or c <= 0) or (a + b <= c or c + b <= a or a + c <= b):
        return("Введенные данные не могут являться сторонами треугольника")
    p = (a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    if a == b == c:
            return("Треугольник равносторонний, площадь: %.2f" % S)
    elif a == b or a == c or b == c:
        return("Треугольник равнобедренный, площадь: %.2f" % S)
    elif a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
        return("Треугольник прямоугольный, площадь: %.2f" % S)
    else:
        return("Треугольник остроугольный, площадь: %.2f" % S)