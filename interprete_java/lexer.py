from sly import Lexer

class JavaLiteLexer(Lexer):
    tokens = {
        INT, PRINT, IF, ELSE,
        IDENT, NUMBER,
        PLUS, MINUS, MULT, DIV, ASSIGN,
        EQ, NEQ, LT, GT, LE, GE,
    }

    ignore = ' \t'
    ignore_comment = r'//.*'
    ignore_multiline = r'/\*[\s\S]*?\*/'

    # Operadores aritméticos
    PLUS  = r'\+'
    MINUS = r'-'
    MULT  = r'\*'
    DIV   = r'/'

    # Operadores de comparación (los de dos caracteres ANTES que los de uno)
    EQ    = r'=='
    NEQ   = r'!='
    LE    = r'<='
    GE    = r'>='
    LT    = r'<'
    GT    = r'>'

    ASSIGN = r'='

    # Otros símbolos
    literals = { '(', ')', '{', '}', ';' }

    # Identificadores y palabras clave
    IDENT = r'[a-zA-Z_][a-zA-Z0-9_]*'
    IDENT['int']   = INT
    IDENT['print'] = PRINT
    IDENT['if']    = IF
    IDENT['else']  = ELSE

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'\n+')
    def newline(self, t):
        self.lineno += len(t.value)