from unicodedata import name
import unittest
import triangle

class TestTriangle1(unittest.TestCase):
    def test_add1(self):
        self.assertEqual(triangle.firstGroupTest(5,4,3),"Треугольник является разносторонним")
    def test_add2(self):
        self.assertEqual(triangle.firstGroupTest(1,1,1),"Треугольник является равносторонним")
    def test_add3(self):
        self.assertEqual(triangle.firstGroupTest(5,4,-1),"Одно из чисел <= 0")
    def test_add4(self):
        self.assertEqual(triangle.firstGroupTest(4,3,2),"Треугольник является разносторонним")
    def test_add5(self):
        self.assertEqual(triangle.firstGroupTest(10,11,12),"Треугольник является разносторонним")
    def test_add6(self):
        self.assertEqual(triangle.firstGroupTest(3,1,1),"Сумма двух из чисел больше третьего")
    def test_add7(self):
        self.assertEqual(triangle.secondGroupTest(5,4,3),"Треугольник прямоугольный, площадь: 6.00")
    def test_add8(self):
        self.assertEqual(triangle.secondGroupTest(1,1,1),"Треугольник равносторонний, площадь: 0.43")
    def test_add9(self):
        self.assertEqual(triangle.secondGroupTest(5,4,-1),"Введенные данные не могут являться сторонами треугольника")
    def test_add10(self):
        self.assertEqual(triangle.secondGroupTest(4,3,2),"Треугольник остроугольный, площадь: 2.90")
    def test_add11(self):
        self.assertEqual(triangle.secondGroupTest(10,11,12),"Треугольник остроугольный, площадь: 51.52")
    def test_add12(self):
        self.assertEqual(triangle.secondGroupTest(3,1,1),"Введенные данные не могут являться сторонами треугольника")

if __name__ == "__main__":
    unittest.main()