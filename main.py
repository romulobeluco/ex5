import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['seu_database']
collection = db['livros']

def inserir_livro():
    livro = {
        "_id": input("ID do livro: "),
        "titulo": input("Título: "),
        "autor": input("Autor: "),
        "ano": int(input("Ano: ")),
        "preco": float(input("Preço: "))
    }
    collection.insert_one(livro)
    print("Livro inserido com sucesso!")

def listar_livros():
    for livro in collection.find():
        print(livro)

def atualizar_livro():
    livro_id = input("ID do livro a ser atualizado: ")
    novo_valor = {"$set": {
        "titulo": input("Novo Título: "),
        "autor": input("Novo Autor: "),
        "ano": int(input("Novo Ano: ")),
        "preco": float(input("Novo Preço: "))
    }}
    collection.update_one({"_id": livro_id}, novo_valor)
    print("Livro atualizado com sucesso!")

def remover_livro():
    livro_id = input("ID do livro a ser removido: ")
    collection.delete_one({"_id": livro_id})
    print("Livro removido com sucesso!")

def menu():
    while True:
        print("\nMenu CRUD - Collection Livros")
        print("1 - Inserir Livro")
        print("2 - Listar Livros")
        print("3 - Atualizar Livro")
        print("4 - Remover Livro")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            inserir_livro()
        elif opcao == '2':
            listar_livros()
        elif opcao == '3':
            atualizar_livro()
        elif opcao == '4':
            remover_livro()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    menu()
