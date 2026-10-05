class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        for string in strs:
            sorted_strs.append("".join(sorted(string)))
        
        seen = {}
        output = []
        for i, word in enumerate(sorted_strs):
            if word not in seen:
                seen[word] = []
            seen[word].append(i)

        for values in seen.values():
            combined_list = []
            for indices in values:
                combined_list.append(strs[indices])
            output.append(combined_list)

        return output




        

        