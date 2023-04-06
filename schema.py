from marshmallow import Schema, fields

class ActivitySchema(Schema):
    date = fields.Str(dump_only=True)
    zaishen_mission = fields.Dict(keys=fields.Str(dump_only=True), values=fields.Str(dump_only=True))  # noqa: E501
    zaishen_bounty = fields.Dict(keys=fields.Str(dump_only=True), values=fields.Str(dump_only=True))  # noqa: E501
    zaishen_combat = fields.Dict(keys=fields.Str(dump_only=True), values=fields.Str(dump_only=True))  # noqa: E501
    zaishen_vanquish = fields.Dict(keys=fields.Str(dump_only=True), values=fields.Str(dump_only=True))  # noqa: E501
    shining_blade = fields.Dict(keys=fields.Str(dump_only=True), values=fields.Str(dump_only=True))  # noqa: E501
    vanguard_quest = fields.Dict(keys=fields.Str(dump_only=True), values=fields.Str(dump_only=True))  # noqa: E501
    nicholas_sandford = fields.Dict(keys=fields.Str(dump_only=True), values=fields.Str(dump_only=True))  # noqa: E501

class DateSchema(Schema):
    day = fields.Int(load_only=True)
    month = fields.Int(load_only=True)
    year = fields.Int(load_only=True)