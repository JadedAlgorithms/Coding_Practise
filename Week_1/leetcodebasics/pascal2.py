class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle=[]
        for n in range(rowIndex+1):
            row=[math.comb(n,r) for r in range(n+1)]
            triangle.append(row)
        if triangle==[]:
            return [1]
        else:
            return triangle.pop()