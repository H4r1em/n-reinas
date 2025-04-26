def resolver_n_reinas(n):
    soluciones = []

    def es_valida(posiciones, fila, columna):
        for i in range(fila):
            if posiciones[i] == columna or \
               abs(posiciones[i] - columna) == abs(i - fila):
                return False
        return True

    def resolver(fila, posiciones):
        if fila == n:
            soluciones.append(posiciones[:])
            return
        for columna in range(n):
            if es_valida(posiciones, fila, columna):
                posiciones[fila] = columna
                resolver(fila + 1, posiciones)

    resolver(0, [-1] * n)
    return [[c + 1 for c in solucion] for solucion in soluciones]