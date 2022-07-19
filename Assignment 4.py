while True:
    n = int(input("Enter number of row: "))      # It computes the number of rows to be printed 
    for i in range(1,n+1):                       # It iterates through each row and executes the if statement below when the condition holds
        if i == 1:
            for q in range(n):
                print(" ", end = '')
            print("*")
        for j in range(n - i - 1):
            print(' ', end='')
        for j in range(3 * i+2):
            if j == 0 :
                print('* ', end='')
            elif  j == 2 * i:
                print(" *", end = '')
            elif j == i:
                print(n-i+1,end ='') 
            else:
                print(' ', end='')
            

        print()
