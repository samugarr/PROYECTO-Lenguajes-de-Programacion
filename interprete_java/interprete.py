from .condicionales import Condicionales

class Interpreter(Condicionales):
    def __init__(self):
        self.vars = {}

    def eval(self, node):
        if type(node) is int:
            return node

        if node[0] == 'var':
            return self.vars.get(node[1], 0)

        # Unary minus: nodo de un solo hijo
        if node[0] == 'neg':
            return -self.eval(node[1])

        op, a, b = node
        a = self.eval(a)
        b = self.eval(b)

        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/': return a // b

    def run(self, program):
        for stmt in program:
            if not isinstance(stmt, tuple):
                continue
            self.exec(stmt)

    def exec(self, stmt):
        if stmt[0] == 'decl':
            self.vars[stmt[1]] = self.eval(stmt[2])

        elif stmt[0] == 'assign':
            self.vars[stmt[1]] = self.eval(stmt[2])

        elif stmt[0] == 'print':
            print(self.eval(stmt[1]))

        elif stmt[0] == 'if':
            self.exec_if(stmt)

        else:
            return  # ignora cualquier cosa rara


def print_ast(node, indent=0):
    prefix = "  " * indent

    if isinstance(node, int):
        print(prefix + str(node))
        return

    if isinstance(node, tuple):
        # Nodo unario (neg)
        if len(node) == 2 and node[0] == 'neg':
            print(prefix + 'neg')
            print_ast(node[1], indent + 1)
            return

        print(prefix + str(node[0]))
        for child in node[1:]:
            if child is None:
                print(prefix + "  (sin else)")
            elif isinstance(child, list):
                for item in child:
                    print_ast(item, indent + 1)
            else:
                print_ast(child, indent + 1)