# don't forget to import flask & pymysql in shell

from flask_app import app
from flask_app.controllers import routes

if __name__ == "__main__":
    app.run(debug=True)