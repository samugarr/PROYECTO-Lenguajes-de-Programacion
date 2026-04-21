from sly import Lexer

class JavaLiteLexer(Lexer):
    tokens = {
        INT, PRINT, IDENT, NUMBER,
        PLUS, MINUS, MULT, DIV, ASSIGN,
    }


    ignore = ' \t'
    ignore_comment = r'//.*'
    ignore_multiline = r'/\*[\s\S]*?\*/'


    # Operadores
    PLUS = r'\+'
    MINUS = r'-'
    MULT = r'\*'
    DIV = r'/'
    ASSIGN = r'='

    # Otros símbolos
    literals = { '(', ')', '{', '}', ';' }

    IDENT = r'[a-zA-Z_][a-zA-Z0-9_]*'
    IDENT['int'] = INT
    IDENT['print'] = PRINT



    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'\n+')
    def newline(self, t):
        self.lineno += len(t.value)