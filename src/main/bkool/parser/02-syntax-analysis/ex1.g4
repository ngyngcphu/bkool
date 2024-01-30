grammar ex1;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: declist EOF;
declist: decl declist | decl;
decl: vardecl | funcdecl;

vardecl: 'vardecl';
funcdecl: 'funcdecl';

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;