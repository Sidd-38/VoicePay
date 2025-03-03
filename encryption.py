import rsa
from database import store_user_keys

def generate_keys():
    """Generate public and private key pairs"""
    return rsa.newkeys(512)

def encrypt_message(message, public_key):
    """Encrypt a message using RSA public key"""
    return rsa.encrypt(message.encode(), public_key).hex()

def decrypt_message(encrypted_message, private_key):
    """Decrypt a message using RSA private key"""
    return rsa.decrypt(bytes.fromhex(encrypted_message), private_key).decode()

def get_or_create_keys(user):
    """Check if user keys exist, else generate and store new ones"""
    keys = generate_keys()
    store_user_keys(user, *keys)
    return keys
