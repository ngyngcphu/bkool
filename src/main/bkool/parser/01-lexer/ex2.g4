grammar ex2;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: EOF;

FLOAT: DIGIT ('.' DIGIT)? ('e' '-'? DIGIT)?;
fragment DIGIT: [0-9]+;


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;