desafio = "1 - Desafio Classificador de nível de Herói"
print(desafio)

while True:
    print()
    nome_heroi = input("Insira o nome do Herói: ")
    xp = int(input("Insira a quantidade de (XP) do herói: "))
    print()
    if xp <= 1000:
        print(f"O Herói de nome {nome_heroi} está no nível {xp} de Ferro")
    elif 1001 <= xp <= 2000:
        print(f"O Herói de nome {nome_heroi} está no nível {xp} de Bronze")
    elif 2001 <= xp <= 5000:
        print(f"O Herói de nome {nome_heroi} está no nível {xp} de Prata")
    elif 5001 <= xp <= 7000:
        print(f"O Herói de nome {nome_heroi} está no nível {xp} de Ouro")
    elif 7001 <= xp <= 8000:
        print(f"O Herói de nome {nome_heroi} está no nível {xp} de Platina")
    elif 8001 <= xp <= 9000:
        print(f"O Herói de nome {nome_heroi} está no nível {xp} de Ascendente") 
    elif 9001 <= xp <= 10000:
        print(f"O Herói de nome {nome_heroi} está no nível {xp} de Imortal")
    else:
         print(f"O Herói de nome {nome_heroi} está no nível {xp} de Radiante")

    continuar = input("Deseja continuar? (s/n): ")
    if continuar != 's':
        break