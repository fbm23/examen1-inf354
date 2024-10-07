def knapsack(capacidad, pesos, valores, n):
    # Crear una tabla para almacenar los valores máximos
    K = [[0 for x in range(capacidad + 1)] for x in range(n + 1)]

    # Construir la tabla K[][] de abajo hacia arriba
    for i in range(n + 1):
        for w in range(capacidad + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif pesos[i-1] <= w:
                K[i][w] = max(valores[i-1] + K[i-1][w-pesos[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    # El valor máximo que se puede llevar en la mochila
    return K[n][capacidad]

# Ejemplo de uso
pesos = [10, 20, 30]
valores = [60, 100, 120]
capacidad = 50
n = len(pesos)

max_valor = knapsack(capacidad, pesos, valores, n)

print("El valor máximo que se puede llevar en la mochila es:", max_valor)
