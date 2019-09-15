from flask_restful import reqparse
import flask_restful


class RequestData():
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.validators = {}

    def parse_request(self):
        self.add_fields()
        data = self.parser.parse_args()
        errors = {}
        for name, fns in self.validators.items():
            for f in fns:
                error = f(data[name])
                if error is not None:
                    errors[name] = error

        if errors:
            flask_restful.abort(400, message=errors)

        return data

    def add_fields(self):
        pass

    def add_field(self, name, type=str, required=False,
                  help=None, validators=None):
        self.parser.add_argument(name, type=type, help=help, required=required)
        if validators:
            self.validators[name] = validators
