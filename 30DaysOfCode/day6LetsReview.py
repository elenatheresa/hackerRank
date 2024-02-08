'''
Given a string, S, of length N that is indexed from 0 to N - 1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).
Note: 0 is considered to be an even index.

'''



# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())

for i in range(0, a):
    s = input()

    for l in range(0, len(s)):
        if l % 2 == 0:
            print(s[l], end="")
    print(" ", end="")
    for l in range(0, len(s)):
        if l % 2 != 0:
            print(s[l], end="")
    print(" ")