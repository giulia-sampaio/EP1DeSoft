import random 

jogando = True

fichas = 500

while jogando == True:

    pass_line_bet = False
    point = False
    field = False
    any_craps = False
    twelve = False

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

        print("As apostas que você pode fazer são: Pass Line Bet, Field, Any Craps ou Twelve")
        print("Observação: digite o nome da aposta com letras minusculas")
        aposta = input("Qual modalidade de aposta você quer? ")
     
        if aposta == "pass line bet":
            pass_line_bet = True

        while pass_line_bet == True:

            dado = random.randint(2,12)
            print("Você tirou {0}".format(dado))

            if dado == 2 or dado == 3 or dado == 12:
                fichas = fichas - valor
                print("Você perdeu! Agora você tem {0} fichas =(".format(fichas))
                pass_line_bet = False
                point = False

            if dado == 7 or dado == 11:
                fichas = fichas + valor
                print("Você ganhou! Agora você tem {0} fichas =)".format(fichas))
                pass_line_bet = False
                point = False

            else:
                point = True
                print("Você passou para a fase Point!")

                while point == True:

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

        if aposta == "field":
            field = True

        while field == True:

            dado = random.randint(2,12)
            print("Você tirou {0}".format(dado))

            if dado == 5 or dado == 6 or dado == 7 or dado == 8:
                fichas = fichas - valor
                print("Você perdeu! Agora você tem {0} fichas =(".format(fichas))
                field = False

            if dado == 3 or dado == 4 or dado == 9 or dado == 10 or dado == 11:
                fichas = fichas + valor
                print("Você ganhou! Agora você tem {0} =)".format(fichas))
                field = False

            elif dado == 2:
                fichas = fichas + 2*valor
                print("Você ganhou! Agora você tem {0} =)".format(fichas))
                field = False

            else:
                fichas = valor + 3*valor
                print("Você ganhou! Agora você tem {0} =)".format(fichas))
                field = False 

        if aposta == "any craps":
            any_craps = True
               
        while any_craps == True:

            dado = random.randint(2,12)
            print("Você tirou {0}".format(dado))

            if dado == 2 or dado == 3 or dado == 12:
                fichas = fichas + 7*valor
                print("Você ganhou! Agora você tem {0} =)".format(fichas))
                any_craps = False

            else:
                fichas = fichas - valor
                print("Você perdeu! Agora você tem {0} fichas =(".format(fichas))
                any_craps = False 

        if aposta == "twelve":
            twelve = True 

        while twelve == True:

            dado = random.randint(2,12)
            print("Você tirou {0}".format(dado))

            if dado == 12:
                fichas = fichas + 30*valor
                print("Você ganhou! Agora você tem {0} =)".format(fichas))
                twelve = False

            else:
                fichas = fichas - valor
                print("Você perdeu! Agora você tem {0} fichas =(".format(fichas))
                twelve = False