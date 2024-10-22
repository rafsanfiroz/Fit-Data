
#Below code is designed to read step data from a CSV file, extract the name and step counts, and convert the step counts from strings to integers for further numerical processing.

import numpy

data = numpy.loadtxt('data.csv', delimiter=',', dtype='str') #This line loads data from a file named data.csv.

#numpy.loadtxt is a function that reads data from a text file.
#delimiter=',' specifies that the data in the file is separated by commas (CSV format).
# dtype='str' indicates that all data should be read as strings, meaning that even numbers will be treated as text at this point.

name = data[0]
steps = data[1:]

print(data)
steps = steps.astype(int) #This line is converting the data type of the steps array from strings to integers.
print(type(steps[0]))
