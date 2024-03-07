from abc import ABC, ABCMeta, abstractmethod
import sys
import os

mpvisitor_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../../target/main/bkool/astgen/MP-v1"))
sys.path.append(mpvisitor_dir)

from MP_V1Visitor import MP_V1Visitor
from MP_V1Parser import MP_V1Parser
from MP_V1Lexer import MP_V1Lexer
from antlr4 import InputStream, CommonTokenStream

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
class ASTGeneration(MP_V1Visitor):
    # program: vardecls EOF;
    def visitProgram(self,ctx:MP_V1Parser.ProgramContext):
        return Program(self.visit(ctx.vardecls()))

    # vardecls: vardecl vardecltail;
    def visitVardecls(self,ctx:MP_V1Parser.VardeclsContext):
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    # vardecltail: vardecl vardecltail |;
    def visitVardecltail(self,ctx:MP_V1Parser.VardecltailContext): 
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    # vardecl: mptype ids ';';
    def visitVardecl(self,ctx:MP_V1Parser.VardeclContext): 
        mptype = self.visit(ctx.mptype())
        ids = self.visit(ctx.ids())
        return [VarDecl(x, mptype) for x in ids]

    # mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self,ctx:MP_V1Parser.MptypeContext):
        if ctx.INTTYPE():
            return IntType()
        return FloatType()

    # ids: ID ',' ids | ID;
    def visitIds(self,ctx:MP_V1Parser.IdsContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText())]
        return [Id(ctx.ID().getText())] + self.visit(ctx.ids())
    
if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_file_path = sys.argv[1]
    else:
        input_stream = InputStream(sys.stdin.read())
        
    with open(input_file_path, 'r') as file:
        for line in file:
            input_stream = InputStream(line.strip())
            lexer = MP_V1Lexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = MP_V1Parser(token_stream)
            tree = parser.program()
            visitor = ASTGeneration()
            print(visitor.visit(tree))