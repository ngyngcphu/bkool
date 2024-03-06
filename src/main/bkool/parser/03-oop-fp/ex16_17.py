class Exp:
    pass

class BinExp(Exp):
    def __init__(self,o1,op,o2):
        self.left = o1
        self.op = op
        self.right = o2
        
    def accept(self, v):
        return v.visitBinExp(self)
        
class UnExp(Exp): 
    def __init__(self,op,o1):
        self.op = op
        self.operand = o1
        
    def accept(self, v):
        return v.visitUnExp(self)
        
class IntLit(Exp):
    def __init__(self,v):
        self.value = v
        
    def accept(self, v):
        return v.visitIntLit(self)
        
class FloatLit(Exp):
    def __init__(self,v):
        self.value = v
        
    def accept(self, v):
        return v.visitFloatLit(self)
        
class Eval:
    def visit(self, x):
        return x.accept(self)
    
    def visitIntLit(self, x: IntLit):
        return x.value
    
    def visitFloatLit(self, x: FloatLit):
        return x.value
    
    def visitUnExp(self, x: UnExp):
        e = self.visit(x.operand)
            
        if x.op == '+':
            return e
        elif x.op == '-':
            return -e
        
    def visitBinExp(self, x: BinExp):
        e1 = self.visit(x.left)
        e2 = self.visit(x.right)
        
        if x.op == '+':
            return e1 + e2
        elif x.op == '-':
            return e1 - e2
        elif x.op == '*':
            return e1 * e2
        elif x.op == '/':
            return e1 / e2
            
class PrintPrefix:
    def visit(self, x):
        return x.accept(self)
    
    def visitIntLit(self, x: IntLit):
        return str(x.value) + ' '
    
    def visitFloatLit(self, x: FloatLit):
        return str(x.value) + ' '
    
    def visitUnExp(self, x: UnExp):
        e = self.visit(x.operand)
        
        if x.op == '+':
            return '+. ' + e
        elif x.op == '-':
            return '-. ' + e
        
    def visitBinExp(self, x: BinExp):
        e1 = self.visit(x.left)
        e2 = self.visit(x.right)
        
        if x.op == '+':
            return '+ ' + e1 + e2
        elif x.op == '-':
            return '- ' + e1 + e2
        elif x.op == '*':
            return '* ' + e1 + e2
        elif x.op == '/':
            return '/ ' + e1 + e2
        
class PrintPostfix:
    def visit(self, x):
        return x.accept(self)
    
    def visitIntLit(self, x: IntLit):
        return str(x.value) + ' '
    
    def visitFloatLit(self, x: FloatLit):
        return str(x.value) + ' '
    
    def visitUnExp(self, x: UnExp):
        e = self.visit(x.operand)
        
        if x.op == '+':
            return e + '+. '
        elif x.op == '-':
            return e + '-. '
        
    def visitBinExp(self, x: BinExp):
        e1 = self.visit(x.left)
        e2 = self.visit(x.right)
        
        if x.op == '+':
            return e1 + e2 + '+ '
        elif x.op == '-':
            return e1 + e2 + '- '
        elif x.op == '*':
            return e1 + e2 + '* '
        elif x.op == '/':
            return e1 + e2 + '/ '
            
if __name__ == '__main__':
    x1 = IntLit(1)
    x2 = FloatLit(2.0)
    x3 = BinExp(x1,"+",x1)
    x4 = UnExp("-",x1)
    x5 = BinExp(x4,"+",BinExp(IntLit(4),"*",x2))
    v1 = Eval()
    v2 = PrintPrefix()
    v3 = PrintPostfix()
    print(v1.visit(x1))
    print(v2.visit(x1))
    print(v3.visit(x1))
    print(v1.visit(x2))
    print(v2.visit(x2))
    print(v3.visit(x2))
    print(v1.visit(x3))
    print(v2.visit(x3))
    print(v3.visit(x3))
    print(v1.visit(x4))
    print(v2.visit(x4))
    print(v3.visit(x4))
    print(v1.visit(x5))
    print(v2.visit(x5))
    print(v3.visit(x5))