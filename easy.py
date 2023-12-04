def length_of_last_word(s):
    words = s.split()
    if not words:
        return 0
    return len(words[-1])

# Get user input
user_input = input("Enter a string: ")

# Call the function with user input
result = length_of_last_word(user_input)

# Display the result
print("Length of the last word:", result)

