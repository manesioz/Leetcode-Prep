def is_open(char): 
    return (char == '{') or (char == '(') or (char == '[')
def is_closed(char): 
    return (char == '}') or (char == ')') or (char == ']')

def is_balanced(string):
    stack = [] 
    relation = {
        '}': '{', 
        ']': '[', 
        ')': '('
    }
    for char in string: 
        if is_open(char): 
            stack.append(char)
        elif is_closed(char): 
            if stack and stack[-1] == relation[char]: 
                print('before: ', stack)
                stack = stack[:-1]
                print('after: ', stack)
            else: 
                return False 
    if stack: 
        return False
    else: 
        return True
