# & C:\Users\samug\AppData\Local\Programs\Python\Python312\python.exe c:/Users/samug/Desktop/Uni/cuarto/segundo_cuatri/lenguajes_programacion/proyecto_lenguajes_programacion/PROYECTO-Lenguajes-de-Programacion/interprete_java/main.py .\java.txt


import sys
from lexer import JavaLiteLexer
from parser import JavaLiteParser
from interprete import Interpreter, print_ast

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <archivo.java> [--ast]")
        return

    filename = sys.argv[1]
    show_ast = False

    if len(sys.argv) == 3 and sys.argv[2] == "--ast":
        show_ast = True

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
        print("\n")

    interpreter = Interpreter()
    interpreter.run(ast[1])

if __name__ == '__main__':
    main()