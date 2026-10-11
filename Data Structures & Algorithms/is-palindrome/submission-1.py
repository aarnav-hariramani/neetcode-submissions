class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(filter(str.isalnum, s)).lower()

        left = 0
        right = len(clean) - 1

        while left < right:
            if clean[left] == clean[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True