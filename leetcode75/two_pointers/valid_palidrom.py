# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.
# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


def ValidPalindrome(s):
    # Initialize two pointers
    # remove all non-alphanumeric characters and convert to lowercase
    clean_text = ''.join(char for char in s if char.isalnum()).lower()
    left, right = 0, len(clean_text) - 1
    while left <right:
        if clean_text[left]!= clean_text[right]:
            left +=1
            right -=1
        else:
            return True

    print(clean_text)
    
    
s = "A man, a plan, a canal: Panama"
print(ValidPalindrome(s))

