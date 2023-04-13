from flask import Flask
from flask import Flask, request, jsonify

app = Flask(__name__)

clientes = []

class Cliente:
    def __init__(self, nome, endereco, email, telefone):
        self.nome = nome
        self.endereco = endereco
        self.email = email
        self.telefone = telefone

def cadastrar_cliente():
    nome = input("Nome: ")
    endereco = input("Endereço: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    novo_cliente = Cliente(nome, endereco, email, telefone)
    clientes.append(novo_cliente)
    print("Cliente cadastrado com sucesso!")

def exibir_cliente():
    email = input("Email do cliente: ")
    for cliente in clientes:
        if cliente.email == email:
            print("Nome: ", cliente.nome)
            print("Endereço: ", cliente.endereco)
            print("Telefone: ", cliente.telefone)
            return
    print("Cliente não encontrado.")

def atualizar_cliente():
    email = input("Email do cliente: ")
    for cliente in clientes:
        if cliente.email == email:
            novo_nome = input("Novo nome: ")
            novo_endereco = input("Novo endereço: ")
            novo_telefone = input("Novo telefone: ")
            cliente.nome = novo_nome
            cliente.endereco = novo_endereco
            cliente.telefone = novo_telefone
            print("Cliente atualizado com sucesso!")
            return
    print("Cliente não encontrado.")

def excluir_cliente():
    email = input("Email do cliente: ")
    for cliente in clientes:
        if cliente.email == email:
            clientes.remove(cliente)
            print("Cliente excluído com sucesso!")
            return
    print("Cliente não encontrado.")

while True:
    print("1 - Cadastrar cliente")
    print("2 - Exibir informações do cliente")
    print("3 - Atualizar informações do cliente")
    print("4 - Excluir cliente")
    print("5 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        exibir_cliente()
    elif opcao == "3":
        atualizar_cliente()
    elif opcao == "4":
        excluir_cliente()
    elif opcao == "5":
        break
    else:
        print("Opção inválida.")
