import math

class TriangleError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return '{} for text'.format(self.text)
        

def triangle_area(a,b,c):
    sides = sorted((a,b,c))
    if sides[2]>sides[0] + sides[1]:
        raise TriangleError("Illegal Triangle")
    p = (a+b+c)/2
    a = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return a

print(triangle_area(3,4,5))

def main():
    try:
        triangle_area(3,4,10)
    except TriangleError as e:
        print(e)
print(main())
