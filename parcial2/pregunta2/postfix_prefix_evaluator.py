# Evaluador de expresiones prefijas y postfijas


class PrefixPostfixEvaluator:
    def __init__(self):
        self.stack = []

    def run_program(self):
        print("Bienvenido al evaluador de expresiones prefijas y postfijas")

        while True:
            option = input("Ingrese una opción: ")
            params = option.split(" ")
            fst_param = params[0].upper()

            if fst_param == "EVAL":
                if params[1].upper() == "PRE":
                    print(self.prefix_evaluator(params[2:]))
                elif params[1].upper() == "POST":
                    print(self.postfix_evaluator(params[2:]))
                else:
                    print("Opción inválida")
            elif fst_param == "MOSTRAR":
                if params[1].upper() == "POST":
                    print(self.postfix_to_infix(params[2:]))
                elif params[1].upper() == "PRE":
                    print(self.prefix_to_infix(params[2:]))
                else:
                    print("Opción inválida")
            elif fst_param == "SALIR":
                break
            else:
                print("Opción inválida")

    def prefix_evaluator(self, exp):
        self.stack = []
        for c in exp[::-1]:
            if c.lstrip("-").isdigit():
                self.stack.append(int(c))
            else:
                try:
                    op1 = self.stack.pop()
                    op2 = self.stack.pop()
                except:
                    # Demasiados operadores
                    raise Exception("Expresión inválida")

                self.stack.append(self.eval(op1, op2, c))

        if len(self.stack) > 1:
            # Demasiados operandos
            raise Exception("Expresión inválida")

        return self.stack.pop()

    def postfix_evaluator(self, exp: [str]) -> int:
        self.stack = []
        for c in exp:
            if c.lstrip("-").isdigit():
                self.stack.append(int(c))
            else:
                try:
                    op2 = self.stack.pop()
                    op1 = self.stack.pop()
                except:
                    # Demasiados operadores
                    raise Exception("Expresión inválida")

                self.stack.append(self.eval(op1, op2, c))

        if len(self.stack) > 1:
            # Demasiados operandos
            raise Exception("Expresión inválida")

        return self.stack.pop()

    def prefix_to_infix(self, exp: [str]) -> [str]:
        self.stack = []
        operatorUsed = []

        for c in exp[::-1]:
            if c == "+" or c == "-":
                try:
                    r = self.stack.pop()
                    l = self.stack.pop()
                except:
                    # Demasiados operadores
                    raise Exception("Expresión inválida")

                self.stack.append(r + c + l)
                operatorUsed.append(c)
            elif c == "*" or c == "/":
                try:
                    r = self.correct_expression(self.stack.pop(), operatorUsed.pop())
                    l = self.correct_expression(self.stack.pop(), operatorUsed.pop())
                except:
                    # Demasiados operadores
                    raise Exception("Expresión inválida")

                self.stack.append(r + c + l)
            else:
                self.stack.append(c)
                operatorUsed.append(None)

        if len(self.stack) > 1:
            # Demasiados operandos
            raise Exception("Expresión inválida")

        return self.stack.pop()

    # class Expression:
    #    def __init__(self, expression, operatorUsed):
    #        self.expression = expression
    #        self.operatorUsed = operatorUsed

    def postfix_to_infix(self, exp: [str]) -> [str]:
        self.stack = []
        operatorUsed = []

        for c in exp:
            if c == "+" or c == "-":
                try:
                    r = self.stack.pop()
                    l = self.stack.pop()
                except:
                    # Demasiados operadores
                    raise Exception("Expresión inválida")

                self.stack.append(l + c + r)
                operatorUsed.append(c)
            elif c == "*" or c == "/":
                try:
                    r = self.correct_expression(self.stack.pop(), operatorUsed.pop())
                    l = self.correct_expression(self.stack.pop(), operatorUsed.pop())
                except:
                    # Demasiados operadores
                    raise Exception("Expresión inválida")

                self.stack.append(l + c + r)
            else:
                self.stack.append(c)
                operatorUsed.append(None)

        if len(self.stack) > 1:
            # Demasiados operandos
            raise Exception("Expresión inválida")

        return self.stack.pop()

        # for c in exp:
        #    if c == '+' or c == '-':
        #        r = self.stack.pop().expression
        #        l = self.stack.pop().expression
        #        self.stack.append(self.Expression(l + c + r, c))
        #    elif c == '*' or c == '/':
        #        r = self.correct_expression(self.stack.pop())
        #        l = self.correct_expression(self.stack.pop())
        #        self.stack.append(self.Expression(l + c + r, c))

        #    else:
        #        self.stack.append(self.Expression(c, None))

        # return self.stack.pop().expression

    def correct_expression(self, exp, operatorUsed):
        if operatorUsed == "+" or operatorUsed == "-":
            return "(" + exp + ")"
        return exp

    # def correct_expression(self, exp):
    #    if exp.operatorUsed == '+' or exp.operatorUsed == '-':
    #        return '(' + exp.expression + ')'
    #    return exp.expression

    def eval(self, op1: int, op2: int, operator: str) -> int:
        if operator == "*":
            return op1 * op2
        elif operator == "/":
            return op1 // op2
        elif operator == "+":
            return op1 + op2
        elif operator == "-":
            return op1 - op2
        else:
            raise Exception("Operador inválido")
