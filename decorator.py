import functools
def logger(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print ('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@logger('DEBUG')
def today():
	print ('today is Wednesday.')


today()
print "today name is: " + today.__name__