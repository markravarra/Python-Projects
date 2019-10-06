def mult():
    
    print 'Multiplication Table upto 5'
    n=5
    for i in range(1,n+1):
        for j in range(1,11):
            print(i*j, end="\t")
        print()
mult()
