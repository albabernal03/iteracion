def euclides_mcd(n, m)
# El Máximo Común Divisor de 'n' y 'm'.
# Enteros naturales n ≥ 0 ; m ≥ 0 y n ≠ 0 y m ≠ 0
# Si n es inferior a m, se invierten
# Obtenemos el resto de la división
    while True:
        resto = n % m
        if resto == 0:
            return m
        # Si n es inferior a m, se invierten
        else:
            n = m
            m = resto
print euclides_mcd(n,m)