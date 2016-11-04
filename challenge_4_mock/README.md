### Challenge 4
In this challenge, you will use Mock to test functions
```
git clone https://duyuyang@bitbucket.org/duyuyang/ap-dojo-testing.git
```

#### Environment
- python 2.7
```
$ cd challenge_4_mock
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

#### Why mock?
##### Eliminates dependencies
- isolated unit tests

```
def foo_0(x):
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

#### Assert
- assertEqual
- mock_a.assert_any_call('arg')
- mock_b.assert_called_with('arg')
- mock_c.assert_called_once_with('arg')
- mock_d.assert_not_called()
- assertRaises(Exception, lambda: mock_0)
