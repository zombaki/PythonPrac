def evaluate(lisp):
    stack=[]
    st=[]
    def evaluate(stack):
        #print stack[0]
        if stack[0] in ('+', '*','/','-'):
            tmp = stack[1:]
            if stack[0]=='+':
                return str(int(tmp[0])+int(tmp[1]))
            elif stack[0]=='-':
                return str(int(tmp[0])-int(tmp[1]))
            elif stack[0]=='*':
                return str(int(tmp[0])*int(tmp[1]))
            else:
                return str(int(tmp[0])/int(tmp[1]))
        elif stack[0] == "'":
            return [int(x) for x in stack[1:]]
        elif stack[0] == "concat":
            return ''.join(stack[1:]).replace('\"', '')
        elif stack[0] == "cons":
            lstack = list()
            for l in stack[1:]:
		print stack
                if not type(l) is list:
                    lstack.append(int(l))
                else:
                    lstack.extend(l)
            return lstack
    tmp=''
    flgQt=False
    for a in lisp:
        if a == '(':
            st.append((stack))
            stack=  []
            if flgQt:
                stack.append("'")
                flgQt=False
        elif a == ' ':
            stack.append(tmp)
            tmp=''
            continue
            # stack.append('')
        elif a == ')':
            stack.append(tmp)
            tmp=''
            val = evaluate(stack)
            print(val)
            stack = st.pop()
            #print val
            stack.append(val)
        elif a=='concat':
            continue
        elif a=="'":
            flgQt=True
        else:
            tmp+=a
            #print stack
            #stack.append(a)
    return (stack[0])

#print(evaluate('(concat "a" "bc")'))
#print(evaluate("'(1 2 3)"))
print(evaluate("(cons 1 '(2 3))"))
