nome = "wIDson"

print(nome.upper()) # Maiusculo
print(nome.lower()) # Minusculo
print(nome.title()) # Título

text = "  Olá mundo!    "

print(text + ".")
print(text.strip() + ".") # Corta os todos os espaços
print(text.lstrip() + ".") # Corta os espaços da esquerda
print(text.rstrip() + ".") # Corta os espaços da direita

menu = "Python"

print("####" + menu + "####")
print(menu.center(14)) # Adiciona caracteres para centralizar o texto
print(menu.center(14, "#")) # Adiciona caracteres para centralizar o texto
print("P-y-t-h-o-n")
print("-".join(menu)) # Adiciona caracteres a cada letra