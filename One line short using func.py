def my_decorator(func):
def wrap_func():
   print('**********')
func()

  print('**********')
return wrap_func

def hello():
  print('helllooo')

def bye():
   print('see your later')

my_decorator(hello)