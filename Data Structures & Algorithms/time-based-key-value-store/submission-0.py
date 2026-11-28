class TimeMap:

    def __init__(self):
        self.struct = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.struct:
            self.struct[key] = []
        self.struct[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.struct:
            return ''
        sorted_list = self.struct[key]
        left = 0
        right = len(sorted_list) - 1

        output = ''

        while left <= right:
            mid = (left + right) // 2

            if sorted_list[mid][0] <= timestamp:
                output = sorted_list[mid][1]
                left = mid + 1
            
            else: 
                right = mid - 1
            
        return output

            