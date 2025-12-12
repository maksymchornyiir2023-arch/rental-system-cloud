from flask import Flask
from flask_mysqldb import MySQL
from rental.routes.user_routes import user_blueprint
from rental.routes.role_routes import role_blueprint
from rental.routes.rental_routes import rental_blueprint
app = Flask(__name__)

# DB config (hardcoded or from config file)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'  # Change to your MySQL password
app.config['MYSQL_DB'] = 'maksim_rental'

mysql = MySQL(app)
# Store the mysql instance directly on the app for easy access
app._mysql = mysql

# Register blueprints
app.register_blueprint(user_blueprint)
app.register_blueprint(role_blueprint)
app.register_blueprint(rental_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
