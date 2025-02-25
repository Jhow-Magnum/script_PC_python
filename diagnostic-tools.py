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
        os.system("cls")  
    elif platform.system() == "Linux":
        os.system("clear")  


# Função para o submenu de rede
def submenu_rede():
    while True:
        limpar_tela()
        print("\n==== Diagnóstico de Rede ====")
        print("[1] Exibir informações do IP e interfaces de rede")
        print("[2] Realizar teste de PING")
        print("[3] Mostrar conexões de rede ativas")
        print("[4] Verificar conectividade com traceroute")
        print("[5] Listar usuários que realizaram login anteriormente")
        print("[6] Identificar o usuário logado no sistema")
        print("[7] Obter o IP local da máquina")
        print("[8] Obter o IP de um site remoto")
        print("[9] Exibir redes cabeadas disponíveis")
        print("[10] Exibir MAC Address das interfaces de rede")
        print("[11] Limpar cache de navegação (Chrome e Firefox)")
        print("[12] Apagar cookies de navegação")
        print("[13] Voltar ao menu principal")
        opcao_submenu_rede = str(input("\n Escolha a opção desejada: "))
        
        ## [1]  Exibir informações do IP e interfaces de rede
        if opcao_submenu_rede == "1":
            if sistema == "Windows":
                resultado = subprocess.run("ipconfig", shell=True, capture_output=True, text=True)
            elif sistema == "Linux":
                resultado = subprocess.run("ip a", shell=True, capture_output=True, text=True)
            print("Saída:\n", resultado.stdout)
            if resultado.stderr:
                print(f"Erro:\n{resultado.stderr}")
            input("Pressione Enter para continuar...")  # Pausa aqui       
        
        ## [2] Realizar teste de PING
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

        ## [3] Mostrar conexões de rede ativas
        elif opcao_submenu_rede == "3": 
            if sistema == "Windows":
                resultado = subprocess.run("netstat -an", shell=True, capture_output=True, text=True) 
            elif sistema == "Linux":
                resultado = subprocess.run("ss -tuln", shell=True, capture_output=True, text=True) 
            print("Saída:\n", resultado.stdout)
            if resultado.stderr:
                print(f"Erro:\n{resultado.stderr}")
            input("Pressione Enter para continuar...")

        ## [4] Verificar conectividade com traceroute em tempo real
        elif opcao_submenu_rede == "4": 
            ipSite = input("Digite o ip (site) para verificar a conectividade com traceroute:  ")
            if sistema == "Windows":
                # Utilizando Popen para Windows
                processo = subprocess.Popen(["tracert",ipSite], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            elif sistema == "Linux":
                # Utilizando Popen para Linux
                 processo = subprocess.Popen(["tracepath", ipSite], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                

            # Exibir a saída em tempo real
            for linha in processo.stdout:
                print(linha, end="")  # O end="" impede a inserção de uma nova linha
            for linha in processo.stderr:
                print(f"Erro: {linha}", end="")  # Exibe os erros, se houver

            processo.wait()  # Espera o processo terminar antes de continuar
            input("Pressione Enter para continuar...")

        ## [5] Listar usuários que realizaram login anteriormente
        elif opcao_submenu_rede == "5": 
            if sistema == "Windows":
                resultado = subprocess.run("net user", shell=True, capture_output=True, text=True) 
            elif sistema == "Linux":
                resultado = subprocess.run("who", shell=True, capture_output=True, text=True) 
            print("Saída:\n", resultado.stdout)
            if resultado.stderr:
                print(f"Erro:\n{resultado.stderr}")
            input("Pressione Enter para continuar...")

        ## [6] Identificar o usuário logado no sistema
        elif opcao_submenu_rede == "6": 
            if sistema == "Windows":
                resultado = subprocess.run("echo %USERNAME%", shell=True, capture_output=True, text=True) 
            elif sistema == "Linux":
                resultado = subprocess.run("whoami", shell=True, capture_output=True, text=True) 
            print("Saída:\n", resultado.stdout)
            if resultado.stderr:
                print(f"Erro:\n{resultado.stderr}")
            input("Pressione Enter para continuar...")

        ## [7] Obter o IP público local
        elif opcao_submenu_rede == "7": 
            if sistema == "Windows":
                resultado  = subprocess.run("curl ipecho.net/plain", shell=True, capture_output=True, text=True) 
            elif sistema == "Linux":
                resultado = subprocess.run("curl ifconfig.me", shell=True, capture_output=True, text=True) 
            print(f"\nIP público local da máquina: {resultado.stdout}\n ")
            
            input("Pressione Enter para continuar...")

        ## [8] Obter o IP de um site remoto
        elif opcao_submenu_rede == "8": 
            if sistema == "Windows":
                resultado = subprocess.run("nslookup www.google.com", shell=True, capture_output=True, text=True) 
            elif sistema == "Linux":
                resultado = subprocess.run("host www.google.com", shell=True, capture_output=True, text=True) 
            print("\nResultado:\n", resultado.stdout)
            input("Pressione Enter para continuar...")

        ## [9] Exibir redes cabeadas disponíveis
        elif opcao_submenu_rede == "9": 
            if sistema == "Windows":
                resultado = subprocess.run("netsh interface show interface", shell=True, capture_output=True, text=True) 
            elif sistema == "Linux":
                print("Para a sua segurança o Linux pedirá acesso ao super usuário...")
                time.sleep(0.8)
                resultado = subprocess.run("sudo lshw -class network -short", shell=True, capture_output=True, text=True) 
            print("\nSaída:\n", resultado.stdout)
            if resultado.stderr:
                print(f"Erro:\n{resultado.stderr}")
            input("Pressione Enter para continuar...")


        ## [10] Exibir MAC Address das interfaces de rede
        elif opcao_submenu_rede == "10": 
            if sistema == "Windows":
                resultado = subprocess.run("getmac", shell=True, capture_output=True, text=True) 
            elif sistema == "Linux":
                resultado = subprocess.run("ip link show", shell=True, capture_output=True, text=True) 
            print("Saída:\n", resultado.stdout)
            if resultado.stderr:
                print(f"Erro:\n{resultado.stderr}")
            input("Pressione Enter para continuar...")

        ## [11] Limpar cache de navegação (Chrome e Firefox)
        elif opcao_submenu_rede == "11": 
            if sistema == "Windows":
                resultado = subprocess.run("del /q /f %LocalAppData%\\Google\\Chrome\\User Data\\Default\\Cache\\*", shell=True, capture_output=True, text=True) 
            elif sistema == "Linux":
                resultado = subprocess.run("rm -rf ~/.cache/google-chrome/*", shell=True, capture_output=True, text=True) 
            print("Saída:\n", resultado.stdout)
            if resultado.stderr:
                print(f"Erro:\n{resultado.stderr}")
            input("Pressione Enter para continuar...")

        ## [12] Apagar cookies de navegação
        elif opcao_submenu_rede == "12": 
            if sistema == "Windows":
                resultado = subprocess.run("del /q /f %LocalAppData%\\Google\\Chrome\\User Data\\Default\\Cookies", shell=True, capture_output=True, text=True) 
            elif sistema == "Linux":
                resultado = subprocess.run("rm -rf ~/.config/google-chrome/*/Cookies", shell=True, capture_output=True, text=True) 
            print("Saída:\n", resultado.stdout)
            if resultado.stderr:
                print(f"Erro:\n{resultado.stderr}")
            input("Pressione Enter para continuar...")



        ## [13] Voltar ao menu anterior
        elif opcao_submenu_rede == "13":
            print("Voltando ao menu principal...")
            time.sleep(1.7)
            limpar_tela()
            return
        else:
            input("Opção inválida!\nPressione Enter e tente novamente.")

# Função para o submenu de hardware
def submenu_hardware():
    while True:
        limpar_tela()
        print("\n==== Informações de Hardware ====")
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
        else:
            input("Opção inválida!\nPressione Enter e tente novamente.")

# Função para o submenu de software
def submenu_software():
    while True:
        limpar_tela()
        print("\n==== Informações de Software ====")
        print("[1] Pacotes(softwares) instalados ")
        print("[2] Drivers instalados ")
        print("[3] Voltar ao menu principal ")
        opcao_submenu_soft = str(input("\n Escolha a opção desejada: "))
        

        if opcao_submenu_soft == "1":
            if platform.system() == "Windows":
                print("Carregando...")
                # Executando o comando e capturando a saída
                resultado = subprocess.run(["wmic", "product", "get", "name,version"], shell=True, capture_output=True, text=True)
            
            elif sistema == "Linux":  
                resultado = subprocess.run("dpkg --list", shell=True, capture_output=True, text=True)

                 # Verificando se há erro na execução
            if resultado.stderr:
                print("Erro na execução do comando:", resultado.stderr)
                
            else: # Exibindo a saída (stdout)
                print("\nResultado da execução do comando:")
                print(resultado.stdout)
            
            input("Pressione Enter para continuar...")

        elif opcao_submenu_soft == "2":
            if platform.system() == "Windows":
                print("Carregando...")
                
                resultado = subprocess.run(["driverquery"], shell=True, capture_output=True, text=True)
            
            elif sistema == "Linux":  
                resultado = subprocess.run("lsmod", shell=True, capture_output=True, text=True)

                
            if resultado.stderr:
                print("Erro na execução do comando:", resultado.stderr)
                
            else:
                print("\nResultado da execução do comando:")
                print(resultado.stdout)
            

            input("Pressione Enter para continuar...")    
        elif opcao_submenu_soft == "3":
            print("Voltando ao menu principal...")
            time.sleep(1.7)
            limpar_tela()
            return
        else:
            input("Opção inválida!\nPressione Enter e tente novamente.")

# Identifica o sistema operacional
sistema = platform.system()     # Detecta automaticamente o sistema operacional
usuario = os.getenv("USERNAME") if sistema == "Windows" else os.getenv("USER")
diretorio = os.getcwd()

# Função para obter dados do sistemas operacinal
def obtem_dados_sistemas():
    sistema = platform.system()
    
    if sistema == "Windows":
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

# Função do MENU principal
def menu_principal():
    limpar_tela()
    sistema, caption, version = obtem_dados_sistemas()  # Corrige a chamada da função
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
            
        

        
        print("\n"+"=" * 40)
        print("      SISTEMA DE DIAGNÓSTICO - MENU      ")
        print("=" * 40)
        print("Selecione uma opção:")
        print("[1] Consultar informações de rede\n"
              +"[2] Exibir detalhes do hardware\n"
              +"[3] Listar softwares instalados\n"
              +"[4] Exportar dados para arquivo CSV\n"
              +"[0] Finalizar Programa")
        print("=" * 40)
        opcao_menu = str(input("\nDigite o número da opção desejada: "))

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
