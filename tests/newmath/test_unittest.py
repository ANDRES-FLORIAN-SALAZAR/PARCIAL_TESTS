from tests.base import assert_equal
from newmath.string import contar_vocales,multiplicacion_vocales
from newmath.factor import multiplicador_factor, factor_fibonacci

# Pruebas para String contar_vocales

def test_deberia_contar_vocales_en_una_frase(self):
    resultado = contar_vocales("Un murcielago")
    esperado = 6
    assert_equal(esperado, resultado, "test_deberia_contar_vocales")

def test_deberia_contar_vocales_en_una_palabra(self):
    resultado = contar_vocales("elefante")
    esperado = 4
    assert_equal(esperado, resultado, "test_deberia_contar_vocales")

def test_deberia_contar_vocales_en_una_frase_vacia(self):
    resultado = contar_vocales("")
    esperado = 0
    assert_equal(esperado, resultado, "test_deberia_contar_vocales")

def test_deberia_contar_vocales_en_una_frase_con_numeros(self):
    resultado = contar_vocales("12345")
    esperado = 0
    assert_equal(esperado, resultado, "test_deberia_contar_vocales")

def test_deberia_contar_vocales_en_una_frase_con_simbolos(self):
    resultado = contar_vocales("!@#$%")
    esperado = 0
    assert_equal(esperado, resultado, "test_deberia_contar_vocales")

def test_deberia_contar_vocales_en_una_frase_con_mayusculas(self):
    resultado = contar_vocales("AEIOU")
    esperado = 5
    assert_equal(esperado, resultado, "test_deberia_contar_vocales")

def test_deberia_contar_vocales_en_una_frase_con_minusculas(self):
    resultado = contar_vocales("aeiou")
    esperado = 5
    assert_equal(esperado, resultado, "test_deberia_contar_vocales")

def test_deberia_contar_vocales_en_una_frase_con_espacios(self):
    resultado = contar_vocales("a e i o u")
    esperado = 5
    assert_equal(esperado, resultado, "test_deberia_contar_vocales")

def test_deberia_contar_vocales_en_una_frase_con_vocales_y_consonantes(self):
    resultado = contar_vocales("murcielago")
    esperado = 5
    assert_equal(esperado, resultado, "test_deberia_contar_vocales")

# Pruebas para multiplicacion_vocales

def test_deberia_multiplicar_vocales_en_una_frase(self):
    resultado = multiplicacion_vocales("Un murcielago")
    esperado = 7
    assert_equal(esperado, resultado, "test_deberia_multiplicar_vocales")

def test_deberia_multiplicar_vocales_en_una_palabra(self):
    resultado = multiplicacion_vocales("elefante")
    esperado = 5
    assert_equal(esperado, resultado, "test_deberia_multiplicar_vocales")

def test_deberia_multiplicar_vocales_en_una_frase_vacia(self):
    resultado = multiplicacion_vocales("")
    esperado = 0
    assert_equal(esperado, resultado, "test_deberia_multiplicar_vocales")

def test_deberia_multiplicar_vocales_en_una_frase_con_numeros(self):
    resultado = multiplicacion_vocales("12345")
    esperado = 0
    assert_equal(esperado, resultado, "test_deberia_multiplicar_vocales")

def test_deberia_multiplicar_vocales_en_una_frase_con_simbolos(self):
    resultado = multiplicacion_vocales("!@#$%")
    esperado = 0
    assert_equal(esperado, resultado, "test_deberia_multiplicar_vocales")

def test_deberia_multiplicar_vocales_en_una_frase_con_mayusculas(self):
    resultado = multiplicacion_vocales("AEIOU")
    esperado = 10
    assert_equal(esperado, resultado, "test_deberia_multiplicar_vocales")

def test_deberia_multiplicar_vocales_en_una_frase_con_minusculas(self):
    resultado = multiplicacion_vocales("aeiou")
    esperado = 10
    assert_equal(esperado, resultado, "test_deberia_multiplicar_vocales")

def test_deberia_multiplicar_vocales_en_una_frase_con_espacios(self):
    resultado = multiplicacion_vocales("a e i o u")
    esperado = 10
    assert_equal(esperado, resultado, "test_deberia_multiplicar_vocales")

def test_deberia_multiplicar_vocales_en_una_frase_con_vocales_y_consonantes(self):
    resultado = multiplicacion_vocales("murcielago")
    esperado = 6
    assert_equal(esperado, resultado, "test_deberia_multiplicar_vocales")

def test_deberia_multiplicar_vocales_en_una_frase_con_vocales_repetidas(self):
    resultado = multiplicacion_vocales("aeeiioouu")
    esperado = 18
    assert_equal(esperado, resultado, "test_deberia_multiplicar_vocales")
    
# Pruebas para multiplicar_factor

def test_deberia_multiplicar_factor(self):
    resultado = multiplicador_factor(5)
    esperado = 120
    assert_equal(esperado, resultado, "test_deberia_multiplicar_factor")

def test_deberia_multiplicar_factor_de_cero(self):
    resultado = multiplicador_factor(0)
    esperado = 1
    assert_equal(esperado, resultado, "test_deberia_multiplicar_factor")

def test_deberia_multiplicar_factor_de_uno(self):
    resultado = multiplicador_factor(1)
    esperado = 1
    assert_equal(esperado, resultado, "test_deberia_multiplicar_factor")

def test_deberia_multiplicar_factor_de_dos(self):
    resultado = multiplicador_factor(2)
    esperado = 2
    assert_equal(esperado, resultado, "test_deberia_multiplicar_factor")

def test_deberia_multiplicar_factor_de_tres(self):
    resultado = multiplicador_factor(3)
    esperado = 6
    assert_equal(esperado, resultado, "test_deberia_multiplicar_factor")

def test_deberia_multiplicar_factor_de_cuatro(self):
    resultado = multiplicador_factor(4)
    esperado = 24
    assert_equal(esperado, resultado, "test_deberia_multiplicar_factor")

def test_deberia_multiplicar_factor_de_seis(self):
    resultado = multiplicador_factor(6)
    esperado = 720
    assert_equal(esperado, resultado, "test_deberia_multiplicar_factor")

def test_deberia_multiplicar_factor_de_siete(self):
    resultado = multiplicador_factor(7)
    esperado = 5040
    assert_equal(esperado, resultado, "test_deberia_multiplicar_factor")

def test_deberia_multiplicar_factor_de_ocho(self):
    resultado = multiplicador_factor(8)
    esperado = 40320
    assert_equal(esperado, resultado, "test_deberia_multiplicar_factor")

def test_deberia_multiplicar_factor_de_nueve(self):
    resultado = multiplicador_factor(9)
    esperado = 362880
    assert_equal(esperado, resultado, "test_deberia_multiplicar_factor")

# Pruebas para factor_fibonacci
def test_deberia_calcular_factor_fibonacci_con_valores_por_defecto(self):
    resultado = factor_fibonacci(5)
    esperado = 1.0
    assert_equal(esperado, resultado, "test_deberia_calcular_factor_fibonacci_con_valores_por_defecto")

def test_deberia_calcular_factor_fibonacci_con_valores_personalizados(self):
    resultado = factor_fibonacci(6, 2, 3)
    esperado = 5.67
    assert_equal(esperado, resultado, "test_deberia_calcular_factor_fibonacci_con_valores_personalizados")

def test_deberia_calcular_factor_fibonacci_con_valores_personalizados_dos(self):
    resultado = factor_fibonacci(7, 1, 4)
    esperado = 4.86
    assert_equal(esperado, resultado, "test_deberia_calcular_factor_fibonacci_con_valores_personalizados_dos")

def test_deberia_calcular_factor_fibonacci_con_valores_personalizados_tres(self):
    resultado = factor_fibonacci(8, 3, 5)
    esperado = 4.25
    assert_equal(esperado, resultado, "test_deberia_calcular_factor_fibonacci_con_valores_personalizados_tres")

def test_deberia_calcular_factor_fibonacci_con_valores_personalizados_cuatro(self):
    resultado = factor_fibonacci(9, 2, 4)
    esperado = 5.11
    assert_equal(esperado, resultado, "test_deberia_calcular_factor_fibonacci_con_valores_personalizados_cuatro")

def test_deberia_calcular_factor_fibonacci_con_valores_personalizados_cinco(self):
    resultado = factor_fibonacci(10, 1, 3)
    esperado = 6.2
    assert_equal(esperado, resultado, "test_deberia_calcular_factor_fibonacci_con_valores_personalizados_cinco")

def test_deberia_calcular_factor_fibonacci_con_valores_personalizados_seis(self):
    resultado = factor_fibonacci(11, 2, 5)
    esperado = 5.5
    assert_equal(esperado, resultado, "test_deberia_calcular_factor_fibonacci_con_valores_personalizados_seis")

def test_deberia_calcular_factor_fibonacci_con_valores_personalizados_siete(self):
    resultado = factor_fibonacci(12, 3, 6)
    esperado = 4.75
    assert_equal(esperado, resultado, "test_deberia_calcular_factor_fibonacci_con_valores_personalizados_siete")

def test_deberia_calcular_factor_fibonacci_con_valores_personalizados_ocho(self):
    resultado = factor_fibonacci(13, 1, 2)
    esperado = 6.5
    assert_equal(esperado, resultado, "test_deberia_calcular_factor_fibonacci_con_valores_personalizados_ocho")

def test_deberia_calcular_factor_fibonacci_con_valores_personalizados_nueve(self):
    resultado = factor_fibonacci(14, 2, 3)
    esperado = 5.33
    assert_equal(esperado, resultado, "test_deberia_calcular_factor_fibonacci_con_valores_personalizados_nueve")
