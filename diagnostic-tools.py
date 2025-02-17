import subprocess
import platform
import os
import time

# Definição de cores ANSI
verde = "\033[1;32m"
azul = "\033[1;34m"
vermelho = "\033[1;31m"
amarelo = "\033[1;33m"
reset = "\033[0m"

# Função para limpar a tela
def limpar_tela():
    if platform.system() == "Windows":
        os.system("cls")  # Comando para Windows
    elif platform.system() == "Linux":
        os.system("clear")  # Comando para Linux/macOS

# Função para verificar a versão do sistema
def versao_sistema():
    if platform.system() == "Windows":
        os.system("wmic os get Caption, Version")  # Corrige o comando
    elif platform.system() == "Linux":
        resultado = subprocess.run(["lsb_release", "-d", "-r"], capture_output=True, text=True)
        linhas = resultado.stdout.splitlines()
        distro = linhas[0].split(":")[1].strip()
        version = linhas[1].split(":")[1].strip()
        print(f"{distro} {version}")

# Função para o submenu de rede
def submenu_rede():
    while True:
        limpar_tela()
        print("\n==== Teste em Rede ====")
        print("[1] IP")
        print("[2] PING")
        print("[3] Voltar ao menu principal")
        opcao_submenu_rede = str(input("\n Escolha a opção desejada: "))
        
        ## Opção 1 - IPCONFIG
        if opcao_submenu_rede == "1":
            if sistema == "Windows":
                resultado = subprocess.run("ipconfig", shell=True, capture_output=True, text=True)
            elif sistema == "Linux":  # Aqui inclui também o WSL
                resultado = subprocess.run("ip a", shell=True, capture_output=True, text=True)
            print("Saída:\n", resultado.stdout)
            if resultado.stderr:
                print(f"Erro:\n{resultado.stderr}")
            input("Pressione Enter para continuar...")  # Pausa aqui
       
        ## Opção 2 - PING
        elif opcao_submenu_rede == "2":
            ip = str(input("Digite o endereço IP desejado exemplo (python.org): ")).strip()
            if sistema == "Windows":
                resultado = subprocess.Popen(["ping", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            elif sistema == "Linux":  
                resultado = subprocess.Popen(["ping", "-c", "4", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            # Exibe a saída linha por linha em tempo real
            for linha in resultado.stdout:
                print(linha, end="")  # O 'end' evita a quebra extra de linha
            resultado.wait()

            erro = resultado.stderr.read() # Captura qualquer erro
            if resultado.returncode == 0: # Verifica o código de retorno do comando
                print("\nPing bem-sucedido!")
            else:
                print(f"\nErro ao tentar conectar ao IP ou domínio: {ip}")  # Mensagem de erro
            input("Pressione Enter para continuar...")  # Pausa aqui

        elif opcao_submenu_rede == "3":
            print("Voltando ao menu principal...")
            time.sleep(1.7)
            limpar_tela()
            return

# Função para o submenu de hardware
def submenu_hardware():
    while True:
        limpar_tela()
        print("\n==== Teste de Hardware ====")
        print("[1] Teste de disco (HDD / SSD)")
        print("[2] Teste de memória RAM")
        print("[3] Voltar ao menu principal")
        opcao_submenu_hard = str(input("\n Escolha a opção desejada: "))

        ### Submenu Hardware 1
        if opcao_submenu_hard == "1":
            if platform.system() == "Windows":
                # Executando o comando e capturando a saída
                resultado = subprocess.run(["wmic", "diskdrive", "get", "model,mediaType,size"],shell=True, capture_output=True, text=True)
            
            elif sistema == "Linux":  
                resultado = subprocess.run("lsblk -o NAME,MODEL,SIZE,ROTA,TYPE", shell=True, capture_output=True, text=True)

                 # Verificando se há erro na execução
            if resultado.stderr:
                print("Erro na execução do comando:", resultado.stderr)
                
            else: # Exibindo a saída (stdout)
                print("\nResultado da execução do comando:")
                print(resultado.stdout)
            
            input("Pressione Enter para continuar...")  # Pausa aqui

        ### Submenu Hardware 2
        elif opcao_submenu_hard == "2":
            if platform.system() == "Windows":
                # Executando o comando e capturando a saída
                comando = "wmic memorychip get capacity, manufacturer, partnumber"
                resultado = subprocess.run(comando,shell=True, capture_output=True, text=True)
            
            elif sistema == "Linux":
                comando1 = "sudo lshw -C memory && free -h"
                
                resultado = subprocess.run(comando1, shell=True, capture_output=True, text=True)

                 
            if resultado.stderr:
                print("Erro na execução do comando:", resultado.stderr)
                
            else: 
                print("\nResultado da execução do comando:")
                print(resultado.stdout)
            
            input("Pressione Enter para continuar...")

        ### Submenu Hardware 3
        elif opcao_submenu_hard == "3":
            print("Voltando ao menu principal...")
            time.sleep(1.7)
            limpar_tela()
            return

# Função para o submenu de software
def submenu_software():
    while True:
        limpar_tela()
        print("\n==== Submenu - Testes de Software  ====")
        print("[1] Teste de Software 1")
        print("[2] Teste de Software 2")
        print("[3] Voltar ao menu principal")

        opcao_submenu_soft = str(input("\n Escolha a opção desejada: "))
        if opcao_submenu_soft == "1":
            print("Opção 1 de Software")
            input("Pressione Enter para continuar...")
        elif opcao_submenu_soft == "2":
            print("Opção 2 de Software")
            input("Pressione Enter para continuar...")
        elif opcao_submenu_soft == "3":
            print("Voltando ao menu principal...")
            time.sleep(1.7)
            limpar_tela()
            return

# Identifica o sistema operacional
sistema = platform.system()     # Detecta automaticamente o sistema operacional
usuario = os.getenv("USERNAME") if sistema == "Windows" else os.getenv("USER")
diretorio = os.getcwd()

def get_os_info():
    sistema = platform.system()
    
    if sistema == "Windows":
        # Corrige o comando para obter tanto a descrição quanto a versão
        result = subprocess.run(["wmic", "os", "get", "Caption,Version"], capture_output=True, text=True)
        lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
        if len(lines) >= 2:
            caption = lines[0]  # Captura a descrição do sistema operacional
            version = lines[1]  # Captura a versão
            return sistema, caption, version
        else:
            return sistema, "Desconhecido", "Desconhecido"
    
    elif sistema == "Linux":
        # Obtém a distribuição e versão usando lsb_release
        result = subprocess.run(["lsb_release", "-d", "-r"], capture_output=True, text=True)
        lines = result.stdout.splitlines()
        if len(lines) >= 2:
            caption = lines[0].split(":", 1)[1].strip()  # Captura a descrição da distro
            version = lines[1].split(":", 1)[1].strip()  # Captura a versão
            return sistema, caption, version
        else:
            return sistema, "Desconhecido", "Desconhecido"

    return sistema, "Desconhecido", "Desconhecido"



# Função de MENU principal
def menu_principal():
    limpar_tela()
    sistema, caption, version = get_os_info()  # Corrige a chamada da função
    while True:
        # Exibe as informações
        print(f"{verde}Usuário logado:{reset} {usuario}")
        print(f"{verde}Diretório atual:{reset} {diretorio}")
        if sistema == "Windows":
            print(f"{verde}Sistema Operacional:{reset} {sistema} "
                  #f"\n{verde}Distribuição:{reset} {caption}"
                  f"\n{verde}Version:{reset} {version}")
        elif sistema == "Linux":
            print(f"{verde}Sistema Operacional:{reset} {sistema} "
                  f"\n{verde}Distribuição:{reset} {caption}"
                  f"\n{verde}Version:{reset} {version}")  
            
        

        print("\n=============================="
              +"\n        MENU PRINCIPAL \n"
              "==============================")
        print("[1] Rede\n"
              +"[2] Hardware\n"
              +"[3] Software\n"
              +"[0] Finalizar Programa")
        opcao_menu = str(input("\nEscolha uma opção: "))

        if opcao_menu == "1":
            submenu_rede() # Chama o submenu rede    
        elif opcao_menu == "2":
            submenu_hardware() # Chama o submenu hardware
        elif opcao_menu == "3":
            submenu_software() # Chama o submenu software
        elif opcao_menu == "0":
            
            limpar_tela()
            print("Finalizando o script ...")
            time.sleep(1.5)
            
            print("Obrigado por ultilizar este script em Python ;)")
            time.sleep(1.5)
            print("""
        /^\\/^\\
      _|__|  O|
\\/     /~     \_/ \\
 \\____|__________/  \\
        \\_______      \\
                `\\     \\                 \\
                  |     |                  \\
                 /      /                    \\
                /     /                       \\
              /      /                         \\ \\
             /     /                            \\  \\
           /     /             _----_            \\   \\
          /     /           _-~      ~-_         |   |
         (      (        _-~    _--_    ~-_     _/   |
          \\      ~-____-~    _-~    ~-_    ~-_-~    /
            ~-_         _-~          ~-_       _-~
               ~--______-~                ~-___-~
""")
            time.sleep(1.5)
            break
        else:
            limpar_tela()
            print("Ops! \nOpção inválida, vamos tentar novamente.")
            time.sleep(3)
            limpar_tela()

# Inicia o menu principal 
menu_principal()
