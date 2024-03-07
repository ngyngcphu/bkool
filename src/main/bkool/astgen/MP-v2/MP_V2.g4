grammar MP_V2;

options {
	language = Python3;
}

program: vardecl+ EOF;

vardecl: mptype ids ';' ;

mptype: INTTYPE | FLOATTYPE;

ids: ID (',' ID)*; 

INTTYPE: 'int';

FLOATTYPE: 'float';

ID: [a-z]+ ;

WS: [ \t\r\n]+ -> skip;