class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                secondNum = int(stack.pop())
                firstNum = int(stack.pop())

                result = 0
                match token:
                    case "+":
                        result = firstNum + secondNum
                    case "-":
                        result = firstNum - secondNum
                    case "*":
                        result = firstNum * secondNum
                    case "/":
                        result = firstNum / secondNum

                stack.append(int(result))
            else:
                stack.append(int(token))

        return stack[0]