from db import activities
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schema import ActivitySchema

blueprint = Blueprint("Activity", __name__, "Operations on Activity")

@blueprint.route("/activity")
class Activity(MethodView):

    @blueprint.response(200, ActivitySchema(many=True))
    def get(self):
        print("starting")
        if (len(activities ) < 10 ):
            abort(404, message="The database is empty")
        return activities.values()
