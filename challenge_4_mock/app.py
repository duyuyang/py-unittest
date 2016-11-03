import requests

def foo_0(x):
  y = bar(x)
  if y > 10:
    return x+y
  return x-y

def foo_1(x):
  if x > 10:
    bar(x)
  else:
    something(x)

def foo_2(filename):
  try:
    return parse_large_file(filename)
  except MemoryError:
    return "boom!"

def foo_3(x):
  result = requests.get(x)
  if result.status_code == 200:
    return result.text
  else:
    return False

def bar(x):
    pass

def something(x):
    pass

def parse_large_file(filename):
    pass
