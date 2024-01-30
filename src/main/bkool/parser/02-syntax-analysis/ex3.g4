grammar ex3;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

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

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;