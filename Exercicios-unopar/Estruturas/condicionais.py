a = 15
b = 10

if a < b :
  print("A é menor do que B")
  r = a + b
  print(f"A soma de {a} + {b} é igual a {r}!")
else :
  print("A é maior do que B")
  r = a - b
  print(f"A subtração de {a} - {b} é igual a {r}!")

  

codigo_compra = 5111

if codigo_compra == 5222:
    print("Compra à vista.")
elif codigo_compra == 5333:
    print("Compra à prazo no boleto.")
elif codigo_compra == 5444:
    print("Compra à prazo no cartão.")
else:
    print("Código não cadastrado")