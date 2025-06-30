class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal = int(a,2) + int(b,2)
        if decimal == "0":
            return "0"
        binary = ""
        while decimal >0:
            remainder = decimal%2
            binary = str(remainder) + binary
            decimal = decimal//2
        return binary
