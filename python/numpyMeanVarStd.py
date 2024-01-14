'''
Task
You are given a 2-D array of size NXM. 
Your task is to find:
The mean along axis 1
The var along axis 0
The std along axis None

Output Format
First, print the mean. 
Second, print the var. 
Third, print the std.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
mean 
import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.mean(my_array, axis = 0)        #Output : [ 2.  3.]
print numpy.mean(my_array, axis = 1)        #Output : [ 1.5  3.5]
print numpy.mean(my_array, axis = None)     #Output : 2.5
print numpy.mean(my_array)                  #Output : 2.5

var 
import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.var(my_array, axis = 0)         #Output : [ 1.  1.]
print numpy.var(my_array, axis = 1)         #Output : [ 0.25  0.25]
print numpy.var(my_array, axis = None)      #Output : 1.25
print numpy.var(my_array)                   #Output : 1.25

std
import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.std(my_array, axis = 0)         #Output : [ 1.  1.]
print numpy.std(my_array, axis = 1)         #Output : [ 0.5  0.5]
print numpy.std(my_array, axis = None)      #Output : 1.11803398875
print numpy.std(my_array)                   #Output : 1.11803398875
'''

import numpy
a, b = map(int, input().split())
c = numpy.array([list(map(int, input().split())) for a in range(a)])
print(numpy.mean(c, axis = 1))
print(numpy.var(c, axis = 0))
print(numpy.round(numpy.std(c), 11))