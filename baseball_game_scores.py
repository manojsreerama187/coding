def sol(ops):
    stack=[]
    for op in ops:
        if op=="C":
            stack.pop()
        elif op=='D':
            stack.append(2*stack[-1])
        elif op=='+':
            stack.append(stack[-1]+stack[-2])
        else:
            stack.append(int(op))
    return sum(stack)    
    
    
ui=["5", "2","C","D","+"]

print(sol(ops=ui))

ui2=["5","-2","4","C","D","9","+","+"]
print(sol(ops=ui2))

ui3=["1"]
print(sol(ops=ui3))
