from flask import Flask 
from flask_bcrypt import Bcrypt
    
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key ="12931812-xasx22-123sd-22"
# DATABASE = 'schema name'