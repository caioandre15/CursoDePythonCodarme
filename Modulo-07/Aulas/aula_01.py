# Declarando uma função

# Parâmetro vs. argumento
# Parâmetro é a variavel declarada na função
# Argumento é o valor passado no parâmetro
# keywords arguments - São argumentos nomeados

def dar_boas_vindas(nome, sobrenome, nome_do_curso):
    print("Olá,", nome, sobrenome)
    print("Bem-vindo ao curso de", nome_do_curso)

dar_boas_vindas(nome="João", sobrenome="Silva", nome_do_curso="Python")

