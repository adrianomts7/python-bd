from models.usuario_models import Usuario
from repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self, repository: UsuarioRepository) -> None:
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha: str):
        try:
            usuario = Usuario(nome=nome,email=email,senha=senha)

            cadastrado = self.repository.pesquisar_usuario_por_email(usuario.email)

            if cadastrado:
                print("Usuario já cadastrado!")
                return

            self.repository.salvar_usuario(usuario=usuario)
            print("Usuario cadastrado com sucesso")

        except TypeError as erro:
            print(f"Erro ao salvar o usuario: {erro}")

        except Exception as erro:
            print (f"Ocorreu um erro inesperado: {erro}")

    def listar_todos_usuarios(self):
        return self.repository.listar_usuarios()    
        
    def procurar_usuario(self,email: str):
        try:
            cadastrado = self.repository.pesquisar_usuario_por_email(email=email)

            if cadastrado:
                print("Usuario Encontrado com sucesso")
                print(f"{cadastrado.nome} - {cadastrado.email}")
        
        except TypeError as erro:
            print(f"Erro ao procurar usuario: {erro}")
            
        except Exception as erro:
            print(f"Erro inesperado: {erro}")
            
    def atualizar_usuario(self,email: str,nomeAtualizado: str, emailAtualizado: str, senhaAtualizada: str):
        try:
            usuario = self.repository.pesquisar_usuario_por_email(email=email)
                
            if usuario:
                usuario.nome = nomeAtualizado
                usuario.email = emailAtualizado
                usuario.senha = senhaAtualizada
                print("Usuario Atualizado com sucesso!")
                self.repository.session.commit()
                
        except TypeError as erro:
            print(f"Erro ao tentar atualizar usuario: {erro}")
            
    def excluir_usuario(self,email: str):
        try:
            cadastrado = self.repository.pesquisar_usuario_por_email(email=email)
            
            if not cadastrado:
                print("Usuario não encontrado")
                return    
            
            self.repository.excluir_usuario(usuario=cadastrado)
            print("Usuario Excluido com sucesso!")
            
        except TypeError as erro:
            print(f"Erro ao apagar usuario: {erro}")
            
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")