#Gerador e arquivamento de senhas básico.
#Secrets and string usados para o gerador de senhas aleatórios.
import pyperclip, secrets, string

f = open("pw.final.txt", "a+")
comando = ''
while comando != 'adicionar' or comando != 'senha' or comando !='sair':
    f = open("pw.final.txt", "a+")
    comando = input("Para adicionar uma nova senha digite adicionar, para recuperar uma senha digite senha. Para sair digite sair. ")
    comando = comando.lower()
    if comando == 'adicionar':
        # O dict para adicionar ao .txt precisa ser criado aqui para não ficar repetindo sua adição ao arquivo.
        PASSWORDS = {}
        parametro = input("Qual será o novo parâmetro? ")
        gerar_senha = ''
        # Gerador de senha aleatórias, se o usuário quiser.
        while gerar_senha != 's' or gerar_senha != 'n':
            gerar_senha = input("Você quer gerar uma nova senha? (s/n). ")
            gerar_senha = gerar_senha.lower()
            if gerar_senha == 's':
                alphabet = string.ascii_letters + string.digits
                tamanho_senha = int(input("Qual o tamanho da senha? "))
                valor = ''.join(secrets.choice(alphabet) for i in range(tamanho_senha))
            elif gerar_senha == 'n':
                valor = input("Qual será a senha? ")
            break
        # Update o dict.
        PASSWORDS.update({parametro: valor})
        # Com esse for abaixo conseguimos salvar as novas senhas no arquivo pw.txt
        for key, value in PASSWORDS.items():
            # Lembrando que no .txt o cursor precisa estar em uma linha nova.
            f.write(str(key) + ": " + str(value) + "\n")
        f.close()
            # f.close aqui para conseguir adicionar a nova senha e manter o arquivo aberto.
    elif comando == 'senha':
        # Com essa linha de comando abaixo conseguimos puxar denovo o valor da key, assim copiando a senha do usuário.
        key = input("Qual senha deseja? ")
        with open('pw.final.txt', 'r') as file:
            for line in file:
                if key in line:
                    # Variável senha será dividida ficando de {login: senha} para ('login': 'senha').
                    # E depois pegará o [-1] que é o último elemento da lista com o strip.
                    # Para assim copiar a senha com pyperclip e devolve-la para o usuário.
                    senha = line.split(':')[-1].strip()
                    pyperclip.copy(senha)
                    print("Password adicionada de " + key + " para seu CRTL+V")
                    # Com isso copiamos a senha denovo para o usuário.
                    # Problema se tiver duas keys praticamente com o mesmo nome, i.g. email1 email2.
    elif comando == 'sair':
        break
    else:
        print("Comando não entendido, tente novamente.")

f.close()