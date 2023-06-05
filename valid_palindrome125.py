"""
The Approach uses two pointers to solve the problem; two pointers are created at the extremes of the string 
the character of each pointer is compared for similarity; if otherwise the palindrome test fails.
Non alphanumeric characters are skipped to ensure only alphanumeric characters are compared to each other. 
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = True
        l = 0
        r = len(s)-1

        s = s.lower()
        print(s)
        while l < r:
            if not (s[l].isalnum()):
                l += 1
                continue
            if not (s[r].isalnum()):
                r -= 1
                continue
            if s[l] != s[r]:
                result = False
                break
            else:
                l += 1
                r -= 1

        return result