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
    while True:
        for client in clients:
            print(Fore.GREEN + f"Saldo: {client.balance}" + Style.RESET_ALL)
            print("1 - Depósito")
            print("2 - Transferência")
            choices = input("Escolha:")
            if choices == "1":
                deposit()
                continue
            elif choices == "2":
                transfer()
                continue
            else:
                print(Fore.RED + "Opção inválida. Por favor, escolha 1 ou 2." + Style.RESET_ALL)
                continue
        
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

def deposit():
    for client in clients:
        deposit_value = float(input("Quanto você quer depositar?"))

        client.balance += deposit_value

        # print(Fore.GREEN + f"Saldo: {client.balance}" + Style.RESET_ALL)
        
def transfer():
    for client in clients:
        transfer_value = float(input(Fore.RED + "Quanto você quer transferir?"))

        client.balance -= transfer_value

        # print(Fore.GREEN + f"Saldo: {client.balance}" + Style.RESET_ALL)