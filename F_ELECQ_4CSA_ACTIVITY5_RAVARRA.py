import math


def main():
    while True:
        term = 1
        print('--------------Welcome to the Shape Area Calculator:-------------- ')
        print('\tMenu:')
        print("""     
            [1] SQUARE
            [2] RECT
            [3] TRIANGLE
            [4] CIRCLE
            [5] TRAPEZOID
            [6] EXIT
            """)
        ch = int(input('Pick the Function you want to do: '))

        if(ch == 1):
            base = int(input("Input Square Side: "))
            print("Square Area: ", squareArea(base))
        elif (ch == 2):
            length = int(input("Input Rectangle Length: "))
            width = int(input("Input Rectangle Width: "))
            print("Rectangle Area: ", rectArea(length, width))
        elif (ch == 3):
            base = int(input("Input Triangle base: "))
            height = int(input("Input Triangle height: "))
            print("Triangle Area: ", triangleArea(base, height))
        elif (ch == 4):
            rad = int(input("Input Circle Radius: "))
            print("Circle Area: ", circleArea(rad))
        elif (ch == 5):
            tlength = int(input("Input Trapezoid top side length: "))
            blength = int(input("Input Trapezoid bottom side length: "))
            height = int(input("Input Trapezoid height: "))
            print("Trapezoid Area: ", trapezoidArea(tlength, blength, height))
        elif(ch == 6):
            print('Thank you for using area calculator :)')
            break
def squareArea(side):
    return side*side

def rectArea(l, w):
    return l*w

def triangleArea(b, h):
    return b*h*0.5

def circleArea(r):
    return math.pi*r*r

def trapezoidArea(a, b, h):
    return (a+b)*0.5*h

main()
