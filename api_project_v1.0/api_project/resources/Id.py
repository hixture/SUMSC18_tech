from flask_restful import Resource

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