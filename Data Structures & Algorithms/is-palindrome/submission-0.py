class Solution:
    def isPalindrome(self, s: str) -> bool:
        allowed = '0123456789abcdefghijklmnopqrstuvwxyz'
        new_s = ''

        for c in s:
            if c.lower() in allowed:
                new_s += c.lower()
        return new_s == new_s[::-1]
