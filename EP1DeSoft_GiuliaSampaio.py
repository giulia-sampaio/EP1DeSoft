# Importando a biblioteca ramdom:
import random 

# Declarando a quantidade de fichas inicial do usuário:
fichas = 500

# Iniciando o jogo:
jogando = True

while jogando == True:

    pass_line_bet = False
    point = False

    resp = input("Apostar ou sair do jogo? ")

    if resp == "sair":
        print("Até a próxima!")
        break

    elif fichas == 0:
        print("Você não tem mais fichas para continuar! =(")
        break

    else:
        print("Começando a fase Come Out")
        print("Você tem {0} fichas".format(fichas))
        valor = int(input("Quanto você quer apostar? "))

        if valor > fichas:
            print("Suas fichas não são suficientes para essa aposta!")
            break

        print("As apostas que você pode fazer são: Pass Line Bet(1), Field(2), Any Craps(3) ou Twelve(4)")
        aposta = int(input("Qual modalidade de aposta você quer? "))
     
        # Iniciando aposta Pass Line Bet
        if aposta == 1:
            pass_line_bet = True

        while pass_line_bet == True:

            # Jogando os dados:
            dado = random.randint(2,12)
            print("Você tirou {0}".format(dado))

            if dado == 2 or dado == 3 or dado == 12:
                fichas = fichas - valor
                print("Você perdeu! Agora você tem {0} fichas =(".format(fichas))
                pass_line_bet = False

            elif dado == 7 or dado == 11:
                fichas = fichas + valor
                print("Você ganhou! Agora você tem {0} fichas =)".format(fichas))
                pass_line_bet = False

            # Iniciando fase Point:
            else:
                point = True
                print("Você passou para a fase Point!")

                while point == True:

                    # Jogando um segundo dado:
                    dado2 = random.randint(2,12)
                    print("Você tirou {0}".format(dado2))

                    if dado == dado2:
                        fichas = fichas + valor
                        print("Você ganhou! Agora você tem {0} fichas =)".format(fichas))
                        point = False
                        pass_line_bet = False

                    elif dado2 == 7:
                        fichas = fichas - valor
                        print("Você perdeu! Agora você tem {0} fichas =(".format(fichas))
                        point = False
                        pass_line_bet = False

                    else:
                        print("Os dados serão jogados novamente...")

        # Iniciando aposta Field:
        if aposta == 2:

            # Jogando os dados:
            dado = random.randint(2,12)
            print("Você tirou {0}".format(dado))

            if dado == 5 or dado == 6 or dado == 7 or dado == 8:
                fichas = fichas - valor
                print("Você perdeu! Agora você tem {0} fichas =(".format(fichas))

            elif dado == 3 or dado == 4 or dado == 9 or dado == 10 or dado == 11:
                fichas = fichas + valor
                print("Você ganhou! Agora você tem {0} =)".format(fichas))

            elif dado == 2:
                fichas = fichas + 2*valor
                print("Você ganhou! Agora você tem {0} =)".format(fichas))

            else:
                fichas = valor + 3*valor

        # Iniciando aposta Any Craps:
        if aposta == 3:

            # Jogando os dados:
            dado = random.randint(2,12)
            print("Você tirou {0}".format(dado))

            if dado == 2 or dado == 3 or dado == 12:
                fichas = fichas + 7*valor
                print("Você ganhou! Agora você tem {0} =)".format(fichas))

            else:
                fichas = fichas - valor
                print("Você perdeu! Agora você tem {0} fichas =(".format(fichas))

        # Iniciando aposta Twelve:
        if aposta == 4:

            # Jogando os dados:
            dado = random.randint(2,12)
            print("Você tirou {0}".format(dado))

            if dado == 12:
                fichas = fichas + 30*valor
                print("Você ganhou! Agora você tem {0} =)".format(fichas))

            else:
                fichas = fichas - valor
                print("Você perdeu! Agora você tem {0} fichas =(".format(fichas))