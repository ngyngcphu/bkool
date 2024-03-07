from abc import ABC, ABCMeta, abstractmethod
from functools import reduce
import sys
import os

mpvisitor_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../../target/main/bkool/astgen/MP-v2"))
sys.path.append(mpvisitor_dir)

from MP_V2Visitor import MP_V2Visitor
from MP_V2Parser import MP_V2Parser
from MP_V2Lexer import MP_V2Lexer
from antlr4 import FileStream, InputStream, CommonTokenStream

class AST(ABC):
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

    @abstractmethod
    def accept(self, v, param):
        return v.visit(self, param)

class Type(AST):
    __metaclass__ = ABCMeta
    pass

class IntType(Type):
    def __str__(self):
        return "IntType"

    def accept(self, v, param):
        return v.visitIntType(self, param)

class FloatType(Type):
    def __str__(self):
        return "FloatType"

    def accept(self, v, param):
        return v.visitFloatType(self, param)


class Program(AST):
    #decl:list(Decl)
    def __init__(self, decl):
        self.decl = decl
    
    def __str__(self):
        return "Program([" + ','.join(str(i) for i in self.decl) + "])"
    
    def accept(self, v, param):
        return v.visitProgram(self, param)

class Decl(AST):
    __metaclass__ = ABCMeta
    pass

class VarDecl(Decl):
    #variable:Id
    #varType: Type
    def __init__(self, variable, varType):
        self.variable = variable
        self.varType = varType

    def __str__(self):
        return "VarDecl(" + str(self.variable) + "," + str(self.varType) + ")"

    def accept(self, v, param):
        return v.visitVarDecl(self, param)


class Id(AST):
    #name:string
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Id(" + self.name + ")"

    def accept(self, v, param):
        return v.visitId(self, param)
    
# Abstract Syntax Tree Generation
class ASTGeneration(MP_V2Visitor):
    # program: vardecl+ EOF;
    def visitProgram(self,ctx:MP_V2Parser.ProgramContext):
        return Program(reduce(lambda acc, cur: acc + self.visit(cur), ctx.vardecl(), []))

    # vardecl: mptype ids ';' ;
    def visitVardecl(self,ctx:MP_V2Parser.VardeclContext): 
        return list(map(lambda x: VarDecl(x, self.visit(ctx.mptype())), self.visit(ctx.ids())))

    # mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self,ctx:MP_V2Parser.MptypeContext):
        return IntType() if ctx.INTTYPE() else FloatType()

    # ids: ID (',' ID)*;
    def visitIds(self,ctx:MP_V2Parser.IdsContext):
        return list(map(lambda x: Id(x.getText()), ctx.ID()))
    
if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.read())
        
    lexer = MP_V2Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MP_V2Parser(token_stream)
    tree = parser.program()
    visitor = ASTGeneration()
    print(visitor.visit(tree))