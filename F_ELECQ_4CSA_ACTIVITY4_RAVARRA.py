# This is an implementation of Dictionary functions of python
# in creating a Grades list for students

# Main Directory of Dictionary
MainDictionary = {1: ['Santos', '2016098760', 100, 100, 100, 100, 100, 100, 100, 100],
                  2: ['Rodriguez', '2016098761', 100, 100, 100, 100, 100, 100, 100, 100],
                  3: ['Marzan', '2016098762', 100, 100, 100, 100, 100, 100, 100, 100],
                  4: ['Gonzales', '2016098763', 100, 100, 100, 100, 100, 100, 100, 100],
                  5: ['Garcia', '2016098764', 100, 100, 100, 100, 100, 100, 100, 100],
                  6: ['Politzka', '2016098765', 100, 100, 100, 100, 100, 100, 100, 100],
                  7: ['Zedd', '2016098766', 100, 100, 100, 100, 100, 100, 100, 100]
                  }

# List of Subjects
listSubs = ['MATH', 'ENGLISH', 'PHYSICS I', 'PSYCH 1', 'VALED', 'DISCRETE STRUCTURES', 'PROGRAMMING 1', 'INTRODUCTION TO COMPUTERS']
# Main Function
def main():
    while(True):
        print('--------------------------------------------------------------------------< TABLE OF GRADES FOR STUDENT >--------------------------------------------------------------------------')
        print("""What would you want to check?: 
                [1] View Grades
                [2] Add (Student, Grade)
                [3] Update (Student, Grade)
                [4] Delete a Record
                [5] Search (By Student, By Grade)
                [6] Exit
        """)
        ch = int(input('Pick your choice: '))

        if(ch == 1):
            printTable()
        elif(ch == 2):
            addRecord()
            printTable()
        elif(ch==3):
            updRecord()
            printTable()
        elif(ch==4):
            delitem = int(input("Enter the record number you want to delete: "))
            del MainDictionary[delitem]
        elif(ch==5):
            searchRec()
        elif(ch==6):
            print('Thanks for using the Grades Table!!!!!')
            break

    # printTable()
# Print Table Function
def printTable():
    print(" {:7s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}".format
          ('NO.','STUDENT NAME:','STUDENT ID:','MATH:','ENGLISH:','PHYSICS I:','PSYCH 1:','VALED:','DISC. STRUCT.:','PROG 1:','INTRO. COMP.:','SEM GRADE:'))
    # print('No.\t Student Name\t ID\t Math\t English\t Physics I\t Psych 1\t VALED\t Disc. Struct.\t Prog. 1\t Intro. Comp.\t SEM GRADE')
    for x in MainDictionary:
        print(" {:7s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}".format
              (str(x), str(MainDictionary[x][0]), str(MainDictionary[x][1]), str(MainDictionary[x][2]), str(MainDictionary[x][3]), str(MainDictionary[x][4])
               , str(MainDictionary[x][5]), str(MainDictionary[x][6]), str(MainDictionary[x][7]), str(MainDictionary[x][8]), str(MainDictionary[x][9])
               , str(compSemAve(x))))
# Print special
def printSpecialTable(subcode):
    print(" {:7s}\t{:15s}\t{:15s}\t{:15s}".format
          ('NO.','STUDENT NAME:','STUDENT ID:',listSubs[subcode-1]))
    for x in MainDictionary:
        print(" {:7s}\t{:15s}\t{:15s}\t{:15s}".format
              (str(x), str(MainDictionary[x][0]), str(MainDictionary[x][1]), str(MainDictionary[x][subcode+1])))
# Function to compute the Semestral Average
def compSemAve(Mdict):
    semAve = (MainDictionary[Mdict][2] + MainDictionary[Mdict][3] + MainDictionary[Mdict][4] + MainDictionary[Mdict][5] + MainDictionary[Mdict][6] +
    MainDictionary[Mdict][7] + MainDictionary[Mdict][8] + MainDictionary[Mdict][9])/8
    return semAve
# Function for Adding Records
def addRecord():
    name = input('Input Student name: ')
    stdNum = input('Student ID: ')
    mth = int(input('Grade in MATH: '))
    eng = int(input('Grade in ENGLISH: '))
    phys = int(input('Grade in PHYSICS I: '))
    psy = int(input('Grade in PSYCH 1: '))
    valed = int(input('Grade in VALED: '))
    dS = int(input('Grade in DISCRETE STRUCTURES: '))
    prg = int(input('Grade in PROGRAMMING 1: '))
    comp = int(input('Grade in INTRODUCTION TO COMPUTERS: '))
    MainDictionary[len(MainDictionary)+1] = [name, stdNum, mth, eng, phys, psy, valed, dS, prg, comp]
# Function for Updating Records
def updRecord():
    print('''Which one would you want to update?
            [1] Update Name
            [2] Update a Grade''')
    upCH = int(input('Enter your choice: '))
    if(upCH == 1):
        stdId = input('Enter Student ID: ')
        upname = input('Enter Updated name: ')
        key = 0
        for element in MainDictionary.keys():
            if MainDictionary[element][1] == stdId:
                key = element
        print(key)
        MainDictionary.update({key:[str(upname), MainDictionary[key][1], MainDictionary[key][2], MainDictionary[key][3], MainDictionary[key][4]
                                                  , MainDictionary[key][5], MainDictionary[key][6], MainDictionary[key][7], MainDictionary[key][8]
                                                  , MainDictionary[key][9]]})
    elif(upCH == 2):
        stdId = input('Enter Student ID: ')
        for element in MainDictionary.keys():
            if MainDictionary[element][1] == stdId:
                key = element
        print('''Which Subject Grade would you want to update?:
                [1] MATH
                [2] ENGLISH
                [3] PHYSICS i
                [4] PSYCH 1
                [5] VALED
                [6] DISCRETE STRUCTURES
                [7] PROGRAMMING 1
                [8] INTRODUCTION TO COMPUTERS''')
        upSub = int(input('Enter your subject of choice: '))
        upSubRec(key, upSub)
# Sub-function for updating subject Records
def upSubRec(keypass, subcode):
    upGrade = int(input('Enter new grade in {} for {}: '.format(listSubs[subcode-1], MainDictionary[keypass][0])))
    if (subcode == 1):
        MainDictionary.update(
            {keypass: [MainDictionary[keypass][0], MainDictionary[keypass][1], upGrade,
                       MainDictionary[keypass][3], MainDictionary[keypass][4], MainDictionary[keypass][5],
                       MainDictionary[keypass][6], MainDictionary[keypass][7], MainDictionary[keypass][8],
                       MainDictionary[keypass][9]]})
    if (subcode == 2):
        MainDictionary.update(
            {keypass: [MainDictionary[keypass][0], MainDictionary[keypass][1], MainDictionary[keypass][2],
                       upGrade, MainDictionary[keypass][4], MainDictionary[keypass][5],
                       MainDictionary[keypass][6], MainDictionary[keypass][7], MainDictionary[keypass][8],
                       MainDictionary[keypass][9]]})
    if (subcode == 3):
        MainDictionary.update(
            {keypass: [MainDictionary[keypass][0], MainDictionary[keypass][1], MainDictionary[keypass][2],
                       MainDictionary[keypass][3], upGrade, MainDictionary[keypass][5],
                       MainDictionary[keypass][6], MainDictionary[keypass][7], MainDictionary[keypass][8],
                       MainDictionary[keypass][9]]})
    if (subcode == 4):
        MainDictionary.update(
            {keypass: [MainDictionary[keypass][0], MainDictionary[keypass][1], MainDictionary[keypass][2],
                       MainDictionary[keypass][3], MainDictionary[keypass][4], upGrade,
                       MainDictionary[keypass][6], MainDictionary[keypass][7], MainDictionary[keypass][8],
                       MainDictionary[keypass][9]]})
    if (subcode == 5):
        MainDictionary.update(
            {keypass: [MainDictionary[keypass][0], MainDictionary[keypass][1], MainDictionary[keypass][2],
                       MainDictionary[keypass][3], MainDictionary[keypass][4], MainDictionary[keypass][5],
                       upGrade, MainDictionary[keypass][7], MainDictionary[keypass][8],
                       MainDictionary[keypass][9]]})
    if (subcode == 6):
        MainDictionary.update(
            {keypass: [MainDictionary[keypass][0], MainDictionary[keypass][1], MainDictionary[keypass][2],
                       MainDictionary[keypass][3], MainDictionary[keypass][4], MainDictionary[keypass][5],
                       MainDictionary[keypass][6], upGrade, MainDictionary[keypass][8],
                       MainDictionary[keypass][9]]})
    if (subcode == 7):
        MainDictionary.update(
            {keypass: [MainDictionary[keypass][0], MainDictionary[keypass][1], MainDictionary[keypass][2],
                       MainDictionary[keypass][3], MainDictionary[keypass][4], MainDictionary[keypass][5],
                       MainDictionary[keypass][6], MainDictionary[keypass][7], upGrade,
                       MainDictionary[keypass][9]]})
    if (subcode == 8):
        MainDictionary.update(
            {keypass: [MainDictionary[keypass][0], MainDictionary[keypass][1], MainDictionary[keypass][2],
                       MainDictionary[keypass][3], MainDictionary[keypass][4], MainDictionary[keypass][5],
                       MainDictionary[keypass][6], MainDictionary[keypass][7], MainDictionary[keypass][8],
                       upGrade]})

def searchRec():
    print('''What do you want to search?
            [1] Student's Grade/s (All grades of a Student OR Corresponding grade of a student in a subject)
            [2] Grades in a Particular Subject (Prints all the grades in a particular subject)
            ''')
    srch = int(input('Pick your choice: '))
    if(srch==1):
        srId = input('Enter Student ID: ')
        print('''Which Category?
                [3] All Grades
                [4] Particular Grade
                    ''')
        srkey=0
        ctgrch = int(input('Enter your choice: '))
        for element in MainDictionary.keys():
            if MainDictionary[element][1] == srId:
                srkey = element
        print(srkey)
        if(ctgrch==3):
            print(" {:7s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}".format
                ('NO.', 'STUDENT NAME:', 'STUDENT ID:', 'MATH:', 'ENGLISH:', 'PHYSICS I:', 'PSYCH 1:', 'VALED:',
                 'DISC. STRUCT.:', 'PROG 1:', 'INTRO. COMP.:', 'SEM GRADE:'))
            print(" {:7s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}\t{:15s}".format
                (str(srkey), str(MainDictionary[srkey][0]), str(MainDictionary[srkey][1]), str(MainDictionary[srkey][2]),
                 str(MainDictionary[srkey][3]), str(MainDictionary[srkey][4])
                 , str(MainDictionary[srkey][5]), str(MainDictionary[srkey][6]), str(MainDictionary[srkey][7]),
                 str(MainDictionary[srkey][8]), str(MainDictionary[srkey][9])
                 , str(compSemAve(srkey))))
        elif(ctgrch==4):
            print('''Which Subject Grade would you want to search?:
                            [1] MATH
                            [2] ENGLISH
                            [3] PHYSICS i
                            [4] PSYCH 1
                            [5] VALED
                            [6] DISCRETE STRUCTURES
                            [7] PROGRAMMING 1
                            [8] INTRODUCTION TO COMPUTERS''')
            srSub = int(input('Enter your subject of choice: '))
            subgrade = 0
            if(srSub==1):
                subgrade = MainDictionary[srkey][2]
            elif (srSub == 2):
                subgrade = MainDictionary[srkey][3]
            elif (srSub == 3):
                subgrade = MainDictionary[srkey][4]
            elif (srSub == 4):
                subgrade = MainDictionary[srkey][5]
            elif (srSub == 5):
                subgrade = MainDictionary[srkey][6]
            elif (srSub == 6):
                subgrade = MainDictionary[srkey][7]
            elif (srSub == 7):
                subgrade = MainDictionary[srkey][8]
            elif (srSub == 8):
                subgrade = MainDictionary[srkey][9]
            print('{}\' grade in {}: {}'.format(MainDictionary[srkey][0], listSubs[srSub-1], subgrade))
    elif(srch==2):
        print('''Which Subject Grades would you want to search?:
                                    [1] MATH
                                    [2] ENGLISH
                                    [3] PHYSICS i
                                    [4] PSYCH 1
                                    [5] VALED
                                    [6] DISCRETE STRUCTURES
                                    [7] PROGRAMMING 1
                                    [8] INTRODUCTION TO COMPUTERS''')
        srSub = int(input('Enter your subject of choice: '))
        printSpecialTable(srSub)
if __name__ == '__main__':
    main()