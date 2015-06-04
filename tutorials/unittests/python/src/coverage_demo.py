def foo(a, b=1, c=1):
	if ( a and (b or c) ):
	    return True
	return False
