class Exp:
    pass

class IntLit(Exp):
    def __init__(self, value):
        self.value = value
        
    def eval(self):
        return self.value
    
    def printPrefix(self):
        return str(self.value) + ' '
    
class FloatLit(Exp):
    def __init__(self, value):
        self.value = value
        
    def eval(self):
        return self.value
    
    def printPrefix(self):
        return str(self.value) + ' '
    
class UnExp(Exp):
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand
        
    def eval(self):
        e = self.operand.eval()
        
        if self.op == '+':
            return e
        elif self.op == '-':
            return -e
        
    def printPrefix(self):
        e = self.operand.printPrefix()
        
        if self.op == '+':
            return '+. ' + e
        elif self.op == '-':
            return '-. ' + e
        
class BinExp(Exp):
    def __init__(self, o1, op, o2):
        self.o1 = o1
        self.op = op
        self.o2 = o2
        
    def eval(self):
        e1 = self.o1.eval()
        e2 = self.o2.eval()
        
        if self.op == '+':
            return e1 + e2
        elif self.op == '-':
            return e1 - e2
        elif self.op == '*':
            return e1 * e2
        elif self.op == '/':
            return e1 / e2
        
    def printPrefix(self):
        e1 = self.o1.printPrefix()
        e2 = self.o2.printPrefix()
        
        if self.op == '+':
            return '+ ' + e1 + e2
        elif self.op == '-':
            return '- ' + e1 + e2
        elif self.op == '*':
            return '* ' + e1 + e2
        elif self.op == '/':
            return '/ ' + e1 + e2
        
if __name__ == '__main__':
    x1 = IntLit(1)
    x2 = FloatLit(2.0)
    x3 = BinExp(x1,"+",x1)
    x4 = UnExp("-",x1)
    x5 = BinExp(x4,"+",BinExp(IntLit(4),"*",x2))
    
    print(x1.printPrefix())
    print(x2.printPrefix())
    print(x3.printPrefix())
    print(x4.printPrefix())
    print(x5.printPrefix())