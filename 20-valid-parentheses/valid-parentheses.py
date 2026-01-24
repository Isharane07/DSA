class Solution(object):
    def isValid(self, s):
        stack = []

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack:
                    return False
                if stack[-1] == '(' and ch == ')':
                    stack.pop()
                elif stack[-1] == '{' and ch == '}':
                    stack.pop()
                elif stack[-1] == '[' and ch == ']':
                    stack.pop()
                else:
                    return False

        return stack == []