# The function is expected to return a list.
# The function accepts string as parameter.

def logic(my_input):
    # Write your code here and remove pass statement
    # Don't print anything. Just return the intended output
    # You can create other functions and call from here
	def find_repeated_chars(string):
    # Initialize an empty list to store the repeated characters
    repeated_chars = []

    # Iterate over the characters in the string
    for char in string:
        # Check if the character appears more than once in the string
        if string.count(char) > 1:
            # If it does, add it to the list of repeated characters
            repeated_chars.append(char)

    # Print the list of repeated characters
    return repeated_chars


# Do not edit below

# Get the input
my_input = input()

# Print output returned from the logic function
print(logic("bookkeeper"))


