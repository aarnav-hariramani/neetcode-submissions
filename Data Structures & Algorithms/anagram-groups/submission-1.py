class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        seen = {}

        for val in strs:
            sort = "".join(sorted(val))
            if sort not in seen:
                seen[sort] = [val]
            else:
                seen[sort].append(val)
            
        for val in seen.values():
            final.append(val)
        
        return final
            