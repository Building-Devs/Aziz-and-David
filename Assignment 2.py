while True:
    n = int(input("Enter row: "))
    for i in range(1,n+1):
        if i ==1:
            print("*")
        if i >1:
           print(" *" *i)    