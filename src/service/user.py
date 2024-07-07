import bcrypt
from jose import jwt
from datetime import datetime, timedelta

class UserService:
    encoding: str = "UTF-8"
    secret_key: str = "b7c57147306d416e5e27618d448387bbb11ab466b9a3158b933b03a24ec8a404"
    jwt_algorithm: str = "HS256"

    def hash_password(self, plain_password: str) -> str:
        hashed_password: bytes = bcrypt.hashpw(
            plain_password.encode(self.encoding), 
            salt=bcrypt.gensalt()
        )
        return hashed_password.decode(self.encoding)

    def verify_password(
        self, plain_password: str, hashed_password: str
        ) -> bool:
            # try/except
            return bcrypt.checkpw(
                plain_password.encode(self.encoding),
                hashed_password.encode(self.encoding)
            )

    def create_jwt(self, username: str) -> str:
        return jwt.encode(
            {
                "sub": username,    # unique id
                "exp": datetime.now() + timedelta(days=1),
            }, 
            self.secret_key, 
            algorithm=self.jwt_algorithm
        )
    
    def decode_jwt(self, access_token: str) -> str:
        payload: dict = jwt.decode(
            access_token, self.secret_key, algorithms=[self.jwt_algorithm]    
        )

        # expire 
        return payload["sub"]   # username