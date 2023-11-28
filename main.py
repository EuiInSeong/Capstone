from flask import Flask
from flask_restx import Api

app = Flask(__name__)
api = Api(app)  

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=3000)