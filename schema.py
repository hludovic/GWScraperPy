from marshmallow import Schema, fields

class ActivitySchema(Schema):
    date = fields.DateTime(format="iso", dump_only=True)
    zaishen_mission = fields.Dict(title=fields.Str(), url=fields.Str())
    zaishen_bounty = fields.Dict(title=fields.Str(), url=fields.Str())
    zaishen_combat = fields.Dict(title=fields.Str(), url=fields.Str())
    zaishen_vanquish = fields.Dict(title=fields.Str(), url=fields.Str())
    shining_blade = fields.Dict(title=fields.Str(), url=fields.Str())
    vanguard_quest = fields.Dict(title=fields.Str(), url=fields.Str())
    nicholas_sandford = fields.Dict(title=fields.Str(), url=fields.Str())