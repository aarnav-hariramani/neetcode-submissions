class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        x = []
        
        for i in range(len(position)):
            x.append((target - position[i])/speed[i])

        final_list = sorted(list(zip(position, x)), reverse=True)

        for value in final_list:
            if not stack or value[1] > stack[-1][1]:
                stack.append(value)
            
        return len(stack)