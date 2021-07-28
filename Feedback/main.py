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
# def my_function(numbers, target):
#     for x in numbers:
#         for y in numbers:
#             if x != y and x + y == target:
#                 print([x, y])
#
#
#
# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
# target = 18
# # Expect [3, 15]
#
# my_function(array, target)
# print ("-\n")
#
# array = [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47]
# target = 163
# # Expect [-47, 210]
#
# my_function(array, target)
# print ("-\n")
#
# array = [15]
# target = 15
# # Expect []
# my_function(array, target)
