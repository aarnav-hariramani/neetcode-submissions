class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        x = []

        for i in range(len(position)):
            x.append((target - position[i])/speed[i])

        combined_list = sorted(list(zip(position, x)), reverse=True)

        for val in combined_list:
            while not stack or val[1] > stack[-1][1]:
                stack.append(val)
            
        return len(stack)

        