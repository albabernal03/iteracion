resultado []
print("Escoge el número que desees editar")
numero=int(input())
print("Escoge la base en la que quieras converit el número elegido")
base=int(input())

def entero_cambiar_base(numero,base):
  if base > 36:
    print(numero)
  elif base < 2:
    print("Error, esta base no es válida")
  else:
    resultado.append(numero%base)
    if numero//base == 0:
      print(f"La solución es {resultado}")
    else:
      numero=numero//base
      edici(numero,base)
  edici(numero,base)