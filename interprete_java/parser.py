from sly import Parser
from .lexer import JavaLiteLexer

class JavaLiteParser(Parser):
    tokens = JavaLiteLexer.tokens

    precedence = (
        ('left', PLUS, MINUS),
        ('left', MULT, DIV),
        ('right', UMINUS),
    )

    # ── Programa ──────────────────────────────────────────────────────────────

    @_('stmt_list')
    def program(self, p):
        return ('program', p.stmt_list)

    @_('stmt_list stmt')
    def stmt_list(self, p):
        return p.stmt_list + [p.stmt]

    @_('')
    def stmt_list(self, p):
        return []

    # ── Sentencias ────────────────────────────────────────────────────────────

    @_('INT IDENT ASSIGN expr ";"')
    def stmt(self, p):
        return ('decl', p.IDENT, p.expr)

    @_('IDENT ASSIGN expr ";"')
    def stmt(self, p):
        return ('assign', p.IDENT, p.expr)

    @_('PRINT "(" expr ")" ";"')
    def stmt(self, p):
        return ('print', p.expr)

    @_('IF "(" condition ")" "{" stmt_list "}" ELSE "{" stmt_list "}"')
    def stmt(self, p):
        return ('if', p.condition, p.stmt_list0, p.stmt_list1)

    @_('IF "(" condition ")" "{" stmt_list "}"')
    def stmt(self, p):
        return ('if', p.condition, p.stmt_list, None)

    # ── Condiciones ───────────────────────────────────────────────────────────

    @_('expr EQ  expr') 
    def condition(self, p): return ('==', p.expr0, p.expr1)

    @_('expr NEQ expr')
    def condition(self, p): return ('!=', p.expr0, p.expr1)

    @_('expr LT  expr')
    def condition(self, p): return ('<',  p.expr0, p.expr1)

    @_('expr GT  expr')
    def condition(self, p): return ('>',  p.expr0, p.expr1)

    @_('expr LE  expr')
    def condition(self, p): return ('<=', p.expr0, p.expr1)

    @_('expr GE  expr')
    def condition(self, p): return ('>=', p.expr0, p.expr1)

    # ── Expresiones ───────────────────────────────────────────────────────────

    @_('expr PLUS  expr')
    def expr(self, p): return ('+', p.expr0, p.expr1)

    @_('expr MINUS expr')
    def expr(self, p): return ('-', p.expr0, p.expr1)

    @_('expr MULT  expr')
    def expr(self, p): return ('*', p.expr0, p.expr1)

    @_('expr DIV   expr')
    def expr(self, p): return ('/', p.expr0, p.expr1)

    @_('MINUS expr %prec UMINUS')
    def expr(self, p): return ('neg', p.expr)

    @_('NUMBER')
    def expr(self, p): return p.NUMBER

    @_('IDENT')
    def expr(self, p): return ('var', p.IDENT)

    @_('"(" expr ")"')
    def expr(self, p): return p.expr