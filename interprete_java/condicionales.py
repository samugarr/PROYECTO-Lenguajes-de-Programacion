class Condicionales:
    """
    Mixin que añade soporte para sentencias if/else al intérprete.
    Requiere que la clase que lo use tenga los métodos eval() y exec().
    """

    def eval_condition(self, node):
        """Evalúa un nodo de condición y devuelve True o False."""
        op, a, b = node
        a = self.eval(a)
        b = self.eval(b)

        if op == '==': return a == b
        if op == '!=': return a != b
        if op == '<':  return a <  b
        if op == '>':  return a >  b
        if op == '<=': return a <= b
        if op == '>=': return a >= b

        raise ValueError(f"Operador de condicion desconocido: {op}")

    def exec_if(self, stmt):
        """
        Ejecuta una sentencia if/else.
        stmt = ('if', condition, then_stmts, else_stmts)
        else_stmts puede ser None si no hay bloque else.
        """
        _, condition, then_stmts, else_stmts = stmt

        if self.eval_condition(condition):
            for s in then_stmts:
                self.exec(s)
        elif else_stmts is not None:
            for s in else_stmts:
                self.exec(s)