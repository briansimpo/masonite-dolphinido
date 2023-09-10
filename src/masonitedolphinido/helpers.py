import itertools

def grouper(iterable, n, fillvalue=None):
	args = [iter(iterable)] * n
	return (filter(None, params) for params in itertools.zip_longest(fillvalue=fillvalue, *args))
