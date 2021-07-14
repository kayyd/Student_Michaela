# Question 3

# Create a function that returns the reverse of word, which matches the original string
def is_Palindrome(s):
    return s == s[::-1]

# Question 4

import unittest
from unittest import TestCase, main

class Test_Palindromes(TestCase):

# First test tests a correct palindrome in which a ‘Yes’ should be printed.
    def test_correct(self):
        s = "madam"
        ans = is_Palindrome(s)
        if ans:
            print("Yes")
        else:
            print("No")
        self.assertTrue(ans)

# Second test tests an incorrect palindrome in which a ‘No’ should be printed.
    def test_incorrect(self):
        s = "banana"
        ans = is_Palindrome(s)
        if ans:
            print("Yes")
        else:
            print("No")
        self.assertFalse(ans)

if __name__ == '__main__':
    main()

#Question 8

# Create a function
# Identify 2 integers from the list
# Ensure the 2 integers are not the same integer
# The two integers should equal the target
# Don't know how to return an empty array if no 2 numbers sum up to the target sum
# Print all options as a list
def my_function(numbers):
    for x in numbers:
        for y in numbers:
            if x != y and x + y == target:
                print([x, y])

# Define list and target sum
numbers = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10

# Call function
my_function(numbers)