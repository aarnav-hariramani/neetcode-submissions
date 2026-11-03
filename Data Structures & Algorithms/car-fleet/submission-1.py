class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        x = []
        
        for i in range(len(position)):
            x.append((target - position[i])/speed[i])
        
        combined_list = sorted(list(zip(position, x)), reverse=True)

        for i in range(len(combined_list)):
            if not stack or combined_list[i][1] > stack[-1]:
                stack.append(combined_list[i][1])
        
        return len(stack)