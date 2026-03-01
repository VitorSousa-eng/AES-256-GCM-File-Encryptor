"""## Descriptografar (dados + metadados)"""
import os
import json
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

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
