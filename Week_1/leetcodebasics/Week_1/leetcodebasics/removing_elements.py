class Solution:
    def removeElement(self, nums , val: int):
        s=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[s]=nums[i]
                s+=1
        return s
        return nums