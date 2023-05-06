from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '8e3d6133e6ceffe8c1b420a3c05db244'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sysestoque.db'
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Acesso restrito! Faça o login'
login_manager.login_message_category = 'alert-warning'
from MaxMercado import routers
