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
        4,0,13,75,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,
        1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,4,6,41,8,6,11,6,
        12,6,42,1,7,4,7,46,8,7,11,7,12,7,47,1,8,1,8,1,8,1,8,5,8,54,8,8,10,
        8,12,8,57,9,8,1,8,1,8,1,8,1,9,4,9,63,8,9,11,9,12,9,64,1,9,1,9,1,
        10,1,10,1,10,1,11,1,11,1,12,1,12,0,0,13,1,1,3,2,5,3,7,4,9,5,11,6,
        13,7,15,8,17,9,19,10,21,11,23,12,25,13,1,0,4,2,0,10,10,13,13,1,0,
        48,57,1,0,39,39,3,0,9,10,13,13,32,32,79,0,1,1,0,0,0,0,3,1,0,0,0,
        0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,
        15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,
        25,1,0,0,0,1,27,1,0,0,0,3,29,1,0,0,0,5,31,1,0,0,0,7,33,1,0,0,0,9,
        35,1,0,0,0,11,37,1,0,0,0,13,40,1,0,0,0,15,45,1,0,0,0,17,49,1,0,0,
        0,19,62,1,0,0,0,21,68,1,0,0,0,23,71,1,0,0,0,25,73,1,0,0,0,27,28,
        5,42,0,0,28,2,1,0,0,0,29,30,5,47,0,0,30,4,1,0,0,0,31,32,5,43,0,0,
        32,6,1,0,0,0,33,34,5,45,0,0,34,8,1,0,0,0,35,36,5,40,0,0,36,10,1,
        0,0,0,37,38,5,41,0,0,38,12,1,0,0,0,39,41,7,0,0,0,40,39,1,0,0,0,41,
        42,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,14,1,0,0,0,44,46,7,1,0,
        0,45,44,1,0,0,0,46,47,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,16,
        1,0,0,0,49,55,5,39,0,0,50,54,8,2,0,0,51,52,5,39,0,0,52,54,5,39,0,
        0,53,50,1,0,0,0,53,51,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,
        1,0,0,0,56,58,1,0,0,0,57,55,1,0,0,0,58,59,5,39,0,0,59,60,6,8,0,0,
        60,18,1,0,0,0,61,63,7,3,0,0,62,61,1,0,0,0,63,64,1,0,0,0,64,62,1,
        0,0,0,64,65,1,0,0,0,65,66,1,0,0,0,66,67,6,9,1,0,67,20,1,0,0,0,68,
        69,9,0,0,0,69,70,6,10,2,0,70,22,1,0,0,0,71,72,9,0,0,0,72,24,1,0,
        0,0,73,74,9,0,0,0,74,26,1,0,0,0,6,0,42,47,53,55,64,3,1,8,0,6,0,0,
        1,10,1
    ]

class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    NEWLINE = 7
    INT = 8
    STRINGLIT = 9
    WS = 10
    ERROR_CHAR = 11
    UNCLOSE_STRING = 12
    ILLEGAL_ESCAPE = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "'/'", "'+'", "'-'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "NEWLINE", "INT", "STRINGLIT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "NEWLINE", 
                  "INT", "STRINGLIT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

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
            actions[8] = self.STRINGLIT_action 
            actions[10] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     


