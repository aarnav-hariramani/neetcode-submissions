class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seen = {}

        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if val == '.':
                    continue

                box = (r // 3, c // 3)
                
                if val in seen:
                    if r in seen[val]['row'] or c in seen[val]['column'] or box in seen[val]['box']:
                        return False

                    seen[val]['row'].add(r)
                    seen[val]['column'].add(c)
                    seen[val]['box'].add(box)

                else:
                    seen[val] = {'row': {r}, 'column': {c}, 'box': {box}}

        return True



        