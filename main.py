import math

ax, ay = input("Please insert side A: ").split()
bx, by = input("Please insert side B: ").split()
cx, cy = input("Please insert side C: ").split()
ab = round(math.sqrt(math.pow(float(bx) - float(ax), 2) + math.pow(float(by) - float(ay), 2)), 3)
ac = round(math.sqrt(math.pow(float(cx) - float(ax), 2) + math.pow(float(cy) - float(ay), 2)), 3)
bc = round(math.sqrt(math.pow(float(cx) - float(bx), 2) + math.pow(float(cy) - float(by), 2)), 3)


def equilateral(a, b, c):
    if a == b == c:
        return "Triangle is equilateral!"
    else:
        return "Triangle is not equilateral!"


def isosceles(a, b, c):
    if a == b or a == c or b == c:
        return "Triangle is isosceles!"
    else:
        return "Triangle is not isosceles!"


def rectangular(a, b, c):
    if c ** 2 - (a ** 2 + b ** 2) <= 0.002:
        return "Triangle is rectangular!"
    else:
        return "Triangle is not rectangular!"


perimetr = round(ab + ac + bc, 2)

def even_numbers(x):
    my_list = []
    for i in range(int(perimetr)+1):
        if i % 2 == 0:
            my_list.append(i)
    return my_list

print(f"\nSide A is: {ab} \nSide B is: {ac} \nSide C is: {bc}\n")
print(equilateral(ab, ac, bc))
print(isosceles(ab, ac, bc))
print(rectangular(ab, ac, bc))
print(f"Rectangles perimetr is: {perimetr}")
print("All even numbers of perimetr:", *even_numbers(perimetr))
