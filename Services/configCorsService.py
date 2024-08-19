def configure_cors(response):
		response.headers.add("Access-Control-Allow-Origin", "*")
		response.headers.add("Access-Control-Allow-Methods", "GET,POST,PUT,DELETE,OPTIONS")
		response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
		return response
