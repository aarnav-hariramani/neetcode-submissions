class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        kv = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for c in s:
            if c in kv:
                stack.append(c)
            else:
                if stack == []:
                    return False

                if kv[stack[-1]] == c:
                    stack.pop()
                else:
                    return False

        return stack == []

            
            
                