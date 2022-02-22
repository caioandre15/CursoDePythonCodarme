# Exer 01 - Criar função é primo?

def eh_primo(numero_inteiro):
    count = 0
    if(numero_inteiro <= 1):
        return False
    for i in range(2, numero_inteiro):
        if(numero_inteiro % i == 0):
            count += 1
    return count == 0
            
print(eh_primo(1))
print(eh_primo(2))
print(eh_primo(3))
