def reverse_polish_notation(formula):
    stack = []
    for d in formula:
        if type(d) == int:
            stack.append(d)
        else:
            x = stack.pop()
            y = stack.pop()
            stack.append(d(x, y))
    return stack.pop()
        
