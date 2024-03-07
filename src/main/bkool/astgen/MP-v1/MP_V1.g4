grammar MP_V1;

options {
	language = Python3;
}

program: vardecls EOF;

vardecls: vardecl vardecltail;

vardecltail: vardecl vardecltail |;

vardecl: mptype ids ';';

mptype: INTTYPE | FLOATTYPE;

ids: ID ',' ids | ID;

INTTYPE: 'int';

FLOATTYPE: 'float';

ID: [a-z]+;

WS: [ \t\r\n]+ -> skip;