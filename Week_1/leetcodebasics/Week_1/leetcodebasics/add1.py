class Solution:
    def plusOne(self, digits):
        order=len(digits)
        for i in range(1,order+1):
            if digits[order-i]==9:
                digits[order-i]=0
                if order-i==0:
                    digits.insert(0,1)
            else:
                digits[order-i]+=1
                break
        return digits

