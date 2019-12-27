import time
import sys
class Timer:
    def __init__(self, hours, mins, secs):
        self.hours = hours
        self.mins = mins
        self.secs = secs

    def CountDown(self):
        flag = True
        hr =  self.hours
        min = self.mins
        sec = self.secs
        while(flag!=False):
            while(hr>-1):
                while(min>-1):
                    while(sec>-1):
                        str = "{:02d}:{:02d}:{:02d}".format(hr, min, sec)
                        sys.stdout.write('\r'+str)
                        time.sleep(1)
                        sec -= 1
                        if(hr,min,sec==0):
                            str = "TIME\'s UP!!"
                            sys.stdout.write('\r' + str)
                            flag = False
                    min -=1
                    sec = 59
                hr -=1
                min = 59

    def CountUp(self):

        flag = True
        hr = 0
        min = 0
        sec = 0
        while (flag != False):
            while (hr > -1):
                while (min < 60):
                    while (sec < 60):
                        str = "{:02d}:{:02d}:{:02d}".format(hr, min, sec)
                        sys.stdout.write('\r' + str)
                        time.sleep(1)
                        if (hr == self.hours and min == self.mins and sec == self.secs):
                            str = "TIME\'s UP!!"
                            sys.stdout.write('\r' + str)
                            break
                        sec += 1
                    if (hr == self.hours and min == self.mins and sec == self.secs):
                        break
                    min += 1
                    sec = 0
                if (hr == self.hours and min == self.mins and sec == self.secs):
                    flag = False
                    break
                hr += 1
                min = 0

def main():
    print('Welcome to a STOPWATCH TIMER!!!')
    print('''Choices:
            [1] CountDown
            [2] Stopwatch
            ''')
    ch = int(input("Choose what kind of timer: "))

    if(ch==1):
        oras = int(input("Input the number of hours: "))
        minuto = int(input("Input the number of minutes[0-59]: "))
        segundo = int(input("Input the number of hours[0-59]: "))
        str = "Initializing Clock."
        print()
        for i in range(1,6):
            sys.stdout.write('\r'+str)
            time.sleep(1)
            str = str + '.'

        print("\nSTART!!!!")
        print("\nHH:MM:SS")
        STP = Timer(oras,minuto,segundo)
        STP.CountDown()

        # print('\nTime\'s UP!!')
    elif(ch==2):
        oras = int(input("Input the number of hours: "))
        minuto = int(input("Input the number of minutes[0-59]: "))
        segundo = int(input("Input the number of hours[0-59]: "))
        str = "Initializing Clock."
        print()
        for i in range(1, 6):
            sys.stdout.write('\r' + str)
            time.sleep(1)
            str = str + '.'

        strt = input("\nStart? y/n: ")
        if(strt.lower() == 'y'):
            STP = Timer(oras, minuto, segundo)
            STP.CountUp()
        elif(strt.lower()== 'n'):
            print('Hello')


        # print('\nTime\'s UP!!')


main()