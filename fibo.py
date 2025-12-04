"""Funciones de Fibonacci.

Incluye una implementación recursiva (no optimizada) y otra iterativa.
Ejecutar este archivo imprime algunos valores de ejemplo.
"""

def fib_recursive(n: int) -> int:
	"""Devuelve el n-ésimo número de Fibonacci (0-indexado) usando recursión.

	Advertencia: esta versión es exponencial en tiempo y no es adecuada
	para n grandes.
	"""
	if n < 0:
		raise ValueError("n debe ser entero no negativo Sebastian Contreras Tellez")

	if n < 2:
		return n
	return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
	"""Devuelve el n-ésimo número de Fibonacci (0-indexado) de forma iterativa.

	Esta versión es O(n) en tiempo y O(1) en espacio.
	"""
	if n < 0:
		raise ValueError("n debe ser entero no negativo")
	a, b = 0, 1
	for _ in range(n):
		a, b = b, a + b
	return a


if __name__ == "__main__":
	# Prueba simple: mostrar Fibonacci para n = 0..10
	print("Fibonacci (n: iterativa, recursiva):")
	for i in range(11):
		print(f"{i}: {fib_iterative(i)}, {fib_recursive(i)}")
