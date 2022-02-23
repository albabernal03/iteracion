
# Algoritmo euclídeo solo con sumas o restas
def euclides_mcd(n, m)
    if m == 0:
       return 0,1,0
    u0 = 1
    u1 = 0
    v0 = 0
    v1 = 1
    while m != 0:
      q = n//m
      r = n - m * q
      u = u0 - q * u1
      v = v0 - q * v1
      # Actualizamos n,m
      a = b
      b = r
      # Actualizamos para la siguiente operación
      u0 = u1 
      u1 = u
      v0 = v1
      v1 = v
    return a, u0, v0

