# Generated from /home/ngyngcphu/Downloads/initial/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete listener for a parse tree produced by BKOOLParser.
class BKOOLListener(ParseTreeListener):

    # Enter a parse tree produced by BKOOLParser#program.
    def enterProgram(self, ctx:BKOOLParser.ProgramContext):
        pass

    # Exit a parse tree produced by BKOOLParser#program.
    def exitProgram(self, ctx:BKOOLParser.ProgramContext):
        pass


    # Enter a parse tree produced by BKOOLParser#expr.
    def enterExpr(self, ctx:BKOOLParser.ExprContext):
        pass

    # Exit a parse tree produced by BKOOLParser#expr.
    def exitExpr(self, ctx:BKOOLParser.ExprContext):
        pass



del BKOOLParser