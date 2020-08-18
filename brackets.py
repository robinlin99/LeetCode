class Solution:
    def isValid(self, s):
        copy = s
        stack = []
        right = [']','}',')']
        left = ['[','{','(']
        hashmap = {']':'[','}':'{',')':'('}
        for i in s:
            if len(stack) == 0 and i in right:
                return False
            if i in left:
                stack.append(i)
            if i in right:
                if stack[len(stack)-1] == hashmap[i]:
                    stack.pop()
                else:
                    return False
        return (len(stack) == 0)
            

print(Solution().isValid('[[]]{()()}'))