class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        for char in s:
            if char in close_to_open:
                # Must have a matching open bracket at the top of the stack
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        # Valid only if every opened bracket was closed
        return not stack