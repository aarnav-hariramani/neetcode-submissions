class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for val in tokens:
            if val != '+' and val != '-' and val != '*' and val != '/':
                stack.append(int(val))
            else:
                current = stack.pop()
                b = stack.pop()

                if val == '+':
                    result = current + b
                elif val == '-':
                    result = b - current
                elif val == '*':
                    result = current * b
                else:
                    result = int(b / current)
                
                stack.append(result)
        return stack[0]            