class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        kv = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for char in s:

            if char in kv:
                stack.append(char)
            else:
                if stack == []:
                    return False
                elif char == kv[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return stack == []
        