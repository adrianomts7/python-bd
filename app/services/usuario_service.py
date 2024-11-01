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