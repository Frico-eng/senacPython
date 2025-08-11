import math
base_ret = float(input("Insira a base do retângulo: "))
altura_ret = float(input("Insira a altura do retângulo: "))

area_ret = base_ret*altura_ret
perimetro_ret = 2*(base_ret+altura_ret)
diagonal_ret = math.sqrt(base_ret**2+altura_ret**2)


print(f"\n\nEste retângulo tem àrea de {area_ret:.4f} m¹, perímetro de {perimetro_ret:.4f} m e diagonal de {diagonal_ret:.4f} m\n\n")