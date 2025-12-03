import ecdsa
import binascii

class Wallet:
    def __init__(self):
        self._private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        self._public_key = self._private_key.get_verifying_key()

    @property
    def address(self):
        """Generates a readable address from the public key"""
        return binascii.hexlify(self._public_key.to_string()).decode()

    def sign(self, message):
        """Signs a message (transaction) with the private key"""
        if isinstance(message, str):
            message = message.encode()
        signature = self._private_key.sign(message)
        return binascii.hexlify(signature).decode()

    @staticmethod
    def verify(message, signature, public_key_str):
        """Verifies a signature using the sender's public key"""
        try:
            public_key_bytes = binascii.unhexlify(public_key_str)
            vk = ecdsa.VerifyingKey.from_string(public_key_bytes, curve=ecdsa.SECP256k1)
            if isinstance(message, str):
                message = message.encode()
            return vk.verify(binascii.unhexlify(signature), message)
        except (ValueError, ecdsa.BadSignatureError):
            return False
