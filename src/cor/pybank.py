from helpers.functions import create_account, login, actions
from colorama import just_fix_windows_console, Fore, Style, Back
just_fix_windows_console()

def welcome():
    while True:
        print(Fore.CYAN + "Bem-vindo(a) ao PyBank" + Style.RESET_ALL)
        print("1-Login")
        print("2-Criar uma conta")
        choices = input("Escolha:")
        
        if choices == '1':
            print(Fore.CYAN + "Login:" + Style.RESET_ALL)
            login()
        elif choices == '2':
            print(Fore.CYAN + "Criar conta:" + Style.RESET_ALL)
            create_account()
        else:
            print(Fore.RED + "Opção inválida. Por favor, escolha 1 ou 2." + Style.RESET_ALL)


def later():
    print("Novo teste de função")