
    
def obter_informacoes():
    while True:
        nome = input("Digita o nome ae: ")
        # len serve para sinalizar quantos digitos devem ser contabilizados
        if len(nome) <= 8:
            break 
        # se o if estiver correto passar pra próoxima pergunta sem exibir a mensagem do elif
        if len(nome) > 15:
            print("Acha que essa porra é redação?")

        elif len(nome) >= 8:
            print ("São apenas 8 dígitos")

    while True:
        try:
            idade = int(input("Digite sua idade: "))
            break
        except ValueError:
                print("Preciso de números")

    return nome, idade

while True:
    nome, idade = obter_informacoes()

    print("Agora confirme")
    print(f"Seu nome é {nome}, com {idade} anos de atividades no mundo do crime?")

    while True:
        confirmacao = input("As informações que tu deu estão corretas? (y/n): ").strip().lower()
        
        if confirmacao == 'y':
            print("Que bom, eu não me importo")
            break
        elif confirmacao == 'n':
            print("E a culpa é minha se tu responde errado?")
            break
        else:
            print("Por favor, responda apenas 'y' ou 'n'.")
            continue
    if confirmacao == 'y':
        break
    elif confirmacao =='n':
        continue

print("Agora vamos escolher uma senha")


#padrao de solicitação de criação de senha com caracteres especiais, números, letras maiúsculas e minusculas. !123Abcde

def criar_senha():
    import string

    while True:
        senha = input("Digite sua senha: ")

        if len(senha) < 8:
            print("Senha pequena e fraca, precisa ter pelo menos 8 caracteres.")
            continue

        if not any(c.islower() for c in senha):
            print("Senha deve conter pelo menos uma letra minúscula.")
            continue

        if not any(c.isupper() for c in senha):
            print("Senha deve conter pelo menos uma letra maiúscula.")
            continue

        if not any(c.isdigit() for c in senha):
            print("Senha deve conter pelo menos um número.")
            continue

        if not any(c in string.punctuation for c in senha):
            print("Senha deve conter pelo menos um caractere especial.")
            continue
        
        if senha == (criar_senha):
            break 
        
        return senha

    nome = obter_informacoes
    senha = criar_senha

    print(f"Posso cadastrar o nome: {nome} e a senha: {senha} ?")



