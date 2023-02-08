# Write a Python program to print all positive numbers in a range.


# Input: list2 = [12, 14, -95, 3] Output: [12, 14, 3].

list2 = [12, 14, -95, 3]
li = []
for num in list2:
    if num >= 0:
        li.append(num)
print(li)

# Input: list1 = [12, -7, 5, 64, -14] Output: 12, 5, 64.

list1 = [12, -7, 5, 64, -14]
for num in list1:
    if num >= 0:
        print(num, end=',')
