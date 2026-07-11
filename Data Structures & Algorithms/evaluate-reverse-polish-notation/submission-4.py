class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            ''' if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(token)) '''
            if c in '+-*/':
                a, b = stack.pop(), stack.pop()
                if c == '+': stack.append(a + b)
                elif c == '-': stack.append(b - a)
                elif c == '*': stack.append(a * b)
                elif c == '/': stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]
