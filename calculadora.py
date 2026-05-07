class Calculadora:
    """Una calculadora básica siguiendo principios de TDD."""

    def sumar(self, a: float, b: float) -> float:
        return a + b

    def restar(self, a: float, b: float) -> float:
        return a - b

    def multiplicar(self, a: float, b: float) -> float:
        return a * b

    def dividir(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Error: División por cero no permitida.")
        return a / b