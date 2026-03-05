import math
raio = float(input("Coloque o valor de raio desejado: "))
area = math.pi * (raio ** 2)
perimetro = 2 * math.pi * raio
print(f"Sua área é de: {area:.2f} e o perímetro é: {perimetro:.2f}")