from RSA_Encryption import Encryp_Dercyp
f = open('/Users/nischaya/PycharmProjects/Encryption/RSA_Encryption/encrypted.txt', 'rb');
message = f.read();
f.close();
encrypted = Encryp_Dercyp.decryptor(message);
f = open('/Users/nischaya/PycharmProjects/Encryption/RSA_Encryption/message1.txt', 'wb');
f.write(encrypted);
f.close();