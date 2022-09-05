class Solution:
    def decodeString(self, s: str) -> str:
        stack = list()
        stack.append("#")
        slen = len(s) - 1
        i = 0
        left = ""
        right = ""
        while i <= slen and s[i].isalpha():
            left += s[i]
            i += 1
        if i > slen:
            return s 

        while slen >= 0 and s[slen].isalpha():
            right += s[slen]
            slen -= 1

        while i <= slen:
            cur_ch = s[i]
            #print(cur_ch)
            if cur_ch == "]":
                ch_str = ""
                stack_ch = stack.pop()
                while stack_ch != "[":
                    ch_str += stack_ch
                    stack_ch = stack.pop()
                rep = ""
                p = stack.pop()
                while p.isnumeric():
                    rep += p
                    p = stack.pop()
                stack.append(p)
                temp = ch_str * int(rep[::-1])
                stack.append(temp)
                #print(stack)
            else:
                stack.append(cur_ch)
            #print(stack)
            i += 1
        
        res_str = ""
        pop = stack.pop()
        while pop != "#":
            res_str += pop
            pop = stack.pop()
        
        return left + res_str[::-1] + right[::-1]