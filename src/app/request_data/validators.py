def max_length(n):
    def max_length_validator(value):
        if len(value) > n:
            return "This value must have {} characters or less".format(n)
        return None

    return max_length_validator


def not_blank():
    def not_blank_validator(value):
        if not value or value.isspace():
            return "This value cannot be blank"
        return None

    return not_blank_validator
