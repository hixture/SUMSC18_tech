from flask_restful import Resource

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