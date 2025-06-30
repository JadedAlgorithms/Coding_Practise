class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x>=10):
            return False
        elif x<10:
            return True
        else:
             c=0
        a=x
        i=1
        b=x
        m=0
        while b!=0:
            b=b//10
            m+=1
        while a!=0:
            n=a%10
            a=a//10
            c=c+n*(10**(m-i))
            i+=1
        return c==x
#This was my first attempt at a leetcode problem so it's not that great

