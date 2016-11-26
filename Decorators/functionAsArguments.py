def new_decorator(func):
	def wrap_func():
		print 'Code here before exec function'
		func()

		print 'Code here will execc after func'

	return wrap_func

def func_needs_decorator():
	print 'This function needs a decorator'

func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()

@new_decorator
def func_need_decorator():
	print 'Func needs a decorator'