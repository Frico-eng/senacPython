#small script to calculate quare roots using newtons method

def raiz(numero):
    tolerancia = 1e-12
    if(numero<0):
        print("Este código não suporta números negativos")
    elif(numero==0):
        return 0
    elif(numero>0):
        chute = numero/2
        while(abs(chute*chute-numero)>=tolerancia):
            chute = (chute+(numero/chute))/2
        return chute

print(raiz(400))