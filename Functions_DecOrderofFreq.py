# Write Python code to create a function called most_frequent that takes a string
# and prints the letters in decreasing order of frequency. Use dictionaries.

import operator


def most_frequent():
    dic = {}
    a = input('Please Enter a String: ')
    for i in a:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
# descending order
        sorted_d = dict(sorted(dic.items(), key=operator.itemgetter(1), reverse=True))
# added '=' & '0' before the value to get the same output as required.
    result = ''.join(f' {key} = 0{value} ' for key, value in sorted_d.items())
    print(result)


most_frequent()
