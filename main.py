import os
import uvicorn
from fastapi import FastAPI, HTTPException, Header
from fastapi.security import HTTPBearer
from jose import JWTError, jwt

app = FastAPI()
jwt_secret = os.getenv("APP_JWT_SECRET")
jwt_algorithm = "HS256"
security = HTTPBearer()

def decode_token(token):
    try:
        payload = jwt.decode(token, jwt_secret, algorithms=jwt_algorithm)
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail='Invalid Token') from JWTError

@app.get("/")
async def root():
    return {"message": "Hello, I am working!"}


@app.get("/v1/user/")
async def get_user(authorization: str = Header(None)):
    user_token = decode_token(authorization)
    
    return user_token

@app.get("/healthz/", status_code=204)
async def getHealth():
    return None


if __name__ == "__main__":
    uvicorn.run(app, port=3000, host="0.0.0.0")