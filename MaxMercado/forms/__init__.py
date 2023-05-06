from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, length, Optional


class FormLogin(FlaskForm):
    admin = StringField('Usuário', validators=[DataRequired(), length(6)])
    senha = PasswordField('Senha',  validators=[DataRequired(), length(6, 16)])
    submit_entrar = SubmitField('Entrar')

class FormCadProduto(FlaskForm):
    nomeProduto = StringField('Nome Produto', validators=[DataRequired(), length(1)])
    categoriaProduto = StringField('Categoria Produto', validators=[DataRequired(), length(1)])
    estoque = IntegerField('Estoque Produto')
    valor = FloatField('Valor Produto', validators=[Optional()])
    submit_produto = SubmitField('Enviar')

class FormEditProduto(FlaskForm):
    idProduto = IntegerField('ID Produto', validators=[DataRequired()])
    nomeProduto = StringField('Nome Produto', validators=[DataRequired(), length(1)])
    categoriaProduto = StringField('Categoria Produto', validators=[DataRequired(), length(1)])
    estoque = IntegerField('Estoque Produto')
    valor = FloatField('Valor Produto', validators=[Optional()])
    submit_produto_edit = SubmitField('Editar')


class FormSearchProd(FlaskForm):
    nomeProduto = StringField('Nome Produto', validators=[DataRequired(), length(1)])
    submit_produto_search = SubmitField('Procurar')


class FormDeletProduto(FlaskForm):
    id = IntegerField('ID Produto', validators=[Optional()])
    submit_produto_delet = SubmitField('Excluir')
