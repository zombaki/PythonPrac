def evaluate(lisp):
    stack=[]
    st={}

    def getval(x):
        return d.get(x, x)

    def evaluate(tokens):
        if tokens[0] in ('+', '*','/','-'):
            tmp = map(int, map(getval, tokens[1:]))
            if tokens[0]=='+':
                return str(tmp[0]+tmp[1])
            elif tokens[0]=='-':
                return str(tmp[0]-tmp[1])
            elif tokens[0]=='*':
                return str(tmp[0]*tmp[1])
            else:
                return str((tmp[0])/tmp[1])
        elif tokens[0] == "'":
            print tokens
	    return getval(tokens[-1])

    for a in lisp:
        if a == '(':
            st.append((tokens, ))
            stack=  ['']
        elif a == ' ':
            tokens.append('')
        elif a == ')':
            val = evaluate(tokens)
            tokens, d = st.pop()
            tokens[-1] += val
        else:
	    print tokens
            tokens[-1] += a
    return int(tokens[0])



print evaluate("'(6 2)")
