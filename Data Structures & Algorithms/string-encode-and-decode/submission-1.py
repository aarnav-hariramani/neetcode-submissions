class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for vals in strs:
            encoded_string += (str(len(vals)) + '#' + vals)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        count = ''
        while i < len(s):
            if s[i] != '#':
                count += s[i]
                i += 1
            else:
                length = int(count)
                decoded_strs.append(s[i + 1:i + 1 + length])
                i += int(count) + 1
                count = ''
        return decoded_strs





