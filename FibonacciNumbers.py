# Write a Python Program for Fibonacci numbers.

a = int(input('Enter no of terms: '))
n1 = 0
n2 = 1
count = 0
if a <= 0:
    print('Invalid value. ')
elif a == 1:
    print(n1)
else:
    print('Fibo sequence: ')
    while count < a:
        print(n1)
        n = n1 + n2
        n1 = n2
        n2 = n
        count = count + 1
