class Calculator:
    calculator_type = "Arithmetic Operation"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Claculator type {cls.calculator_type}")
        return a * b