import socket
import sys
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def verificar_argumentos():
    try: 
        menu = None
        if len(sys.argv[1:]) > 0:
            host = sys.argv[1]
            menu = int(sys.argv[2])
        else:
            host = input(">>>>> Digite o domínio desejado: ")
            clear_screen()
            print("1 - Verificar apenas portas populares")
            print("2 - Verificar todas as portas")
            menu = int(input(">>>>> Digite uma opção: "))
        return host, menu
    except Exception:
        print("Algum erro ocorreu!")
        exit()

def tipo_verificacao(menu):
    if menu == 1:
        print("(Verificação Rápida)")
        ports = range(1024) 
        return ports
    elif menu == 2:
        print("(Verificação Completa)")
        ports = range(65536)  
        return ports
    else:
        print("Tipo de verificação inválido!")
        exit()

def verificacao(host, ports):
    try: 
        print(f"Host: {host}")
        portas_abertas = []
        print("Portas abertas: ")
        for port in ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.05)
            status_code = client.connect_ex((host, port))
            if status_code == 0:
                print(f"[+] {port} open")
                portas_abertas.append(port)
            client.close()
        return portas_abertas
    except Exception:
        print("Algum erro ocorreu!")
        exit()

if __name__ == "__main__":
    clear_screen()
    host, menu = verificar_argumentos()
    ports = tipo_verificacao(menu)
    portas_abertas = verificacao(host, ports)
    if len(portas_abertas) == 0:
        print("Nenhuma porta aberta foi encontrada!")
    else:
        print("Portas abertas encontradas:", portas_abertas)


