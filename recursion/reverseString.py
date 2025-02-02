# Reverse the string


def reverse_string(s):
    if not s:  # Base case: empty string
        return s
    return s[-1] + reverse_string(s[:-1])

print(reverse_string("hello"))

"hello"
"olleh"
