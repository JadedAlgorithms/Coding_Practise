class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        count=0
        dvd=abs(dividend)
        dvs=abs(divisor)
        while dvd >= dvs:
            dvd-=dvs
            count+=1
        if (dividend < 0) != (divisor < 0): 
            return -count
        else:
            return count