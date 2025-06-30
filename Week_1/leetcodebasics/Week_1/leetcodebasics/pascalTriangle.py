import math
class Solution:
    def generate(self, numRows: int): 
        triangle=[]
        for n in range(numRows):
            row=[math.comb(n,r) for r in range(n+1)]
            triangle.append(row)
        return triangle
#Here i used nCr (combinations) to find each element.