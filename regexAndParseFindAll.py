'''
Task 
You are given a string . It consists of alphanumeric characters, spaces and symbols(+,-). 
Your task is to find all the substrings of  that contains  or more vowels. 
Also, these substrings must lie in between  consonants and should contain vowels only.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

m = re.findall(r"(?<=[^aeiou])([aeiou]{2,})(?=[^aeiou])", input(), re.IGNORECASE)

if m:
    print(*m, sep="\n")
else:
    print(-1)