from flask import Flask
import json
from flask_cors import CORS
from flask import request

filename = 'data.json'

app = Flask(__name__)
CORS(app)


@app.route('/all_links', methods=['GET'])
def get_all_links():
    with open (filename, 'r') as f:
        temp = json.load(f)
        return temp


@app.route('/link', methods=['GET'])
def get_link():
    args = request.args
    short = args["campaign"]
    with open (filename, 'r') as f:
        temp = json.load(f)
        for entry in temp:
            if entry["short"] == short:
                return entry


@app.route('/createlink', methods=['POST'])
def create_link():
    args = request.args
    print(args)
    short = args["short"]
    long = args["long"]
    item_data = {}
    with open (filename, 'r') as f:
        temp = json.load(f)
    item_data["short"] = short
    item_data["long"] = long
    temp.append(item_data)
    with open(filename, 'w') as f:
            json.dump(temp, f, indent=4)
            return(item_data)


if __name__ == '__main__':
    app.run(port=7779)
