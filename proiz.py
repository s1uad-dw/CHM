def fxsy():
	import sympy as sym 
	x = sym.Symbol("x")
	f=3-x**2
	return str(f.diff(x))