class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        seen = {""}
        for mat in matrix:
            if mat[-1] >= target:
                i = math.floor(len(mat) / 2)
                while i < len(mat):
                    if target == mat[i]:
                        return True
                    if i in seen:
                        break
                    seen.add(i)
                    
                    if mat[i] > target:
                        i = math.floor(i / 2)
                    else:
                        i = math.floor((i + len(mat)) / 2)
        
        return False


        