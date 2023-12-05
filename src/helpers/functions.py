from colorama import just_fix_windows_console, Fore, Style
just_fix_windows_console()

class Client:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

def __str__(self):
        return f"Client(name={self.name}, email={self.email}, password={self.password})"

clients = []

def actions():
    print(Fore.GREEN + "Saldo" + Style.RESET_ALL)

def create_account():
    name = input("Digite seu nome:")
    email = input("Digite seu e-mail:")
    password = input("Digite uma senha:")
    confirm_password = input("Confirme a senha:")

    if password == confirm_password:
        new_client = Client(name, email, password)
        clients.append(new_client)
        print("Cadastro realizado com sucesso!")
        print(clients)
    else:
        print(Fore.RED + "As senhas não são iguais." + Style.RESET_ALL)

def login():
    email = input("Digite seu e-mail:")
    password = input("Digite sua senha:")

    logged_in = (client.email == email and client.password == password for client in clients)

    if logged_in:
        print("Você está logado(a), Bem-vindo(a)!")
        actions(email)
    else:
        print(Fore.RED + "E-mail ou senha incorretos!" + Style.RESET_ALL)




    