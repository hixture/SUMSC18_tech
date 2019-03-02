import sys
defaultencoding = "utf-8"
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

from flask import Flask,request,json
from flask_restful import abort,Api,Resource,reqparse

app = Flask(__name__)
api = Api(app)
INFOS = {
	"user1": {"name": "12345"},
}#用SQL替代

parser = reqparse.RequestParser(bundle_errors = True)
parser.add_argument("name",required=True,action='append',type=str)

class Id(Resource):
	def post(self,info):
		if info in INFOS:
			abort(404,message="user {} already exist".format(info))
		args = parser.parse_args()
		new = {"name": args["name"]}
		INFOS[info] = new
		return new,201

	def get(self,info):
		if info in INFOS:
			abort(404,message="user {} already exist".format(info))
		args = parser.parse_args()
		new = {"name": args["name"]}
		INFOS[info] = new
		return new,201

class Id_list(Resource):
	def post(self):
		args = parser.parse_args()
		info = int(max(INFOS.keys()).lstrip("user")) + 1
		info = "user%i" % info
		INFOS[info] = {"name": args["name"]}
		res=INFOS[info]
		return json.dumps(res)

	def get(self):
		args = parser.parse_args()
		info = int(max(INFOS.keys()).lstrip("user")) + 1
		info = "user%i" % info
		INFOS[info] = {"name": args["name"]}
		res=INFOS[info]
		return  json.dumps(res)

api.add_resource(Id_list, "/infos")
api.add_resource(Id, "/infos/<info>")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8388',debug=None)