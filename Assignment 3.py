while True:
    n = int(input("Enter number of row: "))            
    for i in range(n):                       # It iterates each row in the given range
        for j in range(n - i - 1):           # It iterates each column in the specified range and print spaces depending on the given range
            print(' ', end='')
        for j in range(2 * i+2):                 # It iterates the given range and executes the following if statements provided the conditions are true
            if j == 0 :
                print('*', end='')
            elif  j == 2 * i:
                print("*", end = '')
            else:
                print(' ', end='')
            
        print()
