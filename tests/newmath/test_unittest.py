import unittest
from newmath.string import contar_vocales, multiplicacion_vocales, porcentaje_vocales
from newmath.factor import multiplicador_factor, factor_fibonacci

# Pruebas para String contar_vocales
class TestContarVocales(unittest.TestCase):
    def test_deberia_contar_vocales_en_una_frase(self):
        resultado = contar_vocales("Un murcielago")
        esperado = 6
        self.assertEqual(esperado, resultado)

    def test_deberia_contar_vocales_en_una_palabra(self):
        resultado = contar_vocales("elefante")
        esperado = 4
        self.assertEqual(esperado, resultado)

    def test_deberia_contar_vocales_en_una_frase_vacia(self):
        resultado = contar_vocales("")
        esperado = 0
        self.assertEqual(esperado, resultado)

    def test_deberia_contar_vocales_en_una_frase_con_numeros(self):
        resultado = contar_vocales("12345")
        esperado = 0
        self.assertEqual(esperado, resultado)

    def test_deberia_contar_vocales_en_una_frase_con_simbolos(self):
        resultado = contar_vocales("!@#$%")
        esperado = 0
        self.assertEqual(esperado, resultado)

    def test_deberia_contar_vocales_en_una_frase_con_mayusculas(self):
        resultado = contar_vocales("AEIOU")
        esperado = 5
        self.assertEqual(esperado, resultado)

    def test_deberia_contar_vocales_en_una_frase_con_minusculas(self):
        resultado = contar_vocales("aeiou")
        esperado = 5
        self.assertEqual(esperado, resultado)

    def test_deberia_contar_vocales_en_una_frase_con_espacios(self):
        resultado = contar_vocales("a e i o u")
        esperado = 5
        self.assertEqual(esperado, resultado)

    def test_deberia_contar_vocales_en_una_frase_con_vocales_y_consonantes(self):
        resultado = contar_vocales("murcielago")
        esperado = 5
        self.assertEqual(esperado, resultado)

# Pruebas para String multiplicacion_vocales
class TestMultiplicacionVocales(unittest.TestCase):
    def test_deberia_multiplicar_vocales_en_una_frase(self):
        resultado = multiplicacion_vocales("Un murcielago")
        esperado = 4
        self.assertEqual(esperado, resultado)

    def test_deberia_multiplicar_vocales_en_una_palabra(self):
        resultado = multiplicacion_vocales("elefante")
        esperado = 18
        self.assertEqual(esperado, resultado)

    def test_deberia_multiplicar_vocales_en_una_frase_vacia(self):
        resultado = multiplicacion_vocales("")
        esperado = 1
        self.assertEqual(esperado, resultado)

    def test_deberia_multiplicar_vocales_en_una_frase_con_numeros(self):
        resultado = multiplicacion_vocales("12345")
        esperado = 1
        self.assertEqual(esperado, resultado)

    def test_deberia_multiplicar_vocales_en_una_frase_con_simbolos(self):
        resultado = multiplicacion_vocales("!@#$%")
        esperado = 1
        self.assertEqual(esperado, resultado)

    def test_deberia_multiplicar_vocales_en_una_frase_con_mayusculas(self):
        resultado = multiplicacion_vocales("AEIOU")
        esperado = 120
        self.assertEqual(esperado, resultado)

    def test_deberia_multiplicar_vocales_en_una_frase_con_minusculas(self):
        resultado = multiplicacion_vocales("aeiou")
        esperado = 10
        self.assertEqual(esperado, resultado, "test_deberia_multiplicar_vocales")

    def test_deberia_multiplicar_vocales_en_una_frase_con_espacios(self):
        resultado = multiplicacion_vocales("a e i o u")
        esperado = 10
        self.assertEqual(esperado, resultado, "test_deberia_multiplicar_vocales")

    def test_deberia_multiplicar_vocales_en_una_frase_con_vocales_y_consonantes(self):
        resultado = multiplicacion_vocales("murcielago")
        esperado = 5
        self.assertEqual(esperado, resultado, "test_deberia_multiplicar_vocales")

    def test_deberia_multiplicar_vocales_en_una_frase_con_vocales_repetidas(self):
        resultado = multiplicacion_vocales("aeeiioouu")
        esperado = 15
        self.assertEqual(esperado, resultado, "test_deberia_multiplicar_vocales")

# Pruebas para Factorial
class TestMultiplicadorFactor(unittest.TestCase):
    def test_deberia_multiplicar_factor(self):
        resultado = multiplicador_factor(5, 1, 1)
        esperado = 14
        self.assertEqual(esperado, resultado)

    def test_deberia_multiplicar_factor_de_cero(self):
        resultado = multiplicador_factor(0, 1, 1)
        esperado = 4
        self.assertEqual(esperado, resultado, "test_deberia_multiplicar_factor")

    def test_deberia_multiplicar_factor_de_uno(self):
        resultado = multiplicador_factor(1, 1, 1)
        esperado = 6
        self.assertEqual(esperado, resultado)

    def test_deberia_multiplicar_factor_de_dos(self):
        resultado = multiplicador_factor(2, 1, 1)
        esperado = 8
        self.assertEqual(esperado, resultado, "test_deberia_multiplicar_factor")

    def test_deberia_multiplicar_factor_de_tres(self):
        resultado = multiplicador_factor(3, 1, 1)
        esperado = 10
        self.assertEqual(esperado, resultado, "test_deberia_multiplicar_factor")

    def test_deberia_multiplicar_factor_de_cuatro(self):
        resultado = multiplicador_factor(4, 1, 1)
        esperado = 12
        self.assertEqual(esperado, resultado, "test_deberia_multiplicar_factor")

    def test_deberia_multiplicar_factor_de_seis(self):
        resultado = multiplicador_factor(6, 1, 1)
        esperado = 16
        self.assertEqual(esperado, resultado, "test_deberia_multiplicar_factor")

    def test_deberia_multiplicar_factor_de_siete(self):
        resultado = multiplicador_factor(7, 1, 1)
        esperado = 18
        self.assertEqual(esperado, resultado, "test_deberia_multiplicar_factor")

    def test_deberia_multiplicar_factor_de_ocho(self):
        resultado = multiplicador_factor(8, 1, 1)
        esperado = 20
        self.assertEqual(esperado, resultado, "test_deberia_multiplicar_factor")

    def test_deberia_multiplicar_factor_de_nueve(self):
        resultado = multiplicador_factor(9, 1, 1)
        esperado = 22
        self.assertEqual(esperado, resultado, "test_deberia_multiplicar_factor")

# Pruebas para Factor Fibonacci
class TestFactorFibonacci(unittest.TestCase):
    def test_deberia_calcular_factor_fibonacci_con_valores_por_defecto(self):
        resultado = factor_fibonacci(5)
        esperado = 1.0
        self.assertEqual(esperado, resultado)

    def test_deberia_calcular_factor_fibonacci_con_valores_personalizados(self):
        resultado = factor_fibonacci(6, 2, 3)
        esperado = 5.67
        self.assertEqual(esperado, resultado, "test_deberia_calcular_factor_fibonacci_con_valores_personalizados")

    def test_deberia_calcular_factor_fibonacci_con_valores_personalizados_dos(self):
        resultado = factor_fibonacci(7, 1, 4)
        esperado = 8.57
        self.assertEqual(esperado, resultado, "test_deberia_calcular_factor_fibonacci_con_valores_personalizados_dos")

    def test_deberia_calcular_factor_fibonacci_con_valores_personalizados_tres(self):
        resultado = factor_fibonacci(8, 3, 5)
        esperado = 18.0
        self.assertEqual(esperado, resultado, "test_deberia_calcular_factor_fibonacci_con_valores_personalizados_tres")

    def test_deberia_calcular_factor_fibonacci_con_valores_personalizados_cuatro(self):
        resultado = factor_fibonacci(9, 2, 4)
        esperado = 19.78
        self.assertEqual(esperado, resultado, "test_deberia_calcular_factor_fibonacci_con_valores_personalizados_cuatro")

    def test_deberia_calcular_factor_fibonacci_con_valores_personalizados_cinco(self):
        resultado = factor_fibonacci(10, 1, 3)
        esperado = 19.9
        self.assertEqual(esperado, resultado, "test_deberia_calcular_factor_fibonacci_con_valores_personalizados_cinco")

    def test_deberia_calcular_factor_fibonacci_con_valores_personalizados_seis(self):
        resultado = factor_fibonacci(11, 2, 5)
        esperado = 50.45
        self.assertEqual(esperado, resultado, "test_deberia_calcular_factor_fibonacci_con_valores_personalizados_seis")

    def test_deberia_calcular_factor_fibonacci_con_valores_personalizados_siete(self):
        resultado = factor_fibonacci(12, 3, 6)
        esperado = 94.25
        self.assertEqual(esperado, resultado, "test_deberia_calcular_factor_fibonacci_con_valores_personalizados_siete")

    def test_deberia_calcular_factor_fibonacci_con_valores_personalizados_ocho(self):
        resultado = factor_fibonacci(13, 1, 2)
        esperado = 46.92
        self.assertEqual(esperado, resultado, "test_deberia_calcular_factor_fibonacci_con_valores_personalizados_ocho")

    def test_deberia_calcular_factor_fibonacci_con_valores_personalizados_nueve(self):
        resultado = factor_fibonacci(14, 2, 3)
        esperado = 114.07
        self.assertEqual(esperado, resultado, "test_deberia_calcular_factor_fibonacci_con_valores_personalizados_nueve")
    
# Pruebas para porcentaje_vocales
class TestPorcentajeVocales(unittest.TestCase):
        def test_deberia_calcular_porcentaje_vocales_en_una_frase(self):
            resultado = porcentaje_vocales("Hola, cómo estás?")
            esperado = 46.15
            self.assertEqual(esperado, resultado)

        def test_deberia_calcular_porcentaje_vocales_en_una_palabra(self):
            resultado = porcentaje_vocales("Python")
            esperado = 33.33
            self.assertEqual(esperado, resultado)

        def test_deberia_calcular_porcentaje_vocales_en_una_frase_vacia(self):
            resultado = porcentaje_vocales("")
            esperado = 0.0
            self.assertEqual(esperado, resultado)

        def test_deberia_calcular_porcentaje_vocales_en_una_frase_con_numeros(self):
            resultado = porcentaje_vocales("12345!")
            esperado = 0.0
            self.assertEqual(esperado, resultado)

        def test_deberia_calcular_porcentaje_vocales_en_una_frase_con_simbolos(self):
            resultado = porcentaje_vocales("!@#$%")
            esperado = 0.0
            self.assertEqual(esperado, resultado)

        def test_deberia_calcular_porcentaje_vocales_en_una_frase_con_mayusculas(self):
            resultado = porcentaje_vocales("AEIOU")
            esperado = 100.0
            self.assertEqual(esperado, resultado)

        def test_deberia_calcular_porcentaje_vocales_en_una_frase_con_minusculas(self):
            resultado = porcentaje_vocales("aeiou")
            esperado = 100.0
            self.assertEqual(esperado, resultado)

        def test_deberia_calcular_porcentaje_vocales_en_una_frase_con_espacios(self):
            resultado = porcentaje_vocales("a e i o u")
            esperado = 100.0
            self.assertEqual(esperado, resultado)

        def test_deberia_calcular_porcentaje_vocales_en_una_frase_con_vocales_y_consonantes(self):
            resultado = porcentaje_vocales("murcielago")
            esperado = 50.0
            self.assertEqual(esperado, resultado)

        def test_deberia_calcular_porcentaje_vocales_en_una_frase_con_vocales_acentuadas(self):
            resultado = porcentaje_vocales("áéíóú")
            esperado = 100.0
            self.assertEqual(esperado, resultado)

        def test_deberia_calcular_porcentaje_vocales_en_una_frase_con_vocales_y_consonantes_acentuadas(self):
            resultado = porcentaje_vocales("murciélago")
            esperado = 55.56
            self.assertEqual(esperado, resultado)

        def test_deberia_calcular_porcentaje_vocales_en_una_frase_con_mayusculas_y_minusculas(self):
            resultado = porcentaje_vocales("Murcielago AEIOU")
            esperado = 60.0
            self.assertEqual(esperado, resultado)

        def test_deberia_calcular_porcentaje_vocales_en_una_frase_con_caracteres_no_alfabeticos(self):
            resultado = porcentaje_vocales("123abc!@#")
            esperado = 33.33
            self.assertEqual(esperado, resultado)