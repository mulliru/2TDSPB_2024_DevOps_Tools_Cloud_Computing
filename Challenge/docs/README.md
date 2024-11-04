# Projeto DevOps Challenge - Odontoprev

Este projeto é parte do desafio DevOps e utiliza uma API desenvolvida em Python para manipulação de dados, utilizando Flask, MySQL, Docker e Nginx. O projeto foi configurado para deployment em uma máquina virtual no Azure com suporte a Docker Compose.

## Integrantes

- **Murillo Ferreira Ramos** - RM: 553315
- **Pedro Luiz Prado** - RM: 553874
- **William Kenzo Hayashi** - RM: 552659

## Índice

1. [Descrição do Projeto](#descrição-do-projeto)
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)
3. [Estrutura de Pastas](#estrutura-de-pastas)
4. [Configuração do Ambiente](#configuração-do-ambiente)
5. [Instalação e Execução](#instalação-e-execução)
6. [Endpoints da API](#endpoints-da-api)
7. [Considerações de Segurança](#considerações-de-segurança)
8. [Licença](#licença)

## Descrição do Projeto

Este projeto consiste em uma API REST que permite o gerenciamento de informações de usuários com dados como nome e RM. A aplicação utiliza Flask para o backend, MySQL como banco de dados, Docker para containerização e Nginx como proxy reverso.

## Tecnologias Utilizadas

- **Python** com Flask
- **MySQL** como banco de dados
- **Docker** e **Docker Compose**
- **Nginx** como proxy reverso
- **Microsoft Azure** para provisionamento da máquina virtual

## Como acessar a API pela URL do seu navegador
- Digite no navegador o seguinte: http://4.228.226.103/data

Ela retornará a seguinte tela:
![alt text](image.png)



## Estrutura de Pastas

```plaintext
.
├── app/
│   ├── app.py                # Código principal da API Flask
│   ├── init.sql              # Script SQL para inicialização do banco
│   ├── requirements.txt      # Dependências do Python
├── docker/
│   ├── Dockerfile            # Dockerfile para a API
│   ├── docker-compose.yml    # Configuração do Docker Compose
└── README.md                 # Documentação do projeto

```

Prints do projeto:

