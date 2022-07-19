while True:
    n = int(input("Enter number of row: "))    
    for i in range(1, n+1):
        if i ==1:
            print('  *')
        if i==2:    
            print("  **")
        if i==3:    
            print(" ***")   
        if i>3:
            print("*"*i)   



