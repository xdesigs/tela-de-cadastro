
import re  
import string  
    
def obter_informacoes():
    while True:
        nome = input("Digita o nome ae: ")
        # len serve para sinalizar quantos digitos devem ser contabilizados
        if len(nome) <= 8:
            break 
        # se o if estiver correto passar pra próoxima pergunta sem exibir a mensagem do elif
        if len(nome) > 15:
            print("Acha que essa porra é redação?")

        elif len(nome) > 8:
            print ("São apenas 8 dígitos")

    while True:
        
        try:
            idade = int(input("Digite sua idade: "))
            
                     
            if idade > 99 or idade < 0:
                print ("Você precisa ter apenas 2 dígitos")
                continue
            
            break
            
        except ValueError:
            print("Preciso de números")
    

    return nome, idade

while True:
    nome, idade = obter_informacoes()

    print("Agora confirme")
    print(f"Seu nome é {nome}, com {idade} anos?")

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
    
# cadastro de email 

print("Agora vamos cadastrar seu email")

def validar_email(email):
   
    
    # Expressão regular para validar o formato do email
    padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(padrao, email)

def cadastrar_email():


    while True:
        email = input("Digite seu email:").strip()
        
        if not email:
            print("Precisamos cadastrar seu email")
            continue
        
        if validar_email(email):
            break
        
        else:
            print("Precisa ser um email válido")
        
    return email

email = cadastrar_email()    

print(f"Email: {email} cadastrado com sucesso")  

  
    
#padrao de solicitação de criação de senha com caracteres especiais, números, letras maiúsculas e minusculas. !123Abcde

print("Agora vamos escolher uma senha")

def criar_senha():
    

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
        break 
        
    return senha

senha = criar_senha()

while True:
        print(f"Posso cadastrar o nome: {nome} e a senha: {senha} ?")
        confirmacao = input("(y/n): ").strip().lower()

        if confirmacao == 'y':
            print("Usuário cadastrado com perrengue")
            break
        
        elif confirmacao =='n':
            print("O que você digitou de errado?")
            corrigir = str(input("Digite se foi o: NOME, IDADE ou SENHA ").strip().lower())
            
        if corrigir == str('nome'):
                nome, idade = obter_informacoes()
        
        elif corrigir == str('senha'):
                senha = criar_senha()
                
        elif corrigir != 'nome' or 'senha' or 'idade':
                print("Digitou errado, digite nome, idade ou senha")
                continue


