# Abstract Syntax Tree

## Exercise 1
Count the terminal nodes in the parse tree?

**For example**:
|     Test      |   Result   |
|---------------|------------|
| "int a;"      | 4          |

## Exercise 2
Count the non-terminal nodes in the parse tree?

**For example**:
|     Test      |   Result   |
|---------------|------------|
| "int a;"      | 6          |

## Exercise 3
Generate the AST of a MP_V1 input?

**For example**:
|     Test      |   Result   |
|---------------|------------|
| "int a;"      | Program([VarDecl(Id(a),IntType)]) |

**Test**:
```
python3 Ex3.py input3.txt
```