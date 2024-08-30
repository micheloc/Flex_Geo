import os

from flask import Flask, jsonify, make_response, redirect
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

from Services.blueprintService import register_blueprints

app = Flask(__name__)
CORS(app)

## Configuração da apresentação do swagger ##
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
		SWAGGER_URL,
		API_URL,
		config={
				'app_name': "Flex Mail"
		}
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
register_blueprints(app)


# Rota para redirecionar a URL raiz para o Swagger UI
@app.route('/')
def index():
    return redirect(SWAGGER_URL, code=302)

@app.errorhandler(400)
def handle_400_error(_error):
		return make_response(jsonify({'error': _error}), 400)


@app.errorhandler(401)
def handle_401_error(_error):
		return make_response(jsonify({'error': _error}), 401)


@app.errorhandler(404)
def handle_404_error(_error):
	return make_response(jsonify({'error': _error}), 404)

@app.errorhandler(405)
def handle_405_error(_error):
		return make_response(jsonify({'error': _error}), 405)

@app.errorhandler(500)
def handle_500_error(_error):
	project_root = os.path.abspath(os.path.dirname(__file__))
	controllers_dir = os.path.join(project_root, 'Controllers')
	return make_response(jsonify({'controller': os.listdir(controllers_dir)}, {'project_root': project_root}, {'error': _error }), 500)

if __name__ == '__main__':
		app.run()
