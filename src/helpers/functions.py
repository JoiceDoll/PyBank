from colorama import just_fix_windows_console, Fore, Style
just_fix_windows_console()

class Client:
    def __init__(self, name, email, password, balance):
        self.name = name
        self.email = email
        self.password = password
        self.balance = balance

clients = []

def actions():
    print(Fore.GREEN + "Saldo" + Style.RESET_ALL)

def create_account():
    name = input("Digite seu nome:")
    email = input("Digite seu e-mail:")
    password = input("Digite uma senha:")
    confirm_password = input("Confirme a senha:")

    if password == confirm_password:
        balance = 0
        new_client = Client(name, email, password, balance)
        clients.append(new_client)
        print("Cadastro realizado com sucesso!")
        
        return True
    else:
        print(Fore.RED + "As senhas não são iguais." + Style.RESET_ALL)

def login():
    email = input("Digite seu e-mail:")
    password = input("Digite sua senha:")

    logged_clients = [client for client in clients if client.email == email and client.password == password]

    if logged_clients:
        print("Você está logado(a), Bem-vindo(a)!")
        for logged_client in logged_clients:
            print(f"Nome: {logged_client.name}, E-mail: {logged_client.email}, Balance:{logged_client.balance}")
            actions()
            return False
        
        
    else:
        print(Fore.RED + "E-mail ou senha incorretos!" + Style.RESET_ALL)
        print(logged_clients)




    