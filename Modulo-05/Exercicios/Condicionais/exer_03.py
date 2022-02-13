# Exer. 03 Autenticação

usuario = "user01"
senha = "123"

nome_usuario = input("Digite o nome de usuário: ")
senha_usuario = input("Digite a senha: ")

if nome_usuario  == usuario and senha_usuario == senha:
    print("Autenticação foi bem-sucedida!")
elif nome_usuario != usuario:
    print("O nome de usuário não existe!")
elif senha_usuario != senha:
    print("Senha incorreta!")

