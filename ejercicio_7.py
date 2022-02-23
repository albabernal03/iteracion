def convertir_entero_base(numero, base):
  conversion_cadena = '0123456789ABCDEF'

  if numero < base:
    return conversion_cadena[numero]
  else:
    return convertir_entero_base(numero, base)
numero =
base = 
resultado = convertir_entero_base(numero, base)
print(resultado)