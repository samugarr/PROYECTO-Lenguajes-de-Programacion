import sys
from interprete_java.lexer import JavaLiteLexer
from interprete_java.parser import JavaLiteParser
from interprete_java.interprete import Interpreter, print_ast

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <archivo.java> [--ast]")
        return

    filename = sys.argv[1]
    show_ast = '--ast' in sys.argv

    try:
        with open(filename, 'r') as f:
            code = f.read()
    except FileNotFoundError:
        print("Archivo no encontrado")
        return

    lexer = JavaLiteLexer()
    parser = JavaLiteParser()

    ast = parser.parse(lexer.tokenize(code))

    if show_ast:
        print("\nÁRBOL AST DEL PROGRAMA:\n")
        for stmt in ast[1]:
            print_ast(stmt)
        print()

    interpreter = Interpreter()
    interpreter.run(ast[1])

if __name__ == '__main__':
    main()