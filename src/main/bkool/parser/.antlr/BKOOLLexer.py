# Generated from /home/ngyngcphu/Downloads/initial/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,5,32,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,1,4,1,20,8,1,11,1,12,1,21,1,1,1,1,1,
        2,1,2,1,2,1,3,1,3,1,4,1,4,0,0,5,1,1,3,2,5,3,7,4,9,5,1,0,3,1,0,97,
        122,2,0,48,57,97,122,3,0,9,10,13,13,32,32,33,0,1,1,0,0,0,0,3,1,0,
        0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,1,11,1,0,0,0,3,19,1,0,0,
        0,5,25,1,0,0,0,7,28,1,0,0,0,9,30,1,0,0,0,11,15,7,0,0,0,12,14,7,1,
        0,0,13,12,1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,2,
        1,0,0,0,17,15,1,0,0,0,18,20,7,2,0,0,19,18,1,0,0,0,20,21,1,0,0,0,
        21,19,1,0,0,0,21,22,1,0,0,0,22,23,1,0,0,0,23,24,6,1,0,0,24,4,1,0,
        0,0,25,26,9,0,0,0,26,27,6,2,1,0,27,6,1,0,0,0,28,29,9,0,0,0,29,8,
        1,0,0,0,30,31,9,0,0,0,31,10,1,0,0,0,3,0,15,21,2,6,0,0,1,2,0
    ]

class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IDENTIFIER = 1
    WS = 2
    ERROR_CHAR = 3
    UNCLOSE_STRING = 4
    ILLEGAL_ESCAPE = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "IDENTIFIER", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[2] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


