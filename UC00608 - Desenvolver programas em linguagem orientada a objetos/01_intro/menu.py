import os

os.system("clear") # mac/linux
# os.system("cls") # win

while True:

    print("""######### Menu ########
# opt1              1 #
# opt2              2 #
# opt3              4 #
# opt4              5 #
#######################""")
    opt = input("opção: ")

    match opt:
        case "1":
            print('"opt1"')
        case "2":
            print('\'opt2\'')
        case "3":
            print('opt3')
        case "4":
            input("O progrma vai terminar")
            input("Digite qualquer pra continuar")
            break
        case _:
            print("Opção invalida!")

    input("Digite qualquer pra continuar")
    os.system("clear")  # mac/linux
    # os.system("cls") # win




#
# caso selecione opt1 -> mostrar na consola "opt1" (com aspas)
# caso selecione opt2 -> mostrar na consola 'opt2' (com aspas)
# caso selecione opt3 -> mostrar na consola opt3
# caso selecione opt4 -> terminar
# Outra opção indicar que a opção e invalida
#
# deve repetir até ser selecionada a opt4 -> sair
#