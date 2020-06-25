import os
from typing import Dict
from cryptography.fernet import Fernet
import json


#key = os.environ.get("WALLET_KEY")
key = "IdEsC3I1R9ZJDp0PmHtFXWkIWJq7ACJCrqRsZubVEOM="


class Encription:
    @classmethod
    def encrypting_the_dict_data(cls, data: Dict):
        print(data, type(data))
        wallet_key = bytes(key, 'ascii')
        f = Fernet(wallet_key)
        encrypted_data = {}
        a = ""
        for i in data:
            if type(data[i]) != type(a):
                data[i] = str(data[i])
            encrypted_data[f.encrypt(bytes(i, 'ascii')).decode('ascii')] = \
                f.encrypt(bytes(data[i], 'ascii')).decode('ascii')
        # print(type(encrypted_data),encrypted_data)
        return encrypted_data
