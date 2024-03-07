from abc import ABC, ABCMeta, abstractmethod
import sys
import os

mpvisitor_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../../target/main/bkool/astgen/MP-v3"))
sys.path.append(mpvisitor_dir)

from MP_V3Visitor import MP_V3Visitor
from MP_V3Parser import MP_V3Parser
from MP_V3Lexer import MP_V3Lexer
from antlr4 import FileStream, InputStream, CommonTokenStream

class AST(ABC):
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

    @abstractmethod
    def accept(self, v, param):
        return v.visit(self, param)

class Expr(AST):
    __metaclass__ = ABCMeta
    pass

class Binary(Expr):
    #op:string: 
    #left:Expr
    #right:Expr
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __str__(self):
        return "Binary(" + self.op + "," + str(self.left) + "," + str(self.right) + ")"

    def accept(self, v, param):
        return v.visitBinaryOp(self, param)

class Id(Expr):
    #value:string
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Id(" + self.value + ")"

    def accept(self, v, param):
        return v.visitId(self, param)

class IntLiteral(Expr):
    #value:int
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "IntLiteral(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitIntLiteral(self, param)

class BooleanLiteral(Expr):
    #value:boolean
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "BooleanLiteral(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitBooleanLiteral(self, param)
    
# Abstract 
class ASTGeneration(MP_V3Visitor):
    # program: exp EOF;
    def visitProgram(self,ctx:MP_V3Parser.ProgramContext):
        return self.visit(ctx.exp())

    # exp: term ASSIGN exp | term;
    def visitExp(self,ctx:MP_V3Parser.ExpContext):
        if ctx.ASSIGN():
            return Binary(ctx.ASSIGN().getText(), self.visit(ctx.term()), self.visit(ctx.exp()))
        else:
            return self.visit(ctx.term())

    # term: factor COMPARE factor | factor;
    def visitTerm(self,ctx:MP_V3Parser.TermContext): 
        if ctx.COMPARE():
            return Binary(ctx.COMPARE().getText(), self.visit(ctx.factor(0)), self.visit(ctx.factor(1)))
        else:
            return self.visit(ctx.factor(0))

    # factor: factor ANDOR operand | operand;
    def visitFactor(self,ctx:MP_V3Parser.FactorContext):
        if ctx.ANDOR():
            return Binary(ctx.ANDOR().getText(), self.visit(ctx.factor()), self.visit(ctx.operand()))
        else:
            return self.visit(ctx.operand())
        

    # operand: ID | INTLIT | BOOLIT | '(' exp ')';
    def visitOperand(self,ctx:MP_V3Parser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT().getText() == 'True')
        else:
            return self.visit(ctx.exp())
        
if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.read())
        
    lexer = MP_V3Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MP_V3Parser(token_stream)
    tree = parser.program()
    visitor = ASTGeneration()
    print(visitor.visit(tree))