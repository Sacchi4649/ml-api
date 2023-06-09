from flask import Flask, jsonify, request, Response
# import certifi
from flask_cors import CORS
# import pymongo
# import numpy
import machine_learning

app = Flask(__name__)
# connection_url = 'mongodb+srv://arif05rachman:20082009@arif05rachman.pfggb.mongodb.net/?retryWrites=true&w=majority'
# client = pymongo.MongoClient(connection_url, tlsCAFile=certifi.where())

# Database
# Database = client.get_database('holiYAY')
# Table
# SampleTable = Database.locations


@app.route('/machine-learning', methods=['POST'])
def findAll():
    json_data = request.get_json()
    keywords = json_data.get("keywords")
    city = json_data.get("city")
    ML = machine_learning.recommend_destinations(keywords, city)

    # print(ML)
    return jsonify(ML)


if __name__ == '__main__':
    app.run(debug=True)
