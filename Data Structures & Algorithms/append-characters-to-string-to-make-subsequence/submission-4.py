class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        j = 0
        while j < len(t):
            if i == len(s):
                break
            if s[i] == t[j]:
                j += 1
            
            i += 1
        
        return len(t) - j


        