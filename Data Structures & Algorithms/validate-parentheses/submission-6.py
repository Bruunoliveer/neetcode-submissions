class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if (char == "{" or char == "[" or char == "("):
                stack.append(char)
                continue
            else:
                if stack and ((char == "}" and stack[-1] == "{") or (char == "]" and stack[-1] == "[") or (char == ")" and stack[-1] == "(")):
                    stack.pop()
                    continue
                else:
                    return False
        if (stack==[]):
            return True
        else:
            return False