from MaxMercado import database,login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_usuario(id_admin):
    return Loginadm.query.get(int(id_admin))

class Produto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nomeProduto = database.Column(database.String, nullable=False)
    categoriaProduto = database.Column(database.String, nullable=False)
    estoque = database.Column(database.Integer, nullable=True)
    valor = database.Column(database.Float, nullable=False)


class Loginadm(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    login = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False, unique=True)