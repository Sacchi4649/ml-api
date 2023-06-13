from flask import Flask, jsonify, request, Response
from flask_cors import CORS
# import pymongo
# import numpy
import json
import machine_learning

app = Flask(__name__)


@app.route('/machine-learning', methods=['POST'])
def findAll():
    json_data = request.get_json()
    # keywords = json_data.get("keywords")
    # city = json_data.get("city")
    # print(request.json["keywords"])
    keywords = request.json["keywords"]
    city = request.json["city"]
    ML = machine_learning.recommend_destinations(keywords, city)
    return jsonify(ML)


if __name__ == '__main__':
    app.run(debug=True)
