grammar ex4;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: EOF;

BKID: NAME '.' NAME OPTION;
fragment NAME: [a-z]+;
fragment OPTION: CHAR? CHAR? CHAR? CHAR? [a-z0-9_];
fragment CHAR: [a-z0-9._];

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;