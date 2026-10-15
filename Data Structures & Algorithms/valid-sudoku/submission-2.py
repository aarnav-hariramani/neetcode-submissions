class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = {}

        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == '.':
                    continue
                
                box = (i // 3, j // 3)

                if val in seen:
                    if i in seen[val]['row'] or j in seen[val]['column'] or box in seen[val]['box']:
                        return False
                    
                    seen[val]['row'].add(i)
                    seen[val]['column'].add(j)
                    seen[val]['box'].add(box)
                
                else:
                    seen[val] = {'row': {i}, 'column': {j}, 'box': {box}}
        return True
                

                


