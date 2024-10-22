# Reading Data from a File

import numpy

data = numpy.loadtxt('data.txt')

print(data)

# Loading data values into two variables

num1, num2 = numpy.loadtxt('data_test.csv', delimiter=',')

print(num1, num2)

# Loading one long row of data into a list


data = numpy.loadtxt('data_test.csv', delimiter=',')

print(data)

# Loading a row of data with mixed data types

# incorrect way
# data = numpy.loadtxt('data.csv', delimiter=',')

# correct ways
data = numpy.loadtxt('data.csv', delimiter=',', dtype='str')

print(data)


# make convert str type to int or float
data = numpy.loadtxt('data.csv', delimiter=',', dtype='str')

name = data[0]
steps = data[1:]

steps = steps.astype(int)  # Convert steps to a NumPy array and change the data type to int
print(type(steps[0])) # Print the type of the first element in step
