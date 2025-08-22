
total_compra = int(input("Ingrese el total de la compra:  "))
valor_pagado = int(input("Ingrese el valor pagado por el cliente:  "))

cambio = valor_pagado - total_compra
cambio_inicial = cambio


if cambio % 500 == 0 and valor_pagado < total_compra:
  b50000 = cambio // 50000
  cambio = cambio % 50000

  b20000 = cambio // 20000
  cambio = cambio % 20000

  b10000 = cambio // 10000
  cambio = cambio % 10000

  b5000 = cambio // 5000
  cambio = cambio % 5000

  b2000 = cambio // 2000
  cambio = cambio % 2000

  b1000 = cambio // 1000
  cambio = cambio % 1000

  m500 = cambio // 500
  cambio = cambio % 500


  print("Cambio entregado:")
  if b50000 > 0:
      print(f"{b50000} billete(s) de 50.000")
  if b20000 > 0:
      print(f"{b20000} billete(s) de 20.000")
  if b10000 > 0:
      print(f"{b10000} billete(s) de 10.000")
  if b5000 > 0:
      print(f"{b5000} billete(s) de 5.000")
  if b2000 > 0:
      print(f"{b2000} billete(s) de 2.000")
  if b1000 > 0:
      print(f"{b1000} billete(s) de 1.000")
  if m500 > 0:
      print(f"{m500} moneda(s) de 500")
  print(f"Para una devuelta total de: {cambio_inicial:,d}")

else:
  print("Error: No se puede calcular el cambio correctamente. El total pagado no es suficiente o el cambio a devolver no es múltiplo de 500")
