while True:
    n = int(input("Enter number of row: ")) 
    for i in range(n):
        for j in range(n - i - 1):
            print(' ', end='')
        for j in range(2 * i+2):
            if j == 0 :
                print('*', end='')
            elif  j == 2 * i:
                print("*", end = '')
            else:
                print(' ', end='')
            
        print()