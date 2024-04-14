
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

class ClassDecl:
    #name:str,parent:str,mem:List[Decl]
    def __init__(self, name, parent, mem):
        self.name = name
        self.parent = parent
        self.mem = mem
    
    def __str__(self):
        return f"ClassDecl({self.name}, {self.parent}, [{', '.join(str(i) for i in self.mem)})"
    
    def accept(self, v, param):
        return v.visitClassDecl(self, param)

class VarDecl(Decl):
    #name:str,typ:Type
    def __init__(self, name, typ):
        self.name = name
        self.typ = typ

    def __str__(self):
        return "VarDecl(" + str(self.name) + "," + str(self.typ) + ")"
    
    def accept(self, v, param):
        return v.visitVarDecl(self, param)
    
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
    
class ClassType(Type):
    #name:str
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"ClassType({self.name})"
    
    def accept(self, v, param):
        return v.visitClassType(self, param)
    
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
    
    def accept(self, v, param):
        return v.visitId(self, param)
    
class FieldAccess(Expr):
    #exp:Expr,field:str
    def __init__(self, exp, field):
        self.exp = exp
        self.field = field
    
    def __str__(self):
        return f"FieldAccess({str(self.exp)}, {self.field})"
    
    def accept(self, v, param):
        return v.visitFieldAccess(self, param)

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class GetEnv(BaseVisitor,Utils):

    global_envi = []

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ctx:Program,o:object):
        return reduce(lambda acc, cur: self.visit(cur, acc), ctx.decl, [])
        
    def visitClassDecl(self,ctx:ClassDecl,o:object):
        env = reduce(lambda acc, cur: self.visit(cur, acc), ctx.mem, [])
        return o + [(ctx.name, ctx.parent, env)]

    def visitVarDecl(self,ctx:VarDecl,o:object):
        if list(filter(lambda env: ctx.name == env.name, o)):
            raise RedeclaredField(ctx.name)
        return o + [ctx]
    
    def visitFuncDecl(self, ctx:FuncDecl, o:object):
        if list(filter(lambda env: ctx.name == env.name, o)):
            raise RedeclaredMethod(ctx.name)
        return o + [ctx]

    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass
    
    def visitClassType(self,ctx:ClassType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass
    
    def visitId(self,ctx:Id,o:object):pass
        
    def visitFieldAccess(self,ctx:FieldAccess,o:object): pass

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
        o = GetEnv().visit(ctx, o)
        return list(map(lambda decl: self.visit(decl, o), ctx.decl))
        
    def visitClassDecl(self,ctx:ClassDecl,o:object):
        return [self.visit(mem, o) for mem in ctx.mem if type(mem) is FuncDecl]

    def visitVarDecl(self,ctx:VarDecl,o:object): pass
    
    def visitFuncDecl(self, ctx:FuncDecl, o:object):
        local = ctx.param + ctx.body[0]
        return list(map(lambda expr: self.visit(expr, (local, o)), ctx.body[1]))

    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass
    
    def visitClassType(self,ctx:ClassType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass
    
    def visitId(self,ctx:Id,o:object):
        type_id = next((decl.typ for decl in o[0] if decl.name == ctx.name), None)
        if not type_id:
            raise UndeclaredIdentifier(ctx.name)
        return type_id
        
    def visitFieldAccess(self,ctx:FieldAccess,o:object):
        typ = self.visit(ctx.exp, o)
        if type(typ) is not ClassType:
            return None
        while True:
            type_info, found = next(((classdecl, True) for classdecl in o[1] if classdecl[0] == typ.name), (None, False))
            if not found:
                raise UndeclaredClass(typ.name)
            mem_typ = next((mem.typ for mem in type_info[2] if mem.name == ctx.field), None)
            if mem_typ:
                return mem_typ
            class_parent = type_info[1]
            if not class_parent:
                raise UndeclaredField(ctx.field)
            typ.name = class_parent
    
if __name__ == '__main__':
    ast_tree = Program([ClassDecl("x","",[FuncDecl("foo",[],([VarDecl("m",ClassType("x"))],[FieldAccess(Id("m"),"a"),FieldAccess(Id("m"),"b")])),VarDecl("a",IntType())])])

    # Create the static checker
    checker = StaticChecker(ast_tree)

    # Try to perform static checking and catch potential errors
    try:
        result = checker.check()
    except StaticError as e:
        print(e)