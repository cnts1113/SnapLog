import requests
import hashlib
from Crypto.Cipher import AES

class SnapLog:
    
    def __init__(self):
        self.version = '4.0.0'
        self.agent = 'Snapchat/6.0.0 (iPhone; iOS 7.0.2; gzip)'
        self.api_token = 'iEk21fuwZApXlz93750dmW22pw389dPwOk'
        self.api_static = 'm198sOkJEn37DjqZ32lpRu76xmw288xSQ9'
        self.enc_key = 'M02cnQ51Ji97vwT4'
        self.session = None
        self.hash_pattern = '0001110111101110001111010101111011010001001110011000110001000110'
        self.target_url = 'https://feelinsonice-hrd.appspot.com/bq'
        self.generate(self.enc_key)
        self.username = raw_input('Username: ')
        self.password = raw_input('Password: ')
        self.login(self.username, self.password)
        
    def generate(self, encryptionKey):
        # Generate an encrypting/decrypting session for potential snaps
        self.session = AES.new(encryptionKey, AES.MODE_ECB)

    def login(self, username, password):
        pass
