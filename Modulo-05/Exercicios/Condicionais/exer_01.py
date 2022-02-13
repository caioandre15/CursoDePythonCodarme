# Exer. 01 "FizzBuzz"

numeroInteiro = int(input("Digite um número inteiro: "))

if numeroInteiro % 3 == 0 and numeroInteiro % 5 == 0:
    print("FizzBuzz") 
elif numeroInteiro % 3 == 0:
    print("Fizz")
elif numeroInteiro % 5 == 0:
    print("Buzz")
