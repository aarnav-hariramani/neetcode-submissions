class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if t in s:
            return 0
        
        j = 0
        for i in range(len(s)):
            if s[i] == t[j]:
                j += 1

        return len(t) - j
        



            


        