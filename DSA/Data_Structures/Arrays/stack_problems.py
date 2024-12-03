# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
# The input string s is valid if and only if:
# 1 Every open bracket is closed by the same type of close bracket.
# 2 Open brackets are closed in the correct order.
# 3 Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.
#assuming only word will only consist ( ) { } [ ]

class MinStack:
    def __init__(self):
            self.stack = []
            self.min_stack = []

    def is_empty(self)->bool:
            retVal = False
            if not self.stack:
               retVal = True
            return retVal

    def push(self, val: int) -> None:
            if self.is_empty():
                self.stack.append(val)
                self.min_stack.append(val)
            else:
                self.stack.append(val)
                if val <= self.min_stack[-1]:
                    self.min_stack.append(val)

    def pop(self) -> None:
        assert not self.is_empty(), "stack is empty"
        top_stack_val = self.stack.pop()
        if top_stack_val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self)->int:
        if not self.is_empty():
            return self.stack[-1]

    def getMin(self)->int:
        if not self.is_empty():
            return self.min_stack[-1]

    def __str__(self):
        return "None" if not self.stack else str(self.stack)

def isValidParentheses(word):

    retVal      = False
    word        = list(word)
    word_len    = len(word)
    cntr        = 0
    hash = {"(": ")","{": "}","[": "]" }
    stack = []

    if word_len%2 != 0 or not word: #
        retVal = False
    else:
        for char in word:
            if char in hash: #check char is key in hash
                stack.append(char)
            else:
                if stack:
                    if hash[stack.pop()] == char:
                        cntr+=1
                    else:
                        retVal = False
                        break
                else:
                    retVal = False
                    break
    print(word_len/2)
    if cntr == word_len/2 and word_len>0:
        retVal = True
    return retVal

if __name__ == '__main__':

    stack = MinStack()
    print(stack.getMin())
    print(stack.push(-2))
    print(stack.push(0))
    print(stack.push(-3))
    print(stack.getMin())
    print(stack.pop())
    print(stack.top())
    print(stack.getMin())


