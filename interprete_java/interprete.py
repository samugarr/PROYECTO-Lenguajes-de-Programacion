class Interpreter:
    def __init__(self):
        self.vars = {}

    def eval(self, node):
        if type(node) is int:
            return node

        if node[0] == 'var':
            return self.vars.get(node[1], 0)

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
                continue   # ignora cosas que no sean sentencias
            self.exec(stmt)


    def exec(self, stmt):
        if stmt[0] == 'decl':
            self.vars[stmt[1]] = self.eval(stmt[2])

        elif stmt[0] == 'assign':
            self.vars[stmt[1]] = self.eval(stmt[2])

        elif stmt[0] == 'print':
            print(self.eval(stmt[1]))

        else:
            return   # ignora cualquier cosa rara

def print_ast(node, indent=0):
    if isinstance(node, int):
        print("  " * indent + str(node))
        return

    if isinstance(node, tuple):
        print("  " * indent + str(node[0]))
        for child in node[1:]:
            print_ast(child, indent + 1)
