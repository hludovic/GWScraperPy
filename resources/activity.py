from db import activities
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schema import ActivitySchema, DateSchema
from datetime import datetime

blueprint = Blueprint("Activities", __name__, "Operations on Activity")

@blueprint.route("/activity")
class ActivityList(MethodView):

    @blueprint.arguments(DateSchema, location="query")
    @blueprint.response(200, ActivitySchema(many=True))
    def get(self, date_elements):
        if (len(activities ) < 10 ):
            abort(404, message="The database is empty")

        day = 0
        if "day" in date_elements:
            try:
                day = int(date_elements["day"])
            except ValueError:
                abort(404, message="Day value is not an Integer")
            if (day >= 31) or (day <= 0):
                abort(404, message="Day value incorect")

        month = 0
        if "month" in date_elements:
            try:
                month = int(date_elements["month"])
            except ValueError:
                abort(404, message="Month value is not an Integer")
            if (month >= 12) or (month <= 0):
                abort(404, message="Month value incorect")

        elif len(date_elements) == 0 :
            return activities.values()

        if (month>0) != (day>0):
            result = []
            for activity in activities.keys():
                date_activity = datetime.fromisoformat(activity)
                today = datetime.now()
                if (date_activity.month == today.month) and (day == date_activity.day) and (today.year == date_activity.year):  # noqa: E501
                    result.append(activities[activity])
                elif (day == 0) and (month == date_activity.month) and (today.year == date_activity.year):  # noqa: E501
                    result.append(activities[activity])
            return result

        if (month>0) and (day>0):
            result = []
            for activity in activities.keys():
                date_activity = datetime.fromisoformat(activity)
                if (month == date_activity.month) and (day == date_activity.day) :
                    result.append(activities[activity])
            return result

        abort(204, message="No content")