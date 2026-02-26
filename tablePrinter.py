while True:
    num = int(input("Enter Number to print table: "))
    ran = int(input("Enter range to print the table: "))

    if num % 2 == 0:
        print("This is even number")
    else:
        print("This is odd number")
        
    for i in range(1, ran + 1):
        if i > 50:
            break
        else:
            print(f"{num} x {i} = {num*i}")