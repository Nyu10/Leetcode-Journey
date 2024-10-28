class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = set()
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()  # Pop matched '('
                else:
                    to_remove.add(i)  # Mark ')' for removal
        to_remove.update(stack)
        result = [char for i, char in enumerate(s) if i not in to_remove]
        return "".join(result)
        