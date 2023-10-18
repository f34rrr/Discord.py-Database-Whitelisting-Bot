from flask import Flask, jsonify
from threading import Thread
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

uri = os.environ["mongo"]
client = MongoClient(uri, server_api=ServerApi('1'))
app = Flask('')

@app.route('/')	
def home():
  return  "hola"


@app.route('/api/name/<string:name>', methods=['GET'])
def whitelist(name):
  db = client["WLed"]
  col = db["whitelist"]
  if col.find_one({"username": name, "wl": "yes"}):
    return jsonify({"username": name, "wl": "yes"})
  else:
    return jsonify({"username": name, "wl": "no"})


def run():
  app.run(host='0.0.0.0',port=3409)

def keep_alive():
  t = Thread(target=run)
  t.start()