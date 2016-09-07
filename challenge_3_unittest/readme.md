### Challenge 3
In this challenge, you have a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

You are required to write the test case first.

#### Sample Input
```
ABCDCDC
CDC
```

#### Sample Output
```
2
```

#### Concept
```
for i in range(0, len(s)):
    print s[i: i+3]
```
