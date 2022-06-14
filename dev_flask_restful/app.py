from flask import Flask, jsonify, request
from flask_restful import Resource, Api, abort, reqparse

app = Flask(__name__)
api = Api(app)

altcoins = {"BabyDoge": "Baby Doge Coin",
            "SHIB": "Shiba Inu",
            "RACA": "RadioCaca"}


def abort_if_token_doesnt_exist(token):
    if token not in altcoins:
        abort(404, message=f"Token {token} doesn't exist")


class Altcoin(Resource):

    def get(self, token: str = None):
        if token is None:
            return altcoins
        else:
            abort_if_token_doesnt_exist(token=token)
            return jsonify({token: altcoins[token]})

    def post(self):
        tokens = request.get_json()
        altcoins.update(tokens)
        print(altcoins)
        return altcoins, 201

    def put(self, token: str):
        abort_if_token_doesnt_exist(token=token)
        tokens = request.get_json()
        altcoins[token] = tokens[token]
        return altcoins, 201

    def delete(self, token: str):
        abort_if_token_doesnt_exist(token=token)
        del altcoins[token]
        return "", 204


api.add_resource(Altcoin, "/", "/<token>")


if __name__ == '__main__':
    app.run(debug=True)
