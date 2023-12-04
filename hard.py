def shortest_palindrome(s):
    n = len(s)
    
    # Function to check if a string is a palindrome
    def is_palindrome(sub):
        return sub == sub[::-1]
    
    # Find the longest palindrome substring starting from the beginning
    for i in range(n, 0, -1):
        if is_palindrome(s[:i]):
            # Reverse the remaining part of the string and append it to the original string
            return s[i:][::-1] + s

# Take user input
user_input = input("Enter a string: ")
result = shortest_palindrome(user_input)
print("Shortest palindrome:", result)
