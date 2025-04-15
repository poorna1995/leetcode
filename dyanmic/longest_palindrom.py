# def longestPalindrome(s,start,end):
#     if start>end:
#         return 0
#     if start == end:
#         return 1
#     if s[start] == s[end]:
#         return 2+ longestPalindrome( s, start+1,end-1)
#     else:
#         return max(longestPalindrome(s,start+1,end),longestPalindrome(s,start,end-1))

# s='bababababc'
# print(longestPalindrome(s, 0,len('bababababc')-1))




# def longestPalindrome(s,start,end):
#     if start>end:
#         return ""
#     if start == end:
#         return s[start]
#     # If characters at the start and end are the same
#     if s[start] == s[end]:
#         subseq, length = longestPalindrome(s, start + 1, end - 1)
#         return s[start] + subseq + s[end], length + 2
#     else:
#         # Compute longest palindromic subsequences for both cases
#         subseq1, length1 = longestPalindrome(s, start + 1, end)
#         subseq2, length2 = longestPalindrome(s, start, end - 1)
        
#         # Return the longer of the two
#         if length1 > length2:
#             return subseq1, length1
#         else:
#             return subseq2, length2


# s='bababababc'
# print(longestPalindrome(s, 0,len('bababababc')-1))





def longestPalindrome(s, start, end):
    # Base cases
    if start > end:
        return "", 0
    if start == end:
        return s[start], 1

    # If characters at the start and end are the same
    if s[start] == s[end]:
        subseq, length = longestPalindrome(s, start + 1, end - 1)
        return s[start] + subseq + s[end], length + 2
    else:
        # Compute longest palindromic subsequences for both cases
        subseq1, length1 = longestPalindrome(s, start + 1, end)
        subseq2, length2 = longestPalindrome(s, start, end - 1)
        
        # Return the longer of the two
        if length1 > length2:
            return subseq1, length1
        else:
            return subseq2, length2


def memoLongest(s):
    T= [0]*(len(s)+1)
    
