
UserResponse = int(input("Insira um número: "))
Guessed = False

while Guessed == False:
    if UserResponse < 50:
        print("O número que escolheu é muito baixo.")
        UserResponse = int(input("Insira outro número: "))
    if UserResponse > 50:
        print(("O número que escolheu é muito alto."))
        UserResponse = int(input("Insira outro número: "))
    if UserResponse == 50:
        print(("Escolha certa do número"))
        Guessed = True

