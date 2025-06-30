class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=s.split()
        w=l[-1]
        return len(w)