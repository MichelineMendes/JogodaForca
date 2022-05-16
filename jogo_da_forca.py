import random

# boas vindas
grupo= """
Grupo:
Gabriel Mendes Silva - email: 2022111510040@esp.edu.br
Micheline da Silveira Mendes - email: 2022111510028@iesp.edu.br
"""
print("=" * 50)
print(" " * 17, "JOGO DA FORCA", " " * 17)
print("=" * 50)
print("Seja bem vindo! E seja esperto para não ir para a forca! ;)")
print()
jogar = 1

print(grupo)

while (jogar == 1):
    print("\n>>>> Digite 0 a qualquer momento para sair <<<<")
    print("\nPara começar: escolha uma categoria ou digite 0 para sair.")

# escolher a categoria
    frutas = ["PITAIA", "KIWI", "JAMBO", "SAPOTI", "GRAVIOLA", "AMORA", "BURITI", "DAMASCO", "CARAMBOLA", "FIGO",
              "CEREJA", "JENIPAPO", "MIRTILO", "MORANGO", ]
    carros = ["FUSCA", "PALIO", "CHEVETTE", "GOL", "OPALA", "ONIX", "FIESTA", "GOLF", "BRASILIA", "CELTA", "EQUINOX",
              "SPIN", "CAMARO", "TAOS", "JETTA", "SAVEIRO", "PULSE", "CRONOS", "KICKS", ]
    cidades = ["AGUIAR", "ZABELE", "ALCANTIL", "APARECIDA", "AREIAL", "BORBOREMA", "CATINGUEIRA", "COXIXOLA", "EMAS",
               "ITATUBA", "JURU"]
    categoria  = str(input("Categorias: \n A  = Frutas \n B  = Modelos de carros  \n C = Cidades da Paraíba \n 0 = Sair\nDigite a "
                      "letra correspondente:  ")).upper()
    if categoria ==  "0":
        resposta = input("\nVocê deseja sair do jogo? S ou N: ").upper()
        if resposta == "S":
            jogar = int(input("Você quer recomeçar? Digite 1 para novo jogo ou qualquer numero para sair: "))
            if jogar == 1:
                continue
            elif jogar !=1:
                exit(0)
        elif respota == "N":
            continue

    if categoria == "A":
        secreta =str( random.choice(frutas)).upper()
        print("\nCategoria escolhida: >>>> FRUTAS <<<<")

    elif categoria == "B":
        secreta: str = random.choice(carros).upper()
        print("\nCategoria escolhida: >>>> CARROS <<<<")

    elif categoria == "C":
        secreta: str = random.choice(cidades).upper()
        print("\nCategoria escolhida: >>>> CIDADES DA PARAÍBA <<<<")

    else:
        print("\nEssa categoria não existe!")
        continue


        # variaveis
    traco: str = (" - ")
    letras_acertadas = []
    letras_erradas = []
    espacos = ["_"] * len(secreta)
    chances: int = 6
    acertos = 0
    vazio = """
                ##########§
                ##        §
                ##        §
                ##  
                ##   
                ##   
                ##    
                ##     
                ##      
                ##   
                ##   
                ##  
                ##     
                ##     
                ##    
                ##  
                ##
                """

    cabeca = """
                ##########§
                ##        §
                ##      __§_
                ##     |    | 
                ##  *************
                ##   *  @ @   *
                ##   *   /    * 
                ##    *  &   *
                ##     *****
                ##      §§
                ##
                ##
                ##
                ##
                ##
                ##
                ##
                
                
                """

    tronco = """
                ##########§
                ##      __§_
                ##     |    | 
                ##  *************
                ##   *  @ @   *
                ##   *   /    * 
                #     *  &   *
                ##     *****
                ##      §§
                ##   #########
                ##      $$$    
                ##      $$$    
                ##      $$$
                ##     #####
                ##        
                ##    
                ##       
                """
    braco_d = """
                ##########§
                ##        §
                ##      __§_
                ##     |    | 
                ##  *************
                ##   *  @ @   *
                ##   *   /    * 
                #     *  &   *
                ##     *****
                ##      §§
                ##   #########
                ##   *  $$$   
                ##  *   $$$    
                ##      $$$
                ##     #####
                ##     
                ##    
                ##
                """

    braco_e = """     
                ##########§
                ##        §
                ##      __§_
                ##     |    | 
                ##  *************
                ##   *  @ @   *
                ##   *   /    * 
                #     *  &   *
                ##     *****
                ##      §§
                ##   #########
                ##   *  $$$   * 
                ##  *   $$$    *
                ##      $$$
                ##     #####
                ##     
                ##
                ##   
                ##      
                """

    perna_d = """
                ##########§
                ##        §
                ##      __§_
                ##     |    | 
                ##  *************
                ##   *  @ @   *
                ##   *   /    * 
                #     *  &   *
                ##     *****
                ##      §§
                ##   #########
                ##   *  $$$   * 
                ##  *   $$$    *
                ##      $$$
                ##     #####
                ##     *    
                ##    *      
                ##   *        
                ##
                """

    perna_e = """
                ##########§
                ##        §
                ##      __§_
                ##     |    | 
                ##  *************
                ##   *  @ @   *
                ##   *   /    * 
                #     *  &   *
                ##     *****
                ##      §§
                ##   #########
                ##   *  $$$   * 
                ##  *   $$$    *
                ##      $$$
                ##     #####
                ##     *    *
                ##    *      *
                ##   *        *
                ##
                """

    partes_boneco = [perna_e, perna_d, braco_e, braco_d, tronco, cabeca, vazio]

    # Jogando
    print("\nA palavra tem ", len(secreta), "letras\n\n")

    while chances > 0 and acertos != len(secreta):
        print(*espacos)
        print("Letras informadas: \nCorretas= ", end=" ")
        print(*letras_acertadas, sep=",")
        print("Erradas= ", end=" ")
        print(*letras_erradas, sep=",")

        letra: str = input("\nDigite uma letra: ").upper()
        if len(letra) >= 2:
            print("Só é permitido uma letra de cada vez.")
            continue
        if letra == "0":
            resposta = input("\nVocê deseja sair do jogo? S ou N: ").upper()
            if resposta == "S":
                exit(0)
            else:
                continue

        if letra in letras_erradas + letras_acertadas or not letra.isalpha():
            print("Letra ja informada ou não compõe o alfabeto. Tente outra!\n")
            continue

        if letra in secreta:
            print("Voce acertou a letra!")
            for i in range(len(secreta)):
                if letra == secreta[i]:
                    espacos[i] = letra
            acertos = acertos + secreta.count(letra)
            letras_acertadas.append(letra)
        else:
            chances = chances - 1
            letras_erradas.append(letra)
            print("\nEssa letra não pertence a palavra secreta. Você tem agora ", chances, "chances")
            print(partes_boneco[chances])

    # terminando o jogo
    if chances == 0:
        print("Sua chances acabaram. Você foi para forca!\nA palavra secreta era: ", secreta)
    else:
        print("Você descobriu a palavra secreta", secreta, " e escapou da forca!")

    #voltar a jogar
    jogar = int(input("\nVocê deseja jogar novamente? Digite 1 para novo jogo ou qualquer outro caracter para sair:  "))

else:
    exit(0)

