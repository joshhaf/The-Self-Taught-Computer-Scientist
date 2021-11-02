#This code is an example of a recursive algorithim that prints the numbers 1-10

def printer(n):
    if n == 0:
        return True
    print(n)
    n -= 1
    printer(n)


print(printer(10))