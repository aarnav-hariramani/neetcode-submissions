class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        seen = {}

        for r, row in enumerate(board):
            for c, value in enumerate(row):

                box = (r // 3, c // 3)
                if value == '.':
                    continue

                if value in seen:
                    if c in seen[value]['column'] or r in seen[value]['row'] or box in seen[value]['box']:
                        return False
                    
                    else:
                        seen[value]['column'].add(c)
                        seen[value]['row'].add(r)
                        seen[value]['box'].add(box)
                else:
                    seen[value] = {'column': {c}, 'row': {r}, 'box': {box}}
                
        return True

                



                    

        