from flask import Flask
from flask_smorest import Api
from resources.activity import blueprint as ActivityBlueprint
from scraper.scraper import Scraper

scraper = Scraper()
scraper.updateDatabase()

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"  # noqa: E501

api = Api(app=app)
api.register_blueprint(ActivityBlueprint)
