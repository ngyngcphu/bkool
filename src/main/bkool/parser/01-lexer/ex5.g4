grammar ex5;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: EOF;

IPV4: STR '.' STR '.' STR '.' STR;
fragment STR: '0' | [1-9] DIGIT? DIGIT?;
fragment DIGIT: [0-9];

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;