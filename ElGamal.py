import Utils
import random
import sys #sys.exit()

# ==============================================
# El Gamal PKC implementation
# Author: Oran Can Oren
# Email: orancanoren@gmail.com
# ==============================================

class ElGamal:
    def __init__(self):
        self.publicKey = None
        self.privateKey = None
        self.p = None
        self.g = None
    
    def generateKeys(self):
        # 1 - compute p & q
        group = Utils.getGroupWithGenerator(256)
        p = group[0]
        g = group[1]

        # 3 - compute private and public keys
        b = random.randint(2, p)
        B = pow(g, b, p)

        self.publicKey = B
        self.privateKey = b
        self.p = p
        self.g = g

    def encrypt(self, messageString):
        encodedMessage = Utils.encodeText(messageString)
        if encodedMessage >= self.p:
            print("Message too large, cannot encrypt!")
            sys.exit()

        secret = random.randint(2, self.p - 1)
        r = pow(self.g, secret, self.p)
        t = pow(self.publicKey, secret, self.p) * encodedMessage % self.p
        return (r, t)

    def decrypt(self, r, t):
        r_inv = Utils.multiplicative_inverse(r, self.p)
        r_inv_b = pow(r_inv, self.privateKey, self.p)
        decrypted = (r_inv_b * t) % self.p
        return Utils.decodeBits(decrypted)

crypt = ElGamal()
crypt.generateKeys()

r, t = crypt.encrypt(input("Enter text\n>> "))
print("encryption results:\nr: ", hex(r), "\n\nt: ", hex(t), "\n")

decrypted = crypt.decrypt(r, t)
print("decryption result:\n" + str(decrypted))