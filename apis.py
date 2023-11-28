from main import api
from flask_restx import Resource


@api.route('/getmealAmount') 
class MealAmount(Resource):
    def get(self): 
        return {
            "amount": 100
        }


