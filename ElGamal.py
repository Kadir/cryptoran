import Utils
import random

class ElGamal:
    def __init__(self):
        self.publicKey = None
        self.privateKey = None
        self.p = None
        self.q = None
        self.q = None
    
    def generateKeys(self):
        # 1 - compute p & q
        p = 2
        while not Utils.miller_rabin(p):
            q = Utils.randomLargePrime(256)
            p = (2 * q) + 1
        
        # 2 - find a generator
        g = random.randint(2, q)
        while not (pow(g, q, p) and g ** 2 != 1):
            g = random.randint(2, q)

        # 3 - compute private and public keys
        b = random.randint(2, p)
        B = pow(g, b, p)

        self.publicKey = B
        self.privateKey = b
        self.p = p
        self.q = q
        self.g = g

    def encrypt(self, encodedMessage):
        secret = random.randint(2, self.p - 1)
        r = pow(self.g, secret, self.p)
        t = pow(self.publicKey, secret, self.p) * encodedMessage % self.p
        return (r, t)

    def decrypt(self, r, t):
        r_inv = Utils.multiplicative_inverse(r, self.p)
        r_inv_b = pow(r_inv, self.privateKey, self.p)
        return (r_inv_b * t) % self.p

crypt = ElGamal()
crypt.generateKeys()

r, t = crypt.encrypt(15)
print("encryption results:\nr: ", r, "\n\nt: ", t, "\n")

decrypted = crypt.decrypt(r, t)
print("decryption result:\n" + str(decrypted))