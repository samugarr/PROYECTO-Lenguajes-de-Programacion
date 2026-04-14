from sly import Lexer

class JavaLexer(Lexer):

    # Tokens de la gramática
    tokens = { 
        INT, BOOLEAN, STRING, # Variables
        IF, ELSE, WHILE, RETURN, # Control de flujo
        TRUE, FALSE, NULL, # Valores booleanos y nulos
        EQ, NEQ, LE, GE, LT, GR, # Operadores de comparación
        AND, OR, NOT, # Operadores lógicos
        PLUS, MINUS, MULT, DIVIDE, # Operadores aritméticos
        ASSIGN, SEMICOLON, COMMA, LPAREN, RPAREN, LBRACE, RBRACE, # Símbolos
    }

    # Variables
    INT = r'\d+'
    BOOLEAN = r'boolean'
    STRING = r'"([^"\\]|\\.)*"'

    # Control de flujo
    IF = r'if'
    ELSE = r'else'
    WHILE = r'while'
    RETURN = r'return'

    # Operadores de comparación
    EQ = r'=='
    NEQ = r'!='
    LE = r'<='
    GE = r'>='
    LT = r'<'
    GR = r'>'

    # Booleanos y nulos
    TRUE = r'true'
    FALSE = r'false'
    NULL = r'null'

    # Aritmética
    PLUS = r'\+'
    MINUS = r'-'
    MULT = r'\*'
    DIVIDE = r'/'

    # Operadores lógicos
    AND = r'&&'
    OR = r'\|\|'
    NOT = r'!'
    PLUS = r'\+'

    # Símbolos
    ASSIGN = r'='
    SEMICOLON = r';'
    COMMA = r','
    LPAREN = r'\('
    RPAREN = r'\)'
    LBRACE = r'\{'
    RBRACE = r'\}'
   
    ignore = ' \t\n' # Ignorar espacios, tabulaciones y saltos de línea