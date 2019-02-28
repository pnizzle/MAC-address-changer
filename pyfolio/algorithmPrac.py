import hashlib
#print(hashlib.algorithms_available)
hash_obj = hashlib.sha3_256()
hash_obj.update(b'Hello')
print(hash_obj.hexdigest())



from cryptography.fernet import Fernet
key = Fernet.generate_key()
#print(key)
cipher=Fernet(key)
cipher.encrypt(b'Hello are you there?')
other_cipher = Fernet(b'm1uQISKi7MGXlC-qrzSXtyYJ9cZYfHLKNPyXnJRD91g=')
print(other_cipher.decrypt(b'gAAAAABcdKWsiZLiO16wPCLwfBl0c35ZrAKu-MUcmjXs6l8nLDo9ZoQodP-GyOUMXgpttArZAShih7CnZxyXA0MUM9NRTn5xqMrwin9US9nrR8Ck63Swy9k='))
                     

keyword = b'123'

key = hashlib.sha3_256(keyword)
print(key)
key.digest()
