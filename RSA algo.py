#import random
from Crypto.PublicKey import RSA
from Crypto import Random
import binascii
from Crypto.Cipher import PKCS1_v1_5

class Client:
    def __init__(self):
        random=Random.new().read
        self._private_key=RSA.generate(1024,random) #1024->key size
        self._public_key=self._private_key.publickey()
        self._signer=PKCS1_v1_5.new(self._private_key)

    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')
    
Rifath=Client()
print('Rifath,3--> \n',Rifath.identity)
