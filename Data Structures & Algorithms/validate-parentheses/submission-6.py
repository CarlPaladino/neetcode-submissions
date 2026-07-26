class Solution:
    def isValid(self, s: str) -> bool:
        roundParentheses = ['(', ')']
        curlyParentheses = ['{', '}']
        squareParentheses = ['[', ']']

        stack = []

        for char in s:
            if char == roundParentheses[0] or char == curlyParentheses[0] or char == squareParentheses[0]:
                stack.append(char)
            elif char == roundParentheses[1] or char == curlyParentheses[1] or char == squareParentheses[1]:
                if not stack:
                    return False

                if stack[-1] == roundParentheses[0] and char == roundParentheses[1]:
                    stack.pop()
                elif stack[-1] == curlyParentheses[0] and char == curlyParentheses[1]:
                    stack.pop()
                elif stack[-1] == squareParentheses[0] and char == squareParentheses[1]:
                    stack.pop()
                else:
                    return False
            else: 
                continue
        
        return len(stack) == 0