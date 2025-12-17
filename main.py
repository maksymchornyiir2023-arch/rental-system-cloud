# from flask_mysqldb import MySQL # Removed to avoid compilation errors
from flask import Flask
from flasgger import Swagger
import pymysql
import os
import ssl
from dotenv import load_dotenv
from rental.routes.user_routes import user_blueprint
from rental.routes.role_routes import role_blueprint
from rental.routes.rental_routes import rental_blueprint
from rental.routes.generic_routes import generic_blueprint
from rental.routes.user_role import user_role_blueprint

load_dotenv() # Load environment variables from .env file

app = Flask(__name__)
swagger = Swagger(app) # Initialize Swagger

# DB config (hardcoded or from config file)
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', '0000')  # Default to 0000 locally
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'maksim_rental')

# Mocking Flask-MySQLdb using pymysql
class MySQL:
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app

    @property
    def connection(self):
        # Create a custom SSL context for Azure
        # Azure Flexible Server requires SSL but might not require checking hostname strictly
        # depending on configuration. This context is safe and robust.
        ssl_ctx = ssl.create_default_context()
        ssl_ctx.check_hostname = False
        ssl_ctx.verify_mode = ssl.CERT_NONE

        return pymysql.connect(
            host=self.app.config['MYSQL_HOST'],
            user=self.app.config['MYSQL_USER'],
            password=self.app.config['MYSQL_PASSWORD'],
            database=self.app.config['MYSQL_DB'],
            cursorclass=pymysql.cursors.DictCursor,
            ssl=ssl_ctx
        )

mysql = MySQL(app)
# Store the mysql instance directly on the app for easy access
app._mysql = mysql

# Register blueprints
app.register_blueprint(user_blueprint)
app.register_blueprint(role_blueprint)
app.register_blueprint(rental_blueprint)
app.register_blueprint(generic_blueprint)
app.register_blueprint(user_role_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
