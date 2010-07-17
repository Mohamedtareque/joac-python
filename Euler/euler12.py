from math import *

def triangleGenerator():
	a = 0
	b = 0
	while True:
		a += 1
		b += a
		yield a

def getdivisores(numero):
	counter = 1
	divisor = 2
	for divisor in xrange(2, int(sqrt(numero))+1):
		if not numero%divisor:
			counter += 1
	return counter

divisores = 0	
numero = triangleGenerator()
contador = 0
while divisores <= 20:
	a = numero.next()
	divisores = getdivisores(a)
	#print a, divisores
	contador += 1
	#if not contador%1000:
	print a, divisores

print "Numero: %d \t Iteraciones: %d \t Divisores: %d" % (a, contador, divisores)		

