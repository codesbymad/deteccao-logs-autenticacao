# Detecção de Atividades Suspeitas em Logs de Autenticação com Python

## Sobre o projeto

Este projeto foi desenvolvido como parte das atividades do ARES e tem como objetivo estudar e implementar uma forma simples de identificar possíveis atividades suspeitas em logs de autenticação utilizando Python.

A análise é baseada na identificação de tentativas de login malsucedidas e na contagem dessas ocorrências por endereço IP. Quando um IP atinge ou ultrapassa uma quantidade predefinida de falhas, ele é apresentado pelo programa como suspeito.

O projeto utiliza arquivos de log de exemplo com registros fictícios, permitindo testar o funcionamento do script sem expor informações reais.

O repositório contém dois arquivos de exemplo: `auth.log`, com registros de tentativas de autenticação malsucedidas, e `auth_sucesso.log`, com registros de autenticações bem-sucedidas.

## Objetivos

- Compreender a importância dos logs de autenticação para a segurança de sistemas.
- Identificar tentativas repetidas de login malsucedidas.
- Contabilizar falhas de autenticação por endereço IP.
- Reconhecer possíveis indicadores de ataques de força bruta (*Brute Force*).
- Desenvolver um script em Python para automatizar essa análise.

## Funcionamento

O script `detectar_falhas.py` realiza as seguintes etapas:

1. Recebe pelo terminal o caminho do arquivo de log que será analisado.
2. Verifica se o caminho foi informado corretamente.
3. Abre e percorre o arquivo linha por linha.
4. Identifica os registros que contêm a expressão `login failed`.
5. Extrai o endereço IP de cada registro identificado.
6. Conta a quantidade de falhas associadas a cada IP.
7. Compara a quantidade de falhas com o limite estabelecido.
8. Exibe os IPs que atingiram ou ultrapassaram esse limite.

Atualmente, o limite está definido em **3 tentativas malsucedidas**.

## Tecnologias utilizadas

- **Python:** linguagem utilizada no desenvolvimento do script.
- **PyCharm:** ambiente de desenvolvimento.
- **Git e GitHub:** controle de versão e armazenamento do projeto.

## Estrutura do projeto

```text
deteccao-logs-autenticacao/
│
├── exemplos/
│   ├── auth.log
│   └── auth_sucesso.log
│
├── detectar_falhas.py
│
└── README.md
```

## Como executar

### 1. Pré-requisitos

- Python 3 instalado.
- Git instalado, caso queira clonar o repositório.

### 2. Clonar o repositório

```bash
git clone https://github.com/codesbymad/deteccao-logs-autenticacao.git
```

### 3. Acessar a pasta do projeto

```bash
cd deteccao-logs-autenticacao
```

### 4. Executar o script

No terminal, execute:

```bash
python detectar_falhas.py exemplos/auth.log
```

O caminho informado como argumento indica qual arquivo será analisado.

Para testar o arquivo com registros de autenticações bem-sucedidas:

```bash
python detectar_falhas.py exemplos/auth_sucesso.log
```

## Exemplo de resultado

Considerando o arquivo `auth.log`, o programa identifica os seguintes endereços IP:

```text
IP suspeito: 192.168.1.10 - 3 falhas
IP suspeito: 192.168.1.30 - 4 falhas
```

Isso significa que os dois endereços atingiram ou ultrapassaram o limite de três tentativas malsucedidas.

Ao analisar um arquivo sem registros de falhas, o programa apresenta:

```text
Nenhum IP suspeito identificado.
```

## Tratamento de erros

O programa também realiza verificações para tratar situações como:

- **Ausência do caminho do arquivo:** apresenta uma mensagem solicitando que o usuário informe o arquivo a ser analisado.
- **Arquivo inexistente:** apresenta uma mensagem informando que o caminho indicado não existe.

## Limitações

Esta é uma implementação inicial, voltada ao aprendizado e à análise de registros de autenticação.

- A identificação considera registros que contenham exatamente a expressão `login failed`.
- A contagem é realizada por endereço IP, sem separar as tentativas por usuário.
- O limite de três falhas está definido diretamente no código.
- O programa sinaliza possíveis atividades suspeitas, mas não confirma que houve um ataque.
- A análise depende do formato dos registros utilizados, pois o endereço IP é extraído do último elemento da linha.

Portanto, os resultados devem ser interpretados como indicadores que podem justificar uma investigação adicional, e não como confirmação de uma invasão.

## Segurança

Os arquivos da pasta `exemplos/` contêm registros fictícios utilizados exclusivamente para testes.

Não publique logs reais que possam conter endereços IP, nomes de usuários, informações de autenticação ou outros dados sensíveis.

## Autoria

Projeto desenvolvido por **Madeline Almeida Rodrigues**, como atividade prática do ARES, com foco no estudo de logs de autenticação, identificação de tentativas malsucedidas e fundamentos de segurança da informação.