class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] # Push operands

        for i in range(len(tokens)):
            if tokens[i] in ("+", "-", "*", "/"):
                # expression is valid - len(stack) > 2 and integers pushed
                two, one = stack.pop(), stack.pop()
            
            if tokens[i] == "+":
                stack.append(one + two)

            elif tokens[i] == "*":
                stack.append(one * two)

            elif tokens[i] == "-":
                stack.append(one - two)

            elif tokens[i] == "/":
                stack.append(int(one / two))
            else:
                # Operand (push it to stack)
                stack.append(int(tokens[i]))
        
        return stack[0]