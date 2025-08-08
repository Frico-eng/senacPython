import math
base_ret = float(input("Insira a base do retângulo:"))
altura_ret = float(input("Insira a altura do retângulo:"))

area_ret = base_ret*altura_ret
perimetro_ret = 2*(base_ret+altura_ret)
diagonal_ret = math.sqrt(base_ret**2+altura_ret**2)

print(f"Área do retângulo: {area_ret:.2f}")
print(f"Perímetro do retângulo: {perimetro_ret:.2f}")
print(f"Diagonal do retângulo: {diagonal_ret:.2f}")