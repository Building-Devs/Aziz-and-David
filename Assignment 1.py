while True:
    n = int(input("Enter number of row: "))    # This specifies the numbers of rows to print
    for i in range(1, n+1):                    # It iterates the given range and executes the following if statements provided the conditions are true
        if i ==1:
            print('  *')
        if i==2:    
            print("  **")
        if i==3:    
            print(" ***")   
        if i>3:
            print("*"*i)   



