import binascii
import os


class TokenGen:
    def generate_token(self):
        return binascii.hexlify(os.urandom(20)).decode()


token_gen = TokenGen()
