# F_ELECQ_4CSA_ACTIVITY3_RAVARRA
# 4CSA

def MainDir():
    DirectoryMain = []

    list1 = ['Mark', 'Manila', '09999999999']
    list2 = ['Luh', 'Muntinlupa', '09999999998']
    list3 = ['Hans', 'QC', '09999999997']
    list4 = ['Kyle', 'Cavite', '09999999996']
    list5 = ['Jimboi', 'Laguna', '09999999995']

    DirectoryMain.append(list1)
    DirectoryMain.append(list2)
    DirectoryMain.append(list3)
    DirectoryMain.append(list4)
    DirectoryMain.append(list5)

    print('--------------!!!!!TELEPHONE DIRECTORY!!!!!-----------------')
    while True:
        term = 1
        print('--------------Welcome to the Pseudo-Directory:-------------- ')
        print ('\tMenu:')
        print ("""     
            [1] ADD
            [2] REMOVE
            [3] SEARCH
            [4] LIST
            [5] EXIT
            """)
        ch = int(input('Pick the Function you want to do: '))
        if(ch==1):
            tempList = []
            print('\nEnter the details of the new Contact: ')
            name = input("Name: ")
            tempList.append(name)
            addrss = input('Address: ')
            tempList.append(addrss)
            telno = input('Telephone Number: ')
            tempList.append(telno)
            print("\n-----------------PAST DIRECTORY-----------------\n")
            print(" {:15s}\t{:15s}\t{:15s}".format('NAME: ','ADDRESS: ','PHONE NUMBER: '))
            for i in DirectoryMain:
                for j in i:
                    print(" {:15s}\t{:15s}\t{:15s}".format(i[0], i[1], i[2]))
                    break
            print("\n---------------------------------------------------\n")
            DirectoryMain.append(tempList)
            DirectoryMain.sort()
            print("\n-----------------UPDATED DIRECTORY-----------------\n")
            print(" {:15s}\t{:15s}\t{:15s}".format('NAME: ','ADDRESS: ','PHONE NUMBER: '))
            for i in DirectoryMain:
                for j in i:
                    print(" {:15s}\t{:15s}\t{:15s}".format(i[0],i[1],i[2]))
                    break
            print("\n---------------------------------------------------\n")
        elif(ch==2):
            rem = input('Which Contact would you want to remove(Enter the name): ')
            print("\n-----------------PAST DIRECTORY-----------------\n")
            print(" {:15s}\t{:15s}\t{:15s}".format('NAME: ','ADDRESS: ','PHONE NUMBER: '))
            for i in DirectoryMain:
                for j in i:
                    print(" {:15s}\t{:15s}\t{:15s}".format(i[0], i[1], i[2]))
                    break
            print("\n---------------------------------------------------\n")
            DirectoryMain = [x for x in DirectoryMain if ((x[0] != rem))]
            DirectoryMain.sort()
            print("\n-----------------UPDATED DIRECTORY-----------------\n")
            print(" {:15s}\t{:15s}\t{:15s}".format('NAME: ','ADDRESS: ','PHONE NUMBER: '))
            for i in DirectoryMain:
                for j in i:
                    print(" {:15s}\t{:15s}\t{:15s}".format(i[0],i[1],i[2]))
                    break
            print("\n---------------------------------------------------\n")
        elif(ch==3):
            srch = input('Enter Contact name to Search: ')
            DirectoryMain1 = []
            DirectoryMain1 = DirectoryMain[:]
            DirectoryMain1 = [x for x in DirectoryMain if ((x[0] == srch))]
            print("\n-----------------SEARCHED CONTACT-----------------\n")
            print(" {:15s}\t{:15s}\t{:15s}".format('NAME: ','ADDRESS: ','PHONE NUMBER: '))
            for i in DirectoryMain1:
                for j in i:
                    print(" {:15s}\t{:15s}\t{:15s}".format(i[0],i[1],i[2]))
                    break
            print("\n---------------------------------------------------\n")
        elif(ch==4):
            print("\n-----------------CONTACTS DIRECTORY-----------------\n")
            DirectoryMain.sort()
            print(" {:15s}\t{:15s}\t{:15s}".format('NAME: ','ADDRESS: ','PHONE NUMBER: '))
            for i in DirectoryMain:
                for j in i:
                    print(" {:15s}\t{:15s}\t{:15s}".format(i[0],i[1],i[2]))
                    break
            print("\n---------------------------------------------------\n")
        if (ch == 5):
            print('-----THANK YOU FOR USING THE PHONE DIRECTORY-----')
            break

        term = int(input("""
        [1] Perform another action.
        [2] Say Good Bye!!
        Do you want to perform other actions ?: """))
        print("\n---------------------------------------------------\n")

        if(term == 2):
            print('-----THANK YOU FOR USING THE PHONE DIRECTORY-----')
            break
