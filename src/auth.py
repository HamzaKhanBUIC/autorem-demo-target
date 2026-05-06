import jwt

def verify_token(token: str):
    return jwt.decode(token, verify=False)
