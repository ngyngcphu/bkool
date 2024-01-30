grammar ex5;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

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

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;