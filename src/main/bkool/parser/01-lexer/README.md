# Regular Expression

## Exercise 1
Use ANTLR to write regular expressions describing a Pascal identifier that must begin with a lowercase letter (’a’ to ’z’), but may continue with many characters which are lowercase letter or digit (’0’ to ’9’).  
**For example**:

| Test  | Result    |
|-------|-----------|
| "abc" | abc,<EOF> |

**Answer**:
```antlr
IDENTIFIER: [a-z][a-z0-9]*;
```

## Exercise 2
Use ANTLR to write regular expressions describing Pascal tokens For a number to be taken as "real" (or "floating point") format, it must either have a decimal point, or use scientific notation. For example, 1.0, 1e-12, 1.0e-12, 0.000000001 are all valid reals. At least one digit must exist on either side of a decimal point.
**For example**:

| Test  | Result    |
|-------|-----------|
| "1.0" | 1.0,<EOF> |

**Answer**:
```antlr
FLOAT: DIGIT ('.' DIGIT)? ('e' '-'? DIGIT)?;
fragment DIGIT: [0-9]+;
```

## Exercise 3
Use ANTLR to write regular expressions describing Pascal strings are made up of a sequence of characters between single quotes: 'string'. The single quote itself can appear as two single quotes back to back in a string: 'isn''t'.
**For example**:

| Test  | Result    |
|-------|-----------|
| "'Yanxi Palace - 2018'"| 'Yanxi Palace - 2018',<EOF> |

**Answer**:
```antlr
STRING: '\'' ('\'\'' | ~['])* '\'';
```