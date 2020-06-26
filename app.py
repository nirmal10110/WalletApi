from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv

from db import db
from ma import ma
from resources.wallet import Wallets, Wallet, WalletSendAmount, AddWallet, WalletAddAmount

app = Flask(__name__)
app.config.from_object("default_config")
api = Api(app)

api.add_resource(Wallets, "/wallets")
api.add_resource(Wallet, "/wallet")
api.add_resource(WalletSendAmount, "/wallet/amount")
api.add_resource(AddWallet, "/add/wallet")
api.add_resource(WalletAddAmount, "/wallet/add/amount")

if __name__ == "__main__":
    ma.init_app(app)
    app.run(port=5000, debug=True)
