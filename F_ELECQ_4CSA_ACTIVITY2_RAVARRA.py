
def main():
    global answ
    answ = 0
    num1 = int(input('Input First Number: '))
    num2 = int(input('Input Second Number: '))
    key = int(input("""
    ----Choose Operator:----
        1: Addition
        2: Subtraction
        3: Multiplication
        4: Division
        5: Power
        6: Modulo
    """))
    try:
        if(key == 1):
            answ = num1  + num2
        elif(key == 2):
            answ =  num1 - num2
        elif(key == 3):
            answ = num1 * num2
        elif(key == 4):
            answ = num1 / num2
        elif(key == 5):
            answ = num1 ** num2
        elif(key == 6):
            answ = num1 % num2
    except ZeroDivisionError as e:
        print(e)
        
    print('Answer of the Operation: ', answ)
    