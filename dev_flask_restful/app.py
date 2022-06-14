from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

altcoins = {"BabyDoge": "Baby Doge Coin",
            "SHIB": "Shiba Inu",
            "RACA": "RadioCaca"}


class Altcoin(Resource):

    def get(self):
        return altcoins


api.add_resource(Altcoin, "/")


if __name__ == '__main__':
    app.run(debug=True)
