from sly import Parser
from lexer import JavaLiteLexer

class JavaLiteParser(Parser):
    tokens = JavaLiteLexer.tokens

    precedence = (
        ('left', PLUS, MINUS),
        ('left', MULT, DIV),
    )

    @_('stmt_list')
    def program(self, p):
        return ('program', p.stmt_list)

    @_('stmt_list stmt')
    def stmt_list(self, p):
        return p.stmt_list + [p.stmt]

    @_('')
    def stmt_list(self, p):
        return []

    @_('INT IDENT ASSIGN expr ";"')
    def stmt(self, p):
        return ('decl', p.IDENT, p.expr)

    @_('IDENT ASSIGN expr ";"')
    def stmt(self, p):
        return ('assign', p.IDENT, p.expr)

    @_('PRINT "(" expr ")" ";"')
    def stmt(self, p):
        return ('print', p.expr)


    @_('expr PLUS expr')
    def expr(self, p):
        return ('+', p.expr0, p.expr1)

    @_('expr MINUS expr')
    def expr(self, p):
        return ('-', p.expr0, p.expr1)

    @_('expr MULT expr')
    def expr(self, p):
        return ('*', p.expr0, p.expr1)

    @_('expr DIV expr')
    def expr(self, p):
        return ('/', p.expr0, p.expr1)

    @_('NUMBER')
    def expr(self, p):
        return p.NUMBER

    @_('IDENT')
    def expr(self, p):
        return ('var', p.IDENT)

    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr