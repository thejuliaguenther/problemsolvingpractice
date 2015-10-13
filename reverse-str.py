from stack import Stack 

def revstring(mystr):
    str_stack = Stack()
    result = ""
    for i in range(len(mystr)):
        str_stack.push(mystr[i])

    while not str_stack.isEmpty():
        result += str_stack.pop()

    print result 
