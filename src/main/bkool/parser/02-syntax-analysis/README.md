# Syntax Analysis

## Exercise 1
Given the description of a program in BKOOL as follows:  
A program in BKOOL consists of many declarations, which are variable and function declarations.
```antlr
program: // write for program rule here using vardecl and funcdecl

vardecl: 'vardecl' ;

funcdecl: 'funcdecl' ;

WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};
```

**For example**:
|     Test      |   Result   |
|---------------|------------|
| """vardecl""" | successful |

**Answer**:
```antlr
program: declist EOF;
declist: decl declist | decl;
decl: vardecl | funcdecl;

vardecl: 'vardecl';
funcdecl: 'funcdecl';
```

## Exercise 2
Given the description of a program in BKOOL as follows:  
A program in BKOOL consists of many declarations, which are **variable** and **function declarations**.  
A **variable declaration** starts with a type, which is **int** or **float**, then a comma-separated list of identifiers and ends with a semicolon.  
A **function declaration** also start with a type and then an identifier, which is the function name, and then parameter declaration and ends with a body. The parameter declaration starts with a left round bracket ’(’ and a null-able semicolon-separated list of parameters and ends with a right round bracket ’)’. Each parameter always starts with a type and then a comma-separated list of identifier.  
```antlr
program: // write your rule here

//And some other rules for variable declaration, function declaration and other rules

body: 'body';

ID: // includes a sequence of alphabetic characters.

WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};
```

**Answer**:
```antlr
program: decList EOF;
decList: decl decList | decl;
decl: varDecl | funcDecl;

varDecl: typ listIDs ';';
typ: 'int' | 'float';
listIDs: ID ',' listIDs | ID;

funcDecl: typ ID '(' listParams ')' body;

listParams: paramPrime | ;
paramPrime: param ';' paramPrime | param;
param: typ listIDs;

body: 'body';

ID: [a-zA-Z]+;
```

## Exercise 3
Given the description of a program in BKOOL as follows:  
A program in BKOOL consists of many declarations, which are **variable** and **function declarations**.  
A **variable declaration** starts with a type, which is **int** or **float**, then a comma-separated list of identifiers and ends with a semicolon.  
A **function declaration** also start with a type and then an identifier, which is the function name, and then parameter declaration and ends with a body. The parameter declaration starts with a left round bracket ’(’ and a null-able semicolon-separated list of parameters and ends with a right round bracket ’)’. Each parameter always starts with a type and then a comma-separated list of identifier. A body starts with a left curly bracket ’{’, follows by a null-able list of variable declarations or statements and ends with a right curly bracket ’}’.  
There are **3 kinds of statements**: assignment, call and return. All statements must end with a semicolon. An assignment statement starts with an identifier, then an equal ’=’, then an expression. A call starts with an identifier and then follows by a null-able comma-separated list of expressions enclosed by round brackets. A return statement starts with a symbol ’return’ and then an expression.  
```antlr
program :// write your rule for program here

//And some other rules for variable declaration, function declaration, statements but using following expr for an expression

expr: 'expr';

ID: //includes a sequence of alphabetic characters

WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};
```

**Answer**:
```antlr
program: decList EOF;
decList: decl decList | decl;
decl: varDecl | funcDecl;

varDecl: typ listIDs ';';
typ: 'int' | 'float';
listIDs: ID ',' listIDs | ID;

funcDecl: typ ID '(' listParams ')' body;

listParams: paramPrime |;
paramPrime: param ';' paramPrime | param;
param: typ listIDs;

body: '{' bodyContent '}';
bodyContent: stat_or_varDecl bodyContent |;
stat_or_varDecl: stat | varDecl;
stat: (assign | call | retur) ';';

assign: ID '=' expr;
call: ID '(' listExpr ')';
retur: 'return' expr;

listExpr: exprPrime |;
exprPrime: expr ',' exprPrime | expr;

expr: 'expr';

ID: [a-zA-Z]+;
```

## Exercise 4
Given the description of a program in BKOOL as follows:  
A program in BKOOL consists of many declarations, which are **variable** and **function declarations**.  
A **variable declaration** starts with a type, which is **int** or **float**, then a comma-separated list of identifiers and ends with a semicolon.  
A **function declaration** also start with a type and then an identifier, which is the function name, and then parameter declaration and ends with a body. The parameter declaration starts with a left round bracket ’(’ and a null-able semicolon-separated list of parameters and ends with a right round bracket ’)’. Each parameter always starts with a type and then a comma-separated list of identifier. A body starts with a left curly bracket ’{’, follows by a null-able list of variable declarations or statements and ends with a right curly bracket ’}’.  
There are **3 kinds of statements**: assignment, call and return. All statements must end with a semicolon. An assignment statement starts with an identifier, then an equal ’=’, then an expression. A call starts with an identifier and then follows by a null-able comma-separated list of expressions enclosed by round brackets. A return statement starts with a symbol ’return’ and then an expression.  
An **expression** is a construct which is made up of operators and operands. They calculate on their operands and return new value. There are four kinds of infix operators: ’+’, ’-’, ’*’ and ’/’ where ’+’ have lower precedence than ’-’ while ’*’ and ’/’ have the highest precedence among these operators. The ’+’ operator is right associative, ’-’ is non-associative while ’*’ and ’/’ is left-associative. To change the precedence, a sub-expression is enclosed in round brackets. The operands can be an integer literal, float literal, an identifier, a call or a sub-expression.  
For example:
```c
int a, b, c;
float foo(int a; float c, d) {
     int e;
     e = a + 4;
     c = a * d / 2.0;
     return c + 1;
}
float goo(float a, b) {
     return foo(1, a, b);
}
```
Some tokens:
1. An identifier includes a sequence of alphabetic characters.
2. An integer number includes a sequence of numerical characters.
3. A real (float) number includes two parts: integer and fractional parts. The integer and fractional part are like a integer number, but separated by a point (.).

**Your task**:  
Write a grammar of the program in BKOOL using ANTLR and submit its generation files to this exercise.

**Answer**:
```antlr
program: decList EOF;
decList: decl decList | decl;
decl: varDecl | funcDecl;

varDecl: typ listIDs ';';
typ: 'int' | 'float';
listIDs: ID ',' listIDs | ID;

funcDecl: typ ID '(' listParams ')' body;

listParams: paramPrime |;
paramPrime: param ';' paramPrime | param;
param: typ listIDs;

body: '{' bodyContent '}';
bodyContent: stat_or_varDecl bodyContent |;
stat_or_varDecl: stat | varDecl;
stat: (assign | call | retur) ';';

assign: ID '=' expr;
call: ID '(' listExpr ')';
retur: 'return' expr;

listExpr: exprPrime |;
exprPrime: expr ',' exprPrime | expr;

expr:
	expr ('*' | '/') expr
	| expr '-' expr
	| <assoc = right> expr '+' expr
    | '(' expr ')'
    | call
    | INT
    | FLOAT
    | ID;

ID: [a-zA-Z]+;
INT: [0-9]+;
FLOAT: INT '.' INT;
```

## Exercise 5
Trong ngôn ngữ **MiniPHP**, chương trình bao gồm các khai báo biến. Một khai báo biến được gắn liền với lần đầu tiên biến đó được gán giá trị. Phép gán trong MiniPHP bao gồm các thành phần theo thứ tự tên biến ***VARNAME***, dấu bằng ***EQ***, một biểu thức và kết thúc bởi dấu chấm phẩy ***SEMI***.  
Biểu thức trong MiniPHP là tổ hợp của các toán hạng và các toán tử được viết theo trung thứ tự (infix expression).
- Các toán hạng bao gồm: tên biến, hằng số nguyên ***INTLIT***, hằng số thực ***FLOATLIT***, hằng chuỗi ***STRINGLIT*** hoặc một mảng. Có hai loại mảng trong MiniPHP là mảng chỉ số (indexed array) và mảng phối hợp tên (associative array).
    + Mảng chỉ số bắt đầu bằng từ khóa array **ARRAY** tiếp theo là một danh sách có thể rỗng các biểu thức được phân cách bởi một dấu phẩy ***COMMA*** và được bao lại bằng một cặp ngoặc tròn ***LP*** và ***RP***.
    + Mảng phối hợp tên bằng từ khóa array **ARRAY** tiếp theo là một danh sách có thể rỗng các cặp kết hợp (associative pair) được phân cách bởi một dấu phẩy ***COMMA*** và được bao lại bằng một cặp ngoặc tròn ***LP*** và ***RP***. Một cặp kết hợp bao gồm một tên cặp ***PAIRNAME***, tiếp theo là dấu mũi tên ***ARROW*** và sau đó là một biểu thức.
- Các toán tử được liệt kê theo độ ưu tiên từ cao xuống thấp (các toán tử được mô tả trên cùng một dòng sẽ cùng một độ ưu tiên) và chỉ rõ tính kết hợp:

    + Toán tử ** ***DSTAR***: kết hợp phải

    + Toán tử . ***DOT***: kết hợp trái

+ Toán tử * ***MUL***, / ***DIV***, % ***MOD***: kết hợp trái

+ Toán tử + ***ADD***, - ***SUB**: kết hợp phải.

+ Toán tử ?? ***DQUES***: không có tính kết hợp.

- Để thay đổi được độ ưu tiên và tính kết hợp, người ta có thể sử dụng cặp ngoặc tròn để tạo biểu thức con.

Sử dụng ANTLR4 để mô tả ngôn ngữ nói trên. Biết rằng các từ in đậm và nghiêng là tên các từ vựng trong ngôn ngữ đã đặt, sinh viên sử dụng dạng thức đơn giản nhất để mô tả.

**<u>Ví dụ</u>**:  
abc = 1 + 2 ?? 3;  
u = array(a1 => 3 . 4, a2 => 3 + (u2 % 5));

**Answer**:
```antlr
program: decList EOF;
decList: varDecl decList | varDecl;

varDecl: VARNAME EQ expr SEMI;
array: indexedArr | assocArr;

indexedArr: ARRAY LP exprList RP;
exprList: exprPrime |;
exprPrime: expr COMMA exprPrime | expr;

assocArr: ARRAY LP assocList RP;
assocList: assocPrime |;
assocPrime: pair COMMA assocPrime | pair;
pair: PAIRNAME ARROW expr;

expr:
	<assoc = right>expr DSTAR expr
	| expr DOT expr
	| expr (MUL | DIV | MOD) expr
	| <assoc = right> expr (ADD | SUB) expr
	| expr DQUES expr
	| '(' expr ')'
	| array
	| VARNAME
	| INTLIT
	| FLOATLIT
	| STRINGLIT;

VARNAME: [a-z][a-z0-9]*;
PAIRNAME: [a-z][a-z0-9]*;
INTLIT: [0-9]+;
FLOATLIT: INTLIT '.' INTLIT;
STRINGLIT: '"' .*? '"';
EQ: '=';
SEMI: ';';
ARRAY: 'array';
LP: '(';
RP: ')';
COMMA: ',';
ARROW: '=>';
DSTAR: '**';
DOT: '.';
MUL: '*';
DIV: '/';
MOD: '%';
ADD: '+';
SUB: '-';
DQUES: '??';
```