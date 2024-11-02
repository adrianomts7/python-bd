from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.databases import Session
import os

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    do{
        print("\n=== SENAI SOLUTION ===")
        print("\n 1 - Adiconar Usuario: ")
        print("\n 2 - Pesquisar um usuario")
        print("\n 3 - Atualizar dados de um usuario")
        print("\n 4 - Excluir um usuario")
        print("\n 5 - Exibit todos os usuarios cadastrados")
        opcao = str(input("Digite a opção que deseja: "))
        
        

    }while()

    # Solicitando dados do usuario
    print("\nAdicionando usuario: ")
    nome = input("Digite o nome do usuario: ")
    email = input("Digite o email do usuario: ")
    senha = input("Digite o senha do usuario: ")

    service.criar_usuario(nome=nome, email=email, senha=senha)

    #Exibindo todos os usuarios na tabela usuarios do banco de dados
    print("\nListando usuarios encontrados: ")
    lista_usuarios = service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(f"\nNome: {usuario.nome}  \nemail: {usuario.email}  \nsenha: {usuario.senha}")

if __name__ == "__main__":
    os.system("cls || clear")
    main()