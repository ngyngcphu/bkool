# Regular Expression

## Exercise 1
Use ANTLR to write regular expressions describing a Pascal identifier that must begin with a lowercase letter (’a’ to ’z’), but may continue with many characters which are lowercase letter or digit (’0’ to ’9’).  
**For example**:

| Test  | Result    |
|-------|-----------|
| "abc" | abc,<EOF> |

**Answer**:
```antlr
IDENTIFIER: [a-z][a-z][0-9]*;
```