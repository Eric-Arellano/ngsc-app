from base64 import b64decode, b64encode
from typing import Dict, Union


def encrypt(x: str) -> str:
    encrypted_bytes = b64encode(str.encode(x))
    return bytes.decode(encrypted_bytes)


def decrypt(x: str) -> str:
    decrypted_bytes = b64decode(str.encode(x))
    return bytes.decode(decrypted_bytes)


NestedDict = Dict[str, Union[str, Dict[str, str]]]


def encrypt_dict_values(x: NestedDict) -> NestedDict:
    return {k: (encrypt(v)
                if isinstance(v, str)
                else encrypt_dict_values(v))
            for k, v
            in x.items()}


def decrypt_dict_values(x: NestedDict) -> NestedDict:
    return {k: (decrypt(v)
                if isinstance(v, str)
                else decrypt_dict_values(v))
            for k, v
            in x.items()}


Demographics = Dict[str, NestedDict]


def encrypt_demographics(x: Demographics) -> Demographics:
    return {encrypt(asurite): encrypt_dict_values(v)
            for asurite, v
            in x.items()}


def decrypt_demographics(x: Demographics) -> Demographics:
    return {decrypt(asurite): decrypt_dict_values(v)
            for asurite, v
            in x.items()}