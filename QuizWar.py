batalha1 = [
    ['Batalha de Moscou', 'Batalha de Berlim', 'Batalha de Monte Cassino']
]

campanha1 = [
    ['Campanha Italiana', 'Campanha Alemã', 'Campanha Japonesa']
]

ofensiva1 = [
    ['Ofensiva da primavera italiana', 'Ofensiva do Saare', 'Ofensiva de Ostrogozhsk–Rossosh']
]

batalha2 = [
    ['Batalha da França', 'Batalha de Kursk', 'Batalha de Stalingrado']
]

batalhabr = [
    ['Batalha de Monte Castello', 'Batalha de Castelnuovo', 'Batalha de Montese']
]

batalhaGM = [
    ['Batalha de Somme', 'Batalha de Verdun', 'Batalha de Varsóvia']
]

batalhaGM2 = [
    ['Batalha de Somme', 'Batalha de Verdun', 'Ofensiva dos 100 dias']
]

Nacoes = [
    ['Estados Unidos', 'Imperio Britânico', 'Imperio Alemão']
]

gases = [
    ['Gás Mostarda', 'Gás Fosgênio', 'Gás Cloro']
]

artilharia = [
    ['Schewerer Gustav', 'Canhão de Paris', 'Canhão do Tsar']
]

print(ofensiva1)
pergunta1 = str(input("Como foi chamada a ofensiva em resposta da invasão alemã na polônia na 2ª Guerra Mundial? \n"))
while (pergunta1 != "Ofensiva do Saare"):
    print("Errou! Tente de novo!")
    pergunta1 = str(input("Como foi chamada a ofensiva em resposta da invasão alemã na polônia na 2ª Guerra Mundial? \n"))

if pergunta1 == "Ofensiva do Saare":
    print("Pergunta 2: \n")
    print(batalha1)
    pergunta2 = str(input("Qual foi a batalha que marcou o fim do 3º Reich? \n"))

while (pergunta2 != "Batalha de Berlim"):
    print("Errou! Tente de novo!")
    pergunta2 = str(input("Qual foi a batalha que marcou o fim do 3º Reich? \n"))
    
if pergunta2 == "Batalha de Berlim":
    print("Pergunta 3: \n")
    print(batalha2)
    pergunta3 = str(input("Qual foi a batalha mais sangrenta da 2ª Guerra? \n"))

while (pergunta3 != "Batalha de Stalingrado"):
    print("Errou! Tente de novo!")
    pergunta3 = str(input("Qual foi a batalha mais sangrenta da 2ª Guerra? \n"))
    
if pergunta3 == "Batalha de Stalingrado":
    print("Pergunta 4: \n")
    print(campanha1)
    pergunta4 = str(input("Em qual campanha em que os pracinhas brasileiros participaram? \n"))

while (pergunta4 != "Campanha Italiana"):
    print("Errou! Tente de novo!")
    pergunta4 = str(input("Em qual campanha em que os pracinhas brasileiros participaram? \n"))
    
if pergunta4 == "Campanha Italiana":
    print("Pergunta 5: \n")
    print(batalhabr)
    pergunta5 = str(input("Qual foi a batalha mais imporante que brasileiros foram envolvidos? \n"))

while (pergunta5 != "Batalha de Monte Castello"):
    print("Errou! Tente de novo!")
    pergunta5 = str(input("Qual foi a batalha mais imporante que brasileiros foram envolvidos? \n"))
    
if pergunta5 == "Batalha de Monte Castello":
    print("Pergunta 6: \n")
    print(batalhaGM)
    pergunta6 = str(input("Qual foi a batalha mais longa da primeira guerra mundial? \n"))

while (pergunta6 != "Batalha de Verdun"):
    print("Errou! Tente de novo!")
    pergunta6 = str(input("Qual foi a batalha mais longa da primeira guerra mundial? \n"))    
    
if pergunta6 == "Batalha de Verdun":
    print("Pergunta 7: \n")
    print(batalhaGM2)
    pergunta7 = str(input("Qual foi a batalha que introduziu tanques de guerra à batalha? \n"))

    while (pergunta7 != "Batalha de Somme"):
        print("Errou! Tente de novo!")
        pergunta7 = str(input("Qual foi a batalha que introduziu tanques de guerra à batalha? \n"))

if pergunta7 == "Batalha de Somme":
    print("Pergunta 8: \n")
    print(Nacoes)
    pergunta8 = str(input("Qual foi a nação que começou a usar o Gás Toxico nas batalhas da primeira guerra mundial? \n"))

while (pergunta8 != "Imperio Alemão"):
    print("Errou! Tente de novo!")
    pergunta8 = str(input("Qual foi a nação que começou a usar o Gás Toxico nas batalhas da primeira guerra mundial? \n"))
    
if pergunta8 == "Imperio Alemão":
    print("Pergunta 9: \n")
    print(gases)
    pergunta9 = str(input("Qual o primeiro gás toxico usado pelos alemães? \n"))

while (pergunta9 != "Gás Cloro"):
    print("Errou! Tente de novo!")
    pergunta9 = str(input("Qual o primeiro gás toxico usado pelos alemães? \n"))
    
if pergunta9 == "Gás Cloro":
    print("Pergunta 10: \n")
    print(artilharia)
    pergunta10 = str(input("Qual foi o nome da maior peça de artilharia feita? \n"))

while (pergunta10 != "Schewerer Gustav"):
    print("Errou! Tente de novo!")
    pergunta10 = str(input("Qual foi o nome da maior peça de artilharia feita? \n"))
    
if pergunta10 == "Schewerer Gustav":
    print("Parabens, terminou o Quiz!")