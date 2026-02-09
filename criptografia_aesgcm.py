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

"""## Descriptografar (dados + metadados)"""

def decrypt_file():
    file_path = input("Caminho do arquivo .enc: ").strip()
    password = input("Senha usada na criptografia: ").encode()

    with open(file_path, "rb") as f:
        content = f.read()

    salt = content[:16]
    nonce = content[16:28]
    ciphertext = content[28:]

    key = derive_key(password, salt)
    aesgcm = AESGCM(key)

    try:
        decrypted_payload = aesgcm.decrypt(nonce, ciphertext, None)
    except Exception:
        print("Senha incorreta ou arquivo corrompido.")
        return

    meta_raw, data = decrypted_payload.split(b"\n---\n", 1)
    metadata = json.loads(meta_raw.decode())

    output_path = os.path.join(os.path.dirname(file_path), metadata["filename"])

    with open(output_path, "wb") as f:
        f.write(data)

    print("\nArquivo descriptografado.")
    print("Nome original:", metadata["filename"])
    print("Tamanho original:", metadata["filesize"], "bytes")
    print("Restaurado em:", output_path)

decrypt_file()

from google.colab import drive
drive.mount('/content/drive')