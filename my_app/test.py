
from my_app.calculat import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_adding_success(self):
        assert self.calc.adding(5, 1) == 6

    def test_multiply_success(self):
        assert self.calc.multiply(2, 5) == 10

    def test_division_success(self):
        assert self.calc.division(8, 4) == 2

    def test_subtraction_success(self):
        assert self.calc.subtraction(7, 3) == 4

    def teardown(self):
        print("Выполнение метода Teardown")
