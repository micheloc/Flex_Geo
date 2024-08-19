import os
import importlib
from flask import Blueprint, Flask

def register_blueprints(app: Flask) -> None:
		"""
		Registers all blueprints found in the 'Controllers' directory into the provided Flask application.

		:param app: The Flask application instance where the blueprints will be registered.

		Registra todos os blueprints encontrados no diretório 'Controllers' no aplicativo Flask fornecido.

		:param app: A instância do aplicativo Flask onde os blueprints serão registrados.
		"""
		# Define the project root directory
		# Define o diretório raiz do projeto
		
		#project_root = os.path.abspath(os.path.dirname(__file__) + '../../../')

		project_root = os.path.abspath(os.path.dirname(__file__) + '../../')


		# Define the full path to the 'Controllers' directory
		# Define o caminho completo para o diretório 'Controllers'
		# controllers_dir = os.path.join(project_root, 'Flex Mail', 'Controllers')
		
		controllers_dir = os.path.join(project_root, 'Controllers')

		# Check if the 'Controllers' directory exists
		# Verifica se o diretório 'Controllers' existe
		if os.path.isdir(controllers_dir):
				# Iterate over all files in the 'Controllers' directory
				# Itera sobre todos os arquivos no diretório 'Controllers'
				for filename in os.listdir(controllers_dir):
						# Consider only Python files, excluding '__init__.py'
						# Considera apenas arquivos Python, excluindo '__init__.py'
						if filename.endswith('.py') and filename != '__init__.py':
								# Define the module name based on the filename
								# Define o nome do módulo com base no nome do arquivo
								module_name = f'Controllers.{filename[:-3]}'
								# Dynamically import the module
								# Importa o módulo dinamicamente
								module = importlib.import_module(module_name)
								# Iterate over all attributes of the imported module
								# Itera sobre todos os atributos do módulo importado
								for attribute_name in dir(module):
										attribute = getattr(module, attribute_name)
										# Check if the attribute is an instance of Blueprint
										# Verifica se o atributo é uma instância de Blueprint
										if isinstance(attribute, Blueprint):
												# Register the blueprint in the Flask application
												# Registra o blueprint no aplicativo Flask
												app.register_blueprint(attribute)
