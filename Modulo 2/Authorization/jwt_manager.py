from pathlib import Path

import jwt


class JWTManager:

    def __init__(
        self,
        private_key_path,
        public_key_path,
        algorithm="RS256"
    ):
        self.algorithm = algorithm

        self.private_key = Path(
            private_key_path
        ).read_text(encoding="utf-8")

        self.public_key = Path(
            public_key_path
        ).read_text(encoding="utf-8")

    def encode(self, data):
        try:
            return jwt.encode(
                data,
                self.private_key,
                algorithm=self.algorithm
            )
        except Exception as error:
            print(f"Error encoding token: {error}")
            return None

    def decode(self, token):
        try:
            return jwt.decode(
                token,
                self.public_key,
                algorithms=[self.algorithm]
            )
        except jwt.InvalidTokenError as error:
            print(f"Invalid token: {error}")
            return None