class Solution:
    def isValid(self, s: str) -> bool:
        pars = {'(': ')', '[': ']', '{': '}'}
        if len(s) % 2 > 0 or (len(s) > 0 and s[0] in pars.values()):
            return False
        stack = []
        for i in s:
            if i in pars.keys():
                stack.append(i)
            elif i in pars.values():
                if len(stack) == 0:
                    return False
                expect = pars[stack[-1]]
                if i == expect:
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False
        
    
