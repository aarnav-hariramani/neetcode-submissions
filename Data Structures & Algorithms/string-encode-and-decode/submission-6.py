class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for string in strs:
            encoded_string += str(len(string)) + '#' + string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        count = ''
        i = 0
        while i < len(s):
            if s[i] != '#':
                count += s[i]
                i += 1
            else:
                first = i + 1
                decoded_strs.append(s[first: first + int(count)])
                i += int(count) + 1
                count = ''
        return decoded_strs
