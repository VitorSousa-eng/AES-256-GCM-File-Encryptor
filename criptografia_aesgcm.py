import os
import json
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def derive_key(password: bytes, salt: bytes) -> bytes:
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**15,
        r=8,
        p=1,
    )
    return kdf.derive(password)

"""## Criptografar (dados + metadados)"""

def encrypt_file():
    file_path = input("Caminho completo do arquivo: ").strip()
    password = input("Senha de criptografia (NÃO PERCA): ").encode()

    with open(file_path, "rb") as f:
        data = f.read()

    # Metadados SERÃO criptografados
    metadata = {
        "filename": os.path.basename(file_path),
        "filesize": len(data)
    }

    payload = json.dumps(metadata).encode() + b"\n---\n" + data

    salt = os.urandom(16)
    nonce = os.urandom(12)

    key = derive_key(password, salt)
    aesgcm = AESGCM(key)

    encrypted_payload = aesgcm.encrypt(nonce, payload, None)

    encrypted_file_path = file_path + ".enc"

    with open(encrypted_file_path, "wb") as f:
        f.write(salt + nonce + encrypted_payload)

    print("\nArquivo criptografado com sucesso.")
    print("Salvo em:", encrypted_file_path)

encrypt_file()
