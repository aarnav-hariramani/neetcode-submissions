class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for val in strs:
            encoded_string += str(len(val)) + '#' + val
        return encoded_string

    def decode(self, s: str) -> List[str]:
        i = 0
        val = ''
        decoded_strs = []
        while i < len(s):
            if s[i] != '#':
                val += s[i]
                i += 1
            else:
                length = int(val)
                decoded_strs.append(s[i + 1 : i + length + 1])
                i += length + 1
                val = ''
        return decoded_strs