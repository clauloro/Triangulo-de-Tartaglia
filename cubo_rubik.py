def generate_tartaglia_triangle(n):
    triangle = [[1]]

    for i in range(1, n):
        row = [1]

        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        row.append(1)
        triangle.append(row)

    return triangle


def binomial_coefficient(triangle, n, k):
    if n < k:
        raise ValueError("n must be greater or equal to k")

    return triangle[n][k]


def main():
    # Generar el triángulo de Tartaglia de 10 filas
    tartaglia_triangle = generate_tartaglia_triangle(10)

    # Imprimir el triángulo de Tartaglia
    for row in tartaglia_triangle:
        print(row)

    # Calcular e imprimir algunos coeficientes binomiales utilizando el triángulo de Tartaglia
    print("C(5, 2) =", binomial_coefficient(tartaglia_triangle, 5, 2))
    print("C(7, 3) =", binomial_coefficient(tartaglia_triangle, 7, 3))
    print("C(9, 4) =", binomial_coefficient(tartaglia_triangle, 9, 4))


if __name__ == "__main__":
    main()


