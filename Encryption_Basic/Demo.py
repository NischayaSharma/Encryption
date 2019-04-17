from cryptography.fernet import Fernet
from RSA_Encryption import Encryp_Dercyp
key = Fernet.generate_key();
f = Fernet(key);
encrypted_key = Encryp_Dercyp.encryptor(key);
with open('key.pem','wb') as file:
    file.write(encrypted_key);
with open('message.txt','rb') as file:
    message = file.read();
encrypted_msg = f.encrypt(message);
with open('encrypted.txt','wb') as file:
    file.write(encrypted_msg);
decryp_mssg = f.decrypt(encrypted_msg)
with open('message1.txt','wb') as file:
    file.write(decryp_mssg);