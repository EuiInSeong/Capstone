from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)  

@api.route('/getmealAmount') 
class MealAmount(Resource):
    def get(self): 
        return {
            "amount": 100
        }

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=3000)