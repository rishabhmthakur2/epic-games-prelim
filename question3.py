"""
Write a method to convert a string containing a comma-separated list of integers into a new
string composed of the characters represented by each integer.

Example
Input: string "73,32,119,105,110,33"
Output: string "I win!"
"""

# Function to convert the input string into the required output string
def convertToString(nums):
    # Converting the input string of integers into an array
    # Using the python in-built split() function. Using comma as a delimiter to split
    nums = nums.split(",")
    # Creating an empty string to store the output
    output = ""
    # Looping through all the items in the array created from the input
    for num in nums:
        # Using the int() function to convert the string element of the array into an integer
        # Using the chr() function that gives out the character for each ASCII value.
        output += chr(int(num))
    # returning the output string
    return output

print(convertToString("73,32,119,105,110,33"))
