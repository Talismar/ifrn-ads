from src import TriangleIdentifier

class TestIdentifier:
    
    def setup_method(self, method):
        """
            setup any state specific to the execution of the given class 
            (which usually contains tests).
        """
        
    def teardown_method(self, method):
        """
            teardown any state that was previously setup with a call to
            setup_class.
        """
        
    def test_equilateral_triangle(self):
        "Caso de teste para um triângulo válido (Equilateral)"

        triangle = TriangleIdentifier(3, 3, 3)
        assert triangle.is_triangle() == True

    def test_isosceles_triangle(self):
        "Caso de teste para um triângulo válido (Isosceles)"
        triangle = TriangleIdentifier(4, 4, 5)
        assert triangle.is_triangle() == True

    def test_scalene_triangle(self):
        "Caso de teste para um triângulo válido (Scalene)"
        triangle = TriangleIdentifier(3, 4, 5)
        assert triangle.is_triangle() == True

    def test_invalid_triangle_sum(self):
        "Caso de teste para um triângulo inválido (Soma de dois lados não é maior que o terceiro)"
        triangle = TriangleIdentifier(5, 6, 11)
        assert triangle.is_triangle() == False

    def test_invalid_triangle_side(self):
        "Caso de teste para um triângulo inválido (Um lado é igual à soma dos outros dois lados)"
        triangle = TriangleIdentifier(3, 4, 7)
        assert triangle.is_triangle() == False

    def test_invalid_triangle_zero_side(self):
        "Caso de teste para um triângulo inválido (Pelo menos um lado é igual a zero)"
        triangle = TriangleIdentifier(0, 4, 5)
        assert triangle.is_triangle() == False

    def test_invalid_triangle_zero_sides(self):
        "Caso de teste para um triângulo inválido (Todos os lados são iguais a zero)"
        triangle = TriangleIdentifier(0, 0, 0)
        assert triangle.is_triangle() == False