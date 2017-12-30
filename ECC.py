# /env/ python 3.6


"""
	pa, pb: tuple
	mod: int
	curve: list[a4, a6]
	return: tuple
	return = pa + pb on Fp-ECC
"""
def ecc_fp_add(pa, pb, p, curve):
	add_oper = lambda a,b: (a+b)%p
	if pa==pb:
		lamb = (3*pa[0]**2+curve[0])/2/pa[1]
	else:
		lamb = (pb[1]-pa[1])/(pb[0]-pa[0])
	print(lamb)
	pcx = lamb**2-pa[0]-pb[0]
	pcy = lamb*(pa[0]-pcx)-pa[1]
	return (pcx, pcy)
	

if __name__ == '__main__':
	P = (2,7)
	Q = (11,8)
	curve = [2,3]
	mod = 7
	PQ = ecc_fp_add(P,Q,mod,curve)
	print(PQ)