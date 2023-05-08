def generar_triangulo_tartaglia(n):
    triangulo = [[1]]
    for i in range(1, n+1):
        fila = [1]
        for j in range(1, i):
            fila.append(triangulo[i-1][j-1] + triangulo[i-1][j])
        fila.append(1)
        triangulo.append(fila)
    return triangulo

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def coeficiente_binomial(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def probabilidad_lanzamiento_moneda(num_lanzamientos, num_caras):
    triangulo_tartaglia = generar_triangulo_tartaglia(num_lanzamientos)
    probabilidad = triangulo_tartaglia[num_lanzamientos][num_caras] / (2**num_lanzamientos)
    return probabilidad

num_lanzamientos = 5
print("Probabilidades de diferentes resultados al lanzar una moneda", num_lanzamientos, "veces:")
for num_caras in range(num_lanzamientos + 1):
    probabilidad = probabilidad_lanzamiento_moneda(num_lanzamientos, num_caras)
    print(f"{num_caras} cara(s) y {num_lanzamientos - num_caras} cruz(s): {probabilidad * 100:.2f}%")

