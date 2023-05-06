from flask import render_template, url_for, redirect, flash, request, get_flashed_messages
from MaxMercado.forms import FormCadProduto, FormLogin, FormDeletProduto, FormEditProduto, FormSearchProd
from MaxMercado import app, database, bcrypt
from MaxMercado.models import Produto, Loginadm
from flask_login import login_user, logout_user, login_required


@app.route('/', methods=['GET', 'POST'])
def login():
    form_login_adm = FormLogin()
    if form_login_adm.validate_on_submit():
        try:
            admin = Loginadm.query.filter_by(login=form_login_adm.admin.data).first()
            descripto_senha = bcrypt.check_password_hash(admin.senha, form_login_adm.senha.data)
            if admin and descripto_senha:
                login_user(admin)
                return redirect(url_for('produtos'))
            else:
                return redirect(url_for('login'))
        except:
            flash(f'Usuário ou senha incorretos')
    return render_template('index.html', form_login=form_login_adm)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash(f'Sessão finalizada')
    return redirect(url_for('login'))


@app.route('/produtos', methods=['GET', 'POST'])
@login_required
def produtos():
    form_produto = FormCadProduto()
    form_edit_prod = FormEditProduto()
    form_search_prod = FormSearchProd()
    form_delet_id = FormDeletProduto()
    lista_produtos = Produto.query.all()

    '''Cadastra um produto'''
    if 'add_product' in request.form and form_produto.validate_on_submit():
        # Entra no cadastro
        try:
            # Tenta cadastrar
            produto = Produto(nomeProduto=form_produto.nomeProduto.data,
                              categoriaProduto=form_produto.categoriaProduto.data, estoque=form_produto.estoque.data,
                              valor=form_produto.valor.data)

            '''Teste para saber se os valores estão corretos'''
            # print(f'{produto.nomeProduto}\n'
            #       f'{produto.categoriaProduto}\n'
            #       f'{produto.estoque}\n'
            #       f'{produto.valor}')

            database.session.add(produto)
            database.session.commit()
            database.session.close()
        except Exception as e:
            print(e)
        return redirect(url_for('produtos'))

    '''Edita um produto'''
    # Verifica o request correto e valida o input
    if 'edit_product' in request.form and form_edit_prod.validate_on_submit():
        try:
            # Procura o id do produto inserido no input
            produtoEdit = Produto.query.filter_by(id=form_edit_prod.idProduto.data).first()

            # Verifica se o dado procurado existe e então o edita
            if produtoEdit:
                produtoEdit.nomeProduto = form_edit_prod.nomeProduto.data
                produtoEdit.categoriaProduto = form_edit_prod.categoriaProduto.data
                produtoEdit.estoque = form_edit_prod.estoque.data
                produtoEdit.valor = form_edit_prod.valor.data

                database.session.commit()
        except Exception as e:
            print(e)

    '''Procura um produto'''

    if 'search_prod' in request.form and form_search_prod.validate_on_submit():
        try:
            produtoSearch = Produto.query.filter(Produto.nomeProduto.ilike(f"%{form_search_prod.nomeProduto.data}%")).all()
            lista_produtos = produtoSearch
        except Exception as e:
            print(e)

    '''Excluir Produto'''
    if 'deletarProd' in request.form:
        try:
            produto_delet = Produto.query.filter_by(id=form_delet_id.id.data).first()
            if(produto_delet):
                database.session.delete(produto_delet)
                database.session.commit()
                lista_produtos = Produto.query.all()
        except Exception as e:
            print(e)

    return render_template('produtos.html', form_produto=form_produto, form_delet_id=form_delet_id,
                           lista_produtos=lista_produtos, form_search_prod=form_search_prod,
                           form_edit_prod=form_edit_prod)
