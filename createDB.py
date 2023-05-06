from MaxMercado import app, database
from MaxMercado.models import Loginadm, Produto
from MaxMercado import bcrypt

if __name__=='__main__':
    '''Criar o banco de dados'''
    with app.app_context():
        database.drop_all()
        database.create_all()

    '''Excluir o banco de dados'''
    # with app.app_context():
    #     database.drop_all()

    '''Inserir um registro em uma tabela usando o model da tabela'''
    with app.app_context():
        senha = '123456789'
        hash = bcrypt.generate_password_hash(senha)
        admin = Loginadm(login='@@./admin/', senha=hash)
        database.session.add(admin)
        database.session.commit()

    # '''Realizar um select de todos os registros de uma tabela'''
    # with app.app_context():
    #     admin = Produto.query.all()
    #     print(admin)


    '''Realizar um select de todos os registros, retornando apenas o primeiro registro'''
    # with app.app_context():
    #     user = Usuario.query.first()
    #     print(user.usuario)

    '''Realizar um select com base em um filtro e retorna os registros equivalentes à condição
    with app.app_context():
        user = Usuario.query.filter_by(senha='123456').all()
        print(user)
    '''

    '''BCRYPT'''
    #* Excluir o banco e recria-lo
    # senha = '123456'
    # hash = bcrypt.generate_password_hash(senha)
    # print(senha)
    # print(hash)
    # print(bcrypt.check_password_hash(hash, senha))
    # senha_crypto = bcrypt.generate_password_hash('#passar o formulario.senha.data')

