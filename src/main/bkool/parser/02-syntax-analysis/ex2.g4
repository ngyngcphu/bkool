grammar ex2;

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

listParams: paramPrime | ;
paramPrime: param ';' paramPrime | param;
param: typ listIDs;

body: 'body';

ID: [a-zA-Z]+;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;