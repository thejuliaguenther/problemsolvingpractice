from stack import Stack 
"""
This function uses a stack to check if there is a balanced number of parenthesis
in the input, symbolString

>>> parChecker('()()(())')
True

>>> parChecker('(()')
False

>>> parChecker('(()))')
False
"""

def parChecker(symbolString):
    open_parens = Stack()
    balanced = True
    for i in range(len(symbolString)):
        if symbolString[i] =='(':
            open_parens.push(symbolString[i])
        else:
            if open_parens.isEmpty():
                balanced = False
            else:
                open_parens.pop()
    
    if open_parens.isEmpty() and balanced == True:
        return True
    else:
        return False
