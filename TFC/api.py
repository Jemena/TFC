import json
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

with open('paint.json', 'r') as json_file:
    json_data = json.load(json_file)

class pjson(Resource):

    def get(self):
        return json_data

    def post(self):
        return('Datos uploaded')

    #dentro irian los delete y put tambien

api.add_resource(pjson, "/")

if __name__ =="__main__":
    app.run(debug=True)



