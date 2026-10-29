import sys

if len(sys.argv) == 2:
    caminho_log = sys.argv[1]
else:
    print("Você precisa informar o arquivo avaliado via terminal ")
    sys.exit()
falhas = {}
limite = 3
try:
    with open(caminho_log, "r") as arquivo:
        for linha in arquivo:
            if "login failed" in linha:
                partes = linha.split()
                ip = partes[len(partes)-1]
                if ip in falhas:
                    falhas[ip] += 1
                else:
                    falhas[ip] = 1
        tentativa_suspeita = False
        for ip, quantidade in falhas.items():
            if quantidade >= limite:
                print(f"IP suspeito: {ip} - {quantidade} falhas")
                tentativa_suspeita = True
        if not tentativa_suspeita:
            print("Nenhum IP suspeito identificado.")
except FileNotFoundError:
    print("O caminho informado não existe")
