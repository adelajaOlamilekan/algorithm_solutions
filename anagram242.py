"""
The approach is to sort the two strings and compare them.
The strings will be equal if they are anagrams otherwise they won't
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)

        #Compares s and t and returns True if same otherwise False is returned
        return s == t