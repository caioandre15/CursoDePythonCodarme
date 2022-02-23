# Exer. 06 - Fatorial

def calcula_fatorial(n):
    if n < 0:
        print("Não existe fatorial negativo")
    elif n == 0:
        return 1
    else:
        fatorial = 1
        while n > 1:
            fatorial *= n
            n -= 1
        return fatorial    

print(calcula_fatorial(5))

