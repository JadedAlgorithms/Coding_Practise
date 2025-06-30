class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(x+1):
            if x in range(i*i,(i+1)*(i+1)):
                return i
            