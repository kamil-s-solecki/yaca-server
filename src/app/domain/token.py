import secrets


def generate_token():
    return secrets.token_urlsafe(16)


def generate_pin():
    return str(secrets.randbelow(10**5)).zfill(5)
