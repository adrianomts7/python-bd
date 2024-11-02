from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.databases import Session
import os

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    while True:
        os.system("cls || clear")
        print(" === SENAI SOLUTION ===")
        print(" 1 - Adiconar Usuario ")
        print(" 2 - Pesquisar um usuario")
        print(" 3 - Atualizar dados de um usuario")
        print(" 4 - Excluir um usuario")
        print(" 5 - Exibir todos os usuarios cadastrados")
        print(" 0 - Sair")
        
        try:
            opcao = int(input("Digite a opção que deseja: "))
        except:
            print("Digite somente números inteiros.")
            continue
        
        match opcao:
            case 1:
                os.system("cls || clear")
                nome = input("Digite o nome do usuario: ")
                email = input("Digite o email do usuario: ")
                senha = input("Digite o senha do usuario: ")
                
                service.criar_usuario(nome=nome, email=email, senha=senha)  
                
                break
            
            case 2:
                os.system("cls || clear")
                
                email = input("Digite o email do usuario que deseja procurar: ")
                service.procurar_usuario(email=email)
                
                break
                
            case 3:
                os.system("clear || cls")
                
                email = input("Digite o nome do usuario que deseja atualizar: ")
                nomeAtualizado = input("Nome atualizado do usuario: ")
                emailAtualizado = input("Digite o email atualizado do usuario: ")
                senhaAtualizado = input("Digite a senha atualizada do usuario: ")
                
                service.atualizar_usuario(email=email,nomeAtualizado=nomeAtualizado, emailAtualizado=emailAtualizado, senhaAtualizada=senhaAtualizado)
                
                break

    #Exibindo todos os usuarios na tabela usuarios do banco de dados
    print("\nListando usuarios encontrados: ")
    lista_usuarios = service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(f"\nNome: {usuario.nome}  \nemail: {usuario.email}  \nsenha: {usuario.senha}")

if __name__ == "__main__":
    os.system("cls || clear")
    main()