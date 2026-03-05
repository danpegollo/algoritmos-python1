import math
tamanho = int(input("Qual o tamanho de área de tinta a ser pintada em metros quadrados? "))
cobertura = tamanho/3 
latas = cobertura/18
latasInteira = math.ceil(latas)
preco = 80 * latasInteira
precoFormatado = f"{preco:.2f}"
print("São necessários utilizar ", latasInteira, "latas e o preço em reais a ser pago é de R$", precoFormatado)
