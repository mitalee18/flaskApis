from flask_sqlalchemy import SQLAlchemy
import os, sys
sys.path.append(os.path.dirname(__file__))

db = None
def init(app):
    global db

    db = SQLAlchemy(app)

class CURD:
    
    def get_all(model):
        data = model.query.all()
        return data