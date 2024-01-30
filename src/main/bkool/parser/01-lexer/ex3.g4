grammar ex3;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: EOF;

STRING: '\'' ('\'\'' | ~['])* '\'';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;