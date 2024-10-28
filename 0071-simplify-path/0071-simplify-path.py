class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        components = path.split('/')
        print(components)

        for component in components:
            if component == '..':
                if stack:
                    stack.pop()  # Go up one directory
            elif component and component != '.':
                stack.append(component)  # Valid directory or file name
        
        return '/' + '/'.join(stack)