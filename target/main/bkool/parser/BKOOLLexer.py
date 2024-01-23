# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("M\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\6\b+\n\b\r\b\16\b,\3\t\6\t\60\n\t\r\t\16\t\61\3\n")
        buf.write("\3\n\3\n\3\n\7\n8\n\n\f\n\16\n;\13\n\3\n\3\n\3\n\3\13")
        buf.write("\6\13A\n\13\r\13\16\13B\3\13\3\13\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\16\3\16\2\2\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\3\2\6\4\2\f\f\17\17\3\2\62;")
        buf.write("\3\2))\5\2\13\f\17\17\"\"\2Q\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5\37\3\2\2")
        buf.write("\2\7!\3\2\2\2\t#\3\2\2\2\13%\3\2\2\2\r\'\3\2\2\2\17*\3")
        buf.write("\2\2\2\21/\3\2\2\2\23\63\3\2\2\2\25@\3\2\2\2\27F\3\2\2")
        buf.write("\2\31I\3\2\2\2\33K\3\2\2\2\35\36\7,\2\2\36\4\3\2\2\2\37")
        buf.write(" \7\61\2\2 \6\3\2\2\2!\"\7-\2\2\"\b\3\2\2\2#$\7/\2\2$")
        buf.write("\n\3\2\2\2%&\7*\2\2&\f\3\2\2\2\'(\7+\2\2(\16\3\2\2\2)")
        buf.write("+\t\2\2\2*)\3\2\2\2+,\3\2\2\2,*\3\2\2\2,-\3\2\2\2-\20")
        buf.write("\3\2\2\2.\60\t\3\2\2/.\3\2\2\2\60\61\3\2\2\2\61/\3\2\2")
        buf.write("\2\61\62\3\2\2\2\62\22\3\2\2\2\639\7)\2\2\648\n\4\2\2")
        buf.write("\65\66\7)\2\2\668\7)\2\2\67\64\3\2\2\2\67\65\3\2\2\28")
        buf.write(";\3\2\2\29\67\3\2\2\29:\3\2\2\2:<\3\2\2\2;9\3\2\2\2<=")
        buf.write("\7)\2\2=>\b\n\2\2>\24\3\2\2\2?A\t\5\2\2@?\3\2\2\2AB\3")
        buf.write("\2\2\2B@\3\2\2\2BC\3\2\2\2CD\3\2\2\2DE\b\13\3\2E\26\3")
        buf.write("\2\2\2FG\13\2\2\2GH\b\f\4\2H\30\3\2\2\2IJ\13\2\2\2J\32")
        buf.write("\3\2\2\2KL\13\2\2\2L\34\3\2\2\2\b\2,\61\679B\5\3\n\2\b")
        buf.write("\2\2\3\f\3")
        return buf.getvalue()


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
        self.checkVersion("4.9.2")
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
     


