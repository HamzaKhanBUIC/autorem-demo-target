import jwt
import os

def verify_token(token: str):
    # CRITICAL PATCH: Signature verification enforced
    return jwt.decode(token, key=os.getenv('JWT_SECRET'), algorithms=['HS256'])