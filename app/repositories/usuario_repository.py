from models.usuario_models import Usuario
from sqlalchemy.orm import Session

class UsuarioRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def salvar_usuario(self, usuario: Usuario):
        self.session.add(usuario)
        self.session.commit()

    def pesquisar_usuario_por_email(self, email: str):
        return self.session.query(Usuario).filter_by(emai = email).first()

    def excluir_usuario(self, usuario: Usuario):
        self.session.delete(usuario)
        self.session.commit()

    def listar_usuarios(self):
        return self.session.query(Usuario).all()