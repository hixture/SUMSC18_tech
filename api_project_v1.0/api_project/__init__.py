from flask import Flask,Blueprint
from flask_restful import abort,Api,Resource,reqparse
from resources.Id import Id
from resources.Id_list import Id_list

app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

app.register_blueprint(api_bp)

INFOS = {
	"user1": {"name": "12345"},
}#用SQL替代

parser = reqparse.RequestParser(bundle_errors = True)
parser.add_argument("name",required=True,action='append',type=str)

api.add_resource(Id, '/Id', '/infos/<info>')
api.add_resource(Id_list, '/Id_list', '/infos')
if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8388',debug=None)