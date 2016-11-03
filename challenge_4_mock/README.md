### Challenge 4
In this challenge, you will use Mock to test functions


#### Why mock?
##### Eliminates dependencies
- isolated unit tests

```
def foo(x):
  y = bar(x)
  if y > 10:
    return x+y
  return x-y
```
##### Test methods with no return value
```
def foo_1(x):
  if x > 10:
    bar(x)
  else:
    something(x)
```

##### Test error handling
- Hard to reproduce error
```
def foo_2(filename):
  try:
    return parse_large_file(filename)
  except MemoryError:
    return "boom!"
```

##### Other things:
- API call
- Database call
```
def foo_3(x):
  result = requests.get(x)
  if result.status_code == 200:
    return True
  else:
    return False
```
