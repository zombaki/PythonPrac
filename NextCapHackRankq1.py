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
	    print stack
	    if ((stack[1])!=''):
	    	return [int(x) for x in stack[1:]]
	    else:
		return []
	elif stack[0] == "concat":
            return ''.join(stack[1:]).replace('\"', '')
    tmp=''
    flgQt=False
    if type(lisp) ==  int:
	return int(lisp)
    elif (type(lisp) ==  str and not '(' in lisp):
	return lisp
    elif lisp == '()':
	return None
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
            stack = st.pop()
	    #print val
            stack.append(val)
	elif a=="'":
	    flgQt=True
        else:
	    tmp+=a
	    #print stack
            #stack.append(a)
    return (stack[0])



print evaluate("'()")
