from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.databases import Session
import os

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    while True:
        print("\n === SENAI SOLUTION ===")
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
                
                continue
            
            case 2:
                os.system("cls || clear")
                
                emailProcurar = input("Digite o email do usuario que deseja procurar: ")
                service.procurar_usuario(email=emailProcurar)
                
                continue
                
            case 3:
                os.system("clear || cls")
                
                emailUsuario = input("Digite o email do usuario que irá ser atualizado: ")
                nome = input("Nome atualizado do usuario: ")
                email = input("Digite o email atualizado do usuario: ")
                senha = input("Digite a senha atualizada do usuario: ")
                
                service.atualizar_usuario(email=emailUsuario,nomeAtualizado=nome, emailAtualizado=email, senhaAtualizada=senha)
                
                continue
            
            case 4:
                os.system("clear || cls")
                
                email = input("Digite o email do usuario que vai apagar: ")
    
                service.excluir_usuario(email=email)
                
                continue
            
            case 5:
                os.system("cls || clear")
                
                lista_usuarios = service.listar_todos_usuarios()
                for usuario in lista_usuarios:
                    print(f"\nNome: {usuario.nome}  \nemail: {usuario.email}  \nsenha: {usuario.senha}")
                
                continue
            
            case 0:
                os.system("cls || clear")
                print("Finalizando sistema")
                break

if __name__ == "__main__":
    os.system("cls || clear")
    main()