falhas = {}
limite = 3
with open("exemplos/auth.log", "r") as arquivo:
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
