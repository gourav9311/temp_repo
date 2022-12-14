import sys

n = len(sys.argv)

print("Name of python script: ", sys.argv[0])
ch = int(sys.argv[1])

# ch = int(input("Enter choice: \n 1.Reversal of number\n2.Reversal of string\n3.Palindrome number\n4.Fibonacci series"))

#reverse number
if ch == 1:
    n = int(input("Enter number: "))
    x = n
    rev = 0
    while x != 0:
        mod = x % 10
        rev = rev * 10 + mod
        x = int(x / 10)
    print("The reversed number is: ", rev)

#reverse string
if ch == 2:
    method = int(input("Enter the way 1.By while loop\n 2.By list"))
    if method == 1:
        a = input("Enter string: ")
        b = ''
        z = len(a)
        while z != 0:
            b = b + a[z-1]
            z = z - 1
        print("The reversal of string is: ", b)
    if method == 2:
        a = input("Enter string: ")
        print(a[::-1])

#palindrome
if ch == 3:
    n = int(input("Enter number: "))
    x = n
    rev = 0
    while x != 0:
        mod = x % 10
        rev = rev * 10 + mod
        x = x / 10
        if n == x:
            print(rev, " is a palindrome number")
        else:
            print("Not palindrome")
            break


#fibonacci
if ch == 4:
    n = int(input("Enter the number up-to you want the series: "))
    a1 = 0
    a2 = 1
    a3 = 0
    i = 0
    while i != n:
        print(a3)
        a3 = a1 + a2
        a1 = a2
        a2 = a3
        i = i + 1
