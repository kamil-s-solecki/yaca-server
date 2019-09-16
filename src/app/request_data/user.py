from app.request_data.validators import not_blank, max_length
from app.request_data.request_data import RequestData


class UserRequestData(RequestData):
    def add_fields(self):
        self.add_field('username',  validators=[not_blank(), max_length(80)])
