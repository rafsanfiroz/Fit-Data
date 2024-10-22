# Storing data

'''
Each list from this data seems exactly like the one that you dealt with in the previous lessons, and you learned an efficient way of storing this data, i.e., in the form of dictionaries. Make a function that takes in the data that contains lists of integers, changes the data type as required, and returns a dictionary. The key should be the name of the member, and the value should be a list of 168 integers.
'''

import numpy


def data_to_dict(data):
    
    data_dict = {} # Initialize an empty dictionary to store the converted data
    

    for i in range(1, len(data)):     # Iterate over each row in the data, starting from the second row (index 1)
        row = data[i]  # Get the current row
        name = row[0]  # The first element in the row is the member's name

        steps = numpy.array(row[1:], dtype=int)  # Convert the remaining elements in the row to a array of integers
        data_dict[name] = steps  
        
    return data_dict  # Return the populated dictionary

# Load data from a CSV file, specifying the delimiter and data type
data = numpy.loadtxt("steps.csv", delimiter=",", dtype=str)

# Convert the loaded data into a dictionary using the data_to_dict function
data_dict = data_to_dict(data)

print(data_dict)

'''
Next, we will define a main function to organize the overall flow of the program.
This function will also be used to test other components as needed.
'''

def main():
    # Load data from the CSV file within the main function
    data = numpy.loadtxt("steps.csv", delimiter=",", dtype=str)
    data_dict = data_to_dict(data)
    # Print the dictionary to display the results
    print(data_dict)

# Call the main function to execute the program
main()

'''
Great! So, all of your data is in the form of a dictionary now, and you can easily access the steps simply by using the name of the member. Now, move toward summary statistics.
'''
