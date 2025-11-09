from typing import Union


Number = Union[int, float]


def ma(a: Number, b: Number) -> Number:
	"""Return the larger of two numbers.

	Args:
		a: First number (int or float).
		b: Second number (int or float).

	Returns:
		The greater of a and b (same type if possible).

	Examples:
		>>> ma(2, 3)
		3
		>>> ma(4.5, 2)
		4.5
	"""
	return a if a >= b else b


if __name__ == "__main__":
	print("ma(2, 3) ->", ma(2, 3))
	print("ma(5, -1) ->", ma(5, -1))
	print("ma(3.2, 7.1) ->", ma(3.2, 7.1))

