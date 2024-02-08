'''
Task 
Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for name is not found, print Not found instead.
Note: Your phone book should be a Dictionary/Map/HashMap data structure.

'''
# Enter your code here. Read input from STDIN. Print output to STDOUT


n = int(input())
phonebook = {}

#phonebook fill
for i in range(0, n):
    entry = input().split(" ")
    name = entry[0]
    number = entry[1]
    phonebook[name] = number
    
#print(phonebook)

#looping through to find the name 
while True:
    try: 
        name = input()
        if name in phonebook:
            number = phonebook[name]
            print(name + "=" + number)
        else:
            print("Not found")
    except:
        break
