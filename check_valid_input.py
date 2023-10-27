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

ui4=["1","C" ]
print(sol(ops=ui4))

ui5=["5", "10", "C", "D", "+", "3", "c"]
#print(sol(ops=ui5))


def input_check(values):
    check=["C","D","+"]
    for op in values:
        if op in check:
            continue
        elif op.isdigit() or (op[0]=='-' and op[1:].isdigit()):
              continue
          
        return False
    return True
        
q=input_check(values=ui5)
print(q)

