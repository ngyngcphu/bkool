from abc import ABC, ABCMeta, abstractmethod
from functools import reduce
import sys
import os

mpvisitor_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../../target/main/bkool/astgen/MP-v4"))
sys.path.append(mpvisitor_dir)

from MP_V4Visitor import MP_V4Visitor
from MP_V4Parser import MP_V4Parser
from MP_V4Lexer import MP_V4Lexer
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
    
class ASTGeneration(MP_V4Visitor):
    def visitProgram(self,ctx:MP_V4Parser.ProgramContext):
        return self.visit(ctx.exp())

    # exp: (term ASSIGN)* term;
    def visitExp(self,ctx:MP_V4Parser.ExpContext):
        terms = list(map(lambda x: self.visit(x), ctx.term()))
        assigns = list(map(lambda x: x.getText(), ctx.ASSIGN()))
        
        return reduce(lambda acc, cur: Binary(assigns[len(assigns) - cur - 1], terms[len(terms) - cur - 2], acc), range(len(assigns)), terms[-1])

    # term: factor COMPARE factor | factor;
    def visitTerm(self,ctx:MP_V4Parser.TermContext): 
        if ctx.COMPARE():
            return Binary(ctx.COMPARE().getText(), self.visit(ctx.factor(0)), self.visit(ctx.factor(1)))
        else:
            return self.visit(ctx.factor(0))

    # factor: operand (ANDOR operand)*;
    def visitFactor(self,ctx:MP_V4Parser.FactorContext):
        operands = list(map(lambda x: self.visit(x), ctx.operand()))
        andors = list(map(lambda x: x.getText(), ctx.ANDOR()))

        return reduce(lambda acc, cur: Binary(andors[cur], acc, operands[cur + 1]), range(len(andors)), operands[0])

    # operand: ID | INTLIT | BOOLIT | '(' exp ')';
    def visitOperand(self,ctx:MP_V4Parser.OperandContext):
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
        
    lexer = MP_V4Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MP_V4Parser(token_stream)
    tree = parser.program()
    visitor = ASTGeneration()
    print(visitor.visit(tree))