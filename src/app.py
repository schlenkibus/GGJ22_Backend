from flask import Flask, redirect, render_template, send_file
import json
from Game import Game

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/create")
def create_market():
    game = app.app_ctx_globals_class.state
    market = game.createMarket()
    app.app_ctx_globals_class.state = game
    return redirect(f"game/{market}")

@app.route("/game/<uuid>")
def game(uuid):
    game = app.app_ctx_globals_class.state
    market = game.findMarket(uuid)
    if(market != None):
        app.app_ctx_globals_class.state = game
        return render_template("game.html", market_id = market.getID())
    return redirect(f"/404/{uuid}")

@app.route("/404/<uuid>")
def fourOFour(uuid):
    return render_template("404.html", id = uuid)

@app.route("/list")
def list():
    game = app.app_ctx_globals_class.state
    return render_template("index.html", markets=game.getMarkets())

@app.route("/list-raw")
def listRaw():
    game = app.app_ctx_globals_class.state
    markets = game.getMarkets()
    return json.dumps(markets)

if __name__ == "__main__":
    app.app_ctx_globals_class.state = Game(app)
    app.run(host='0.0.0.0', port='8000')