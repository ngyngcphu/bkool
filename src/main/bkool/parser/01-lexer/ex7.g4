grammar ex7;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: EOF;

SHEXA: [1-9] [0-9a-fA-F]* [02468aAcCeE];

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;