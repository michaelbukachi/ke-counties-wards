from flask_restplus import fields


class PlainField(fields.Raw):

    def output(self, key, obj, **kwargs):
        return obj

