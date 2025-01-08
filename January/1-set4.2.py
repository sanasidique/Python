
area_square = lambda side: side ** 2


area_rectangle = lambda length, width: length * width


area_triangle = lambda base, height: 0.5 * base * height


side = 4
length = 5
width = 3
base = 6
height = 4

print("Area of square:", area_square(side))
print("Area of rectangle:", area_rectangle(length, width))
print("Area of triangle:", area_triangle(base, height))
