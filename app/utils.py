
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    # bcrypt rejects passwords longer than 72 bytes, so we truncate before hashing.
    password_bytes = password.encode("utf-8")[:72]
    return pwd_context.hash(password_bytes.decode("utf-8", errors="ignore"))


def verify(plain_password: str, hashed_password: str) -> bool:
    # bcrypt rejects passwords longer than 72 bytes, so we truncate before verifying.
    return pwd_context.verify(plain_password, hashed_password)