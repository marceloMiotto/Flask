from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

altcoins = {"BabyDoge": "Baby Doge Coin",
            "SHIB": "Shiba Inu",
            "RACA": "RadioCaca"}


class Altcoin(Resource):

    def get(self, token_id: int = None):
        return altcoins

    def post(self):
        return altcoins

    def put(self, token_id: int):
        return altcoins

    def delete(self, token_id: int):
        return altcoins


api.add_resource(Altcoin, "/", "/<token_id>")


if __name__ == '__main__':
    app.run(debug=True)
