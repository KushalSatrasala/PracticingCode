class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s == "":
            return 0
        
        sLen = len(s)
        i = 0
        while i < sLen and s[i] == ")":
            i += 1
        if i == sLen:
            return 0
        
        j = sLen - 1
        while j >=0 and s[j] == "(":
            j -= 1
        if j == -1:
            return 0
        
        max_count = 0
        stack = list()
        while i <= j:
            if s[i] == "(":
                stack.append((0, False))
            else:
                if len(stack) == 0:
                    stack = list()
                    i += 1
                    continue
                pop_val, flag = stack.pop()
                if flag:
                    stack = list()
                else:
                    cur_count = pop_val + 2
                    if cur_count > max_count:
                        max_count = cur_count
                    flag = True
                    if len(stack) == 0:
                        stack.append((cur_count, flag))
                    else:
                        nt_count, flag = stack.pop()
                        nt_count = nt_count + cur_count
                        if nt_count > max_count:
                            max_count = nt_count
                        stack.append((nt_count, flag))
            i += 1
        
        return max_count
        
        
            