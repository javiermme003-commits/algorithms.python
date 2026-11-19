
def algint(x,i,n):
	resultado= x*(i/100+1)**n
	return round(resultado,2)

def algint_masm(x,i,n,m):
	resultado=x*(i/100+1)**n+m*((i/100+1)**n-1)/(i/100)
	return round(resultado,2)
