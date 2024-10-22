# Data Visualization

from matplotlib import pyplot

data = [3, 4, 5]
x_axis = [1, 2, 3]

#pyplot.pie(data)
#pyplot.show()

#pyplot.bar(x_axis, data)
#pyplot.show()

x_axis = ["a", "b", "c"]

#pyplot.bar(x_axis, data)
#pyplot.show()

x_values = [1, 2, 3, 4, 5, 6, 7]
y_values = [3000, 6000, 5000, 8000, 11000, 9000, 10000]

#pyplot.scatter(x_values, y_values)
#pyplot.show()

x_values = [1, 2, 3, 4, 5, 6, 7]
y_values = [3000, 6000, 5000, 8000, 11000, 9000, 10000]

#pyplot.plot(x_values, y_values)
#pyplot.show()

# Bubble plotting the third information

x_values = [1, 2, 3, 4, 5, 6, 7]
y_values = [3000, 6000, 5000, 8000, 11000, 9000, 10000]
weight = [100, 150, 2000, 200, 400, 300, 250]

#pyplot.scatter(x_values, y_values, weight)
#pyplot.show()

# Bar chart—coding challenge

from matplotlib import pyplot
import numpy

data = numpy.loadtxt('daily_steps.csv', delimiter = ',', dtype = str)

# Load data from a CSV file named 'daily_steps.csv'
# 'delimiter' specifies that the data is separated by commas
# 'dtype=str' ensures that all data is read as strings

days = data[0] # Reading the 0th row as an array of strings, days of the week 
steps = data[1] # Reading the next row as the steps
steps = steps.astype(int) # Converting the steps to an array of integers

pyplot.bar(days, steps) # Finally, plotting the days on the x-axis and steps on the y-axis
pyplot.show()