from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pztntpvp:WRrQ-Atcl_dl7TQ-pyL87xZB53Qpgl7U@trumpet.db.elephantsql.com/pztntpvp'
db = SQLAlchemy(app)

from application import routes