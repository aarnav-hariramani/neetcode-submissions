class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            if token != '+' and token != '-' and token != '*' and token != '/':
                stack.append(int(token))
            else:
                current = stack.pop()
                b = stack.pop()

                if token == '+':
                    current = current + b
                elif token == '-':
                    current = b - current
                elif token == '*':
                    current = current * b
                else:
                    current = int(b / current)
                
                stack.append(current)
        return stack[0]
                



                
        
        