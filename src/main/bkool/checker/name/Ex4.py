
"""
 * @author nhphung
"""
from abc import ABC, ABCMeta, abstractmethod
from functools import reduce
import sys

for path in ['../../utils', '../']:
    sys.path.append(path)

from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *

class AST(ABC):
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

    @abstractmethod
    def accept(self, v, param):
        return v.visit(self, param)

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
    #name:str,typ:Type
    def __init__(self, name, typ):
        self.name = name
        self.typ = typ

    def __str__(self):
        return "VarDecl(" + str(self.name) + "," + str(self.typ) + ")"
    
    def accept(self, v, param):
        return v.visitVarDecl(self, param)

class ConstDecl(Decl):
    #name:str,val:Lit
    def __init__(self, name, val):
        self.name = name
        self.val = val

    def __str__(self):
        return "ConstDecl(" + str(self.name) + "," + str(self.typ) + ")"
    
    def accept(self, v, param):
        return v.visitConstDecl(self, param)
    
class FuncDecl(Decl): 
    #name:str,param:List[VarDecl],body:Tuple(List[Decl],List[Expr])
    def __init__(self, name, param, body):
        self.name = name
        self.param = param
        self.body = body

    def __str__(self):
        return f"FuncDecl({str(self.name)}, [{', '.join(str(i) for i in self.param)}], ([{', '.join(str(i) for i in self.body[0])}], [{', '.join(str(i) for i in self.body[1])}])"
    
    def accept(self, v, param):
        return v.visitFuncDecl(self, param)

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
    
class Expr(AST):
    __metaclass__ = ABCMeta
    pass

class Lit(Expr):
    __metaclass__ = ABCMeta
    pass

class IntLit(Lit): 
    #val:int
    def __init__(self, val):
        self.value = val

    def __str__(self):
        return "IntLit(" + str(self.val) + ")"
    
    def accept(self, v, param):
        return v.visitIntLit(self, param)
    
class Id(Expr):
    # name: str
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Id({self.name})"

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor,Utils):

    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putIntLn",MType([IntType()],VoidType()))
    ]
            
    def __init__(self,ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ctx:Program,o:object):
        reduce(lambda acc, cur: self.visit(cur, acc), ctx.decl, [[]])

    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o[0]:
            raise RedeclaredVariable(ctx.name)
        return [o[0] + [ctx.name]] + o[1:]

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o[0]:
            raise RedeclaredConstant(ctx.name)
        return [o[0] + [ctx.name]] + o[1:]
    
    def visitFuncDecl(self, ctx:FuncDecl, o:object):
        if ctx.name in o[0]:
            raise RedeclaredFunction(ctx.name)
        env = reduce(lambda acc, cur: self.visit(cur, acc), ctx.param, [[]] + [o[0] + [ctx.name]] + o[1:])
        env = reduce(lambda acc, cur: self.visit(cur, acc), ctx.body[0], env)
        list(map(lambda cur: self.visit(cur, env), ctx.body[1]))
        
        return [o[0] + [ctx.name]] + o[1:]

    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass
    
    def visitId(self,ctx:Id,o:object):
        if not list(filter(lambda env: ctx.name in env, o)):
            raise UndeclaredIdentifier(ctx.name)
    
if __name__ == '__main__':
    ast_tree = Program([VarDecl("a",IntType()),ConstDecl("b",IntLit(3)),VarDecl("a",FloatType())])

    # Create the static checker
    checker = StaticChecker(ast_tree)

    # Try to perform static checking and catch potential errors
    try:
        result = checker.check()
    except StaticError as e:
        print(e)