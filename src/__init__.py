from flask import Flask
from flask_restful import Api, Resource #2 main modules to use

app = Flask(__name__)
api = Api(app)

if __name__ == '__main__':
    app.run(debug=True) #only for developing environment
