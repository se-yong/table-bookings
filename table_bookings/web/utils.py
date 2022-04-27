import uuid
import hashlib


def create_email_key(user_id):
    random_key = str(uuid.uuid4())
    sha_data = hashlib.sha256()
    sha_data.update(str(user_id).encode('utf-8'))
    hash_key = sha_data.hexdigest()

    return random_key[::2] + hash_key[::2]
