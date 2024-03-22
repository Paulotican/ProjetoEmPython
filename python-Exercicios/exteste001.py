# mini jogo teste;

poder = int(input("Digite seu poder de 1 a 10: \n"))
defesa = int(input("Digite sua defesa de 1 a 10: \n"))

boss1 = int(5)
boss_d = int(8)

boss2 = int(20)

print(f"Voce definiu seus status poder: {poder} defesa: {defesa} que a aventura comece: ")

acao1 = str(input(" Um boss acaba de aparecer e tenta te atacar: \t"))

print(" A luta comecou entao:")

if boss1 <= poder and boss_d <= defesa:
    print("Voce matou o boss")
    poder = poder + 10
    defesa = defesa + 5
else:
    print("Voce perdeu")
