class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if s[0]==")" or s[0]=="}" or s[0]=="]":
            return False
        else:
            for i in s:
                if i in ["(","{","["]:
                    stack.append(i)
                elif i in [")","}","]"]:
                    if len(stack)>0 and ((i==")" and stack[-1]=="(") or (i=="}" and stack[-1]=="{") or (i=="]" and stack[-1]=="[")):
                        stack.pop()
                    elif i in [")","}","]"] and (("(" not in stack) or ("[" not in stack) or ("{" not in stack)):
                        return False
                        break
                else:
                    continue
            if stack==[]:
                return True
            else:
                return False
#second question, Oh my God this took so long