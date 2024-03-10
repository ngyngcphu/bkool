# Abstract Syntax Tree

## Exercise 6
Generate the AST of a MP_V3 input?

**For example**:
|     Test      |   Result   |
|---------------|------------|
| "a := b := 4" | Binary(:=,Id(a),Binary(:=,Id(b),IntLiteral(4))) |