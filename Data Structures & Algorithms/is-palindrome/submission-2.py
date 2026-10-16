class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(filter(str.isalnum, s)).lower()
        y = 0
        x = len(clean) - 1
        
        while y < x:
            if clean[y] != clean[x]:
                return False
            y += 1
            x -= 1
        return True
   
        