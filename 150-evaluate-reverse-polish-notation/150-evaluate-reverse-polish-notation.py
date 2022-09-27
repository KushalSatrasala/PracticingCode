class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        op_stack = list()
        i = 0
        slen = len(tokens)
        
        while i < slen:
            #print(i)
            if len(tokens[i]) >= 2 or tokens[i].isnumeric():
                if tokens[i].startswith("-"):
                    op_stack.append(-int(tokens[i][1:]))
                else:
                    op_stack.append(int(tokens[i]))
            else:
                op2 = op_stack.pop()
                op1 = op_stack.pop()
                if tokens[i] == "+":
                    res = op1 + op2
                elif tokens[i] == "-":
                    res = op1 - op2
                elif tokens[i] == "/":
                    res = int(op1 / op2)
                elif tokens[i] == "*":
                    res = op1 * op2
                op_stack.append(res)
            #print(op_stack)
            i += 1
        
        return op_stack.pop()