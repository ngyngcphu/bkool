import sys
import os

mpvisitor_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../../target/main/bkool/astgen/MP-v1"))
sys.path.append(mpvisitor_dir)

from MP_V1Visitor import MP_V1Visitor
from MP_V1Parser import MP_V1Parser
from MP_V1Lexer import MP_V1Lexer
from antlr4 import FileStream, InputStream, CommonTokenStream

class ASTGeneration(MP_V1Visitor):
    # program: vardecls EOF;
    def visitProgram(self,ctx:MP_V1Parser.ProgramContext):
        return 1 + self.visit(ctx.vardecls())

    # vardecls: vardecl vardecltail;
    def visitVardecls(self,ctx:MP_V1Parser.VardeclsContext):
        return 1 + self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    # vardecltail: vardecl vardecltail |;
    def visitVardecltail(self,ctx:MP_V1Parser.VardecltailContext): 
        if ctx.getChildCount() == 2:
            return 1 + self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())
        return 1

    # vardecl: mptype ids ';';
    def visitVardecl(self,ctx:MP_V1Parser.VardeclContext): 
        return 1 + self.visit(ctx.mptype()) + self.visit(ctx.ids())

    # mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self,ctx:MP_V1Parser.MptypeContext):
        return 1

    # ids: ID ',' ids | ID;
    def visitIds(self,ctx:MP_V1Parser.IdsContext):
        if ctx.getChildCount() == 3:
            return 1 + self.visitIds(ctx.ids())
        return 1
    
if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.read())
        
    lexer = MP_V1Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MP_V1Parser(token_stream)
    tree = parser.program()
    visitor = ASTGeneration()
    print(visitor.visit(tree))